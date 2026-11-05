"""Trusted host for a restricted, in-memory SQL method language. No Python eval."""
import hashlib, json, os, re, sqlite3, time
from pathlib import Path

def digest(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':'),allow_nan=False).encode()).hexdigest()

class Engine:
    def __init__(self, rows):
        if not rows or len(rows)>20000: raise ValueError('bounded nonempty observations required')
        self.con=sqlite3.connect(':memory:')
        self.con.row_factory=sqlite3.Row
        self.con.execute('PRAGMA temp_store=MEMORY')
        if hasattr(self.con, 'enable_load_extension'):
            self.con.enable_load_extension(False)
        self.columns=list(rows[0])
        if any(not re.fullmatch('[a-z][a-z_]*',k) for k in self.columns): raise ValueError('invalid column')
        self.con.execute('CREATE TABLE observations ('+','.join('"'+k+'" NUMERIC' for k in self.columns)+')')
        self.con.executemany('INSERT INTO observations VALUES ('+','.join('?' for _ in self.columns)+')',[[r[k] for k in self.columns] for r in rows])
        self.con.commit()
        self.con.execute('PRAGMA query_only=ON')
        for limit,value in [(sqlite3.SQLITE_LIMIT_LENGTH,100000),(sqlite3.SQLITE_LIMIT_SQL_LENGTH,16000),(sqlite3.SQLITE_LIMIT_COLUMN,80),(sqlite3.SQLITE_LIMIT_EXPR_DEPTH,60),(sqlite3.SQLITE_LIMIT_COMPOUND_SELECT,10),(sqlite3.SQLITE_LIMIT_ATTACHED,0),(sqlite3.SQLITE_LIMIT_FUNCTION_ARG,16),(sqlite3.SQLITE_LIMIT_VARIABLE_NUMBER,40),(sqlite3.SQLITE_LIMIT_VDBE_OP,50000)]:
            self.con.setlimit(limit,value)
        self.con.set_authorizer(self.authorize)
        self.steps=0
        self.last_query_cost=None
    @staticmethod
    def authorize(action,a,b,db,trigger):
        if action in (sqlite3.SQLITE_SELECT,sqlite3.SQLITE_RECURSIVE): return sqlite3.SQLITE_OK
        if action==sqlite3.SQLITE_READ and a=='observations' and db=='main': return sqlite3.SQLITE_OK
        if action==sqlite3.SQLITE_FUNCTION and b in {'sum','avg','min','max','count','total','abs','round','coalesce','nullif','ifnull','row_number','rank','dense_rank','lag','lead','first_value','last_value'}: return sqlite3.SQLITE_OK
        return sqlite3.SQLITE_DENY
    def query(self, sql, params):
        if not isinstance(sql,str) or len(sql)>16000 or not isinstance(params,dict): raise ValueError('SQL/parameter bounds')
        if len(params)>40 or any(not isinstance(v,(str,int,float,type(None))) or isinstance(v,str) and len(v)>1000 for v in params.values()): raise ValueError('parameter bounds')
        self.steps=0; started=time.monotonic()
        def progress():
            self.steps+=1000
            return int(self.steps>3000000 or time.monotonic()-started>3)
        self.con.set_progress_handler(progress,1000)
        success=False
        try:
            cur=self.con.execute(sql,params); rows=cur.fetchmany(101)
            if len(rows)>100: raise ValueError('result exceeds 100 rows; aggregate or LIMIT')
            result=[dict(r) for r in rows]
            if len(json.dumps(result,allow_nan=False))>40000: raise ValueError('result bytes exceeded')
            success=True
            return {'rows':result,'sql_steps_approx':self.steps,'wall_seconds':time.monotonic()-started}
        finally:
            self.last_query_cost={'sql_steps_approx':self.steps,'wall_seconds':time.monotonic()-started,'success':success}

class Store:
    def __init__(self,path):
        self.path=Path(path)
        self.data={'methods':{},'fields':[],'state_note':'','handoff':'','history':[]}
        if self.path.exists():
            try:
                envelope=json.loads(self.path.read_text(encoding='utf8'))
                if digest(envelope['data'])!=envelope['sha256']: raise ValueError('digest mismatch')
                self.data=envelope['data']
                if set(self.data)!={'methods','fields','state_note','handoff','history'}: raise ValueError('state schema')
            except Exception as e: raise ValueError('saved state corrupt; preserved, not silently reset') from e
    def commit(self):
        self.path.parent.mkdir(parents=True,exist_ok=True)
        tmp=self.path.with_suffix('.tmp')
        tmp.write_text(json.dumps({'data':self.data,'sha256':digest(self.data)},indent=2,allow_nan=False),encoding='utf8')
        os.replace(tmp,self.path)
    def save_method(self,m):
        if set(m)!={'id','sql','guard','context_fields','note'}: raise ValueError('method fields differ')
        if not isinstance(m['id'],str) or not re.fullmatch('[a-zA-Z0-9_-]{1,50}',m['id']): raise ValueError('method id')
        if not isinstance(m['sql'],str) or len(m['sql'])>16000 or not isinstance(m['guard'],dict) or len(m['guard'])>20: raise ValueError('method bounds')
        if any(not isinstance(v,(str,int,float,bool,type(None))) for v in m['guard'].values()): raise ValueError('guard must have scalar equality values')
        self.validate_fields(m['context_fields'])
        if not isinstance(m['note'],str) or len(m['note'])>2000: raise ValueError('note bounds')
        self.data['history'].append({'kind':'method','previous':self.data['methods'].get(m['id']),'new':m})
        self.data['methods'][m['id']]=m; self.commit()
    @staticmethod
    def validate_fields(fields):
        if not isinstance(fields,list) or len(fields)>30 or any(not isinstance(x,str) or not re.fullmatch('[a-z][a-z_]*',x) for x in fields): raise ValueError('context fields')
    def save_state(self,fields,note):
        self.validate_fields(fields)
        if not isinstance(note,str) or len(note)>2000: raise ValueError('state note')
        self.data['fields']=fields; self.data['state_note']=note; self.commit()
    def project(self,context):
        return {k:context.get(k,'<MISSING>') for k in self.data['fields']}
    def get_method(self,name,context):
        m=self.data['methods'][name]
        mismatch={k:{'expected':v,'current':context.get(k,'<MISSING>')} for k,v in m['guard'].items() if k not in context or context[k]!=v}
        if mismatch: raise ValueError('guard rejected: '+json.dumps(mismatch))
        missing=[k for k in m['context_fields'] if k not in context]
        if missing: raise ValueError('required context absent: '+','.join(missing))
        return m
