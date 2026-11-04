"""Read-only structural continuity and local source-binding checks; no truth oracle."""
from pathlib import Path, PurePosixPath
import argparse, collections, hashlib, json, math, re, sys

SCHEMA = 'rel.lessons.v1'
STATES = {'candidate', 'supported', 'needs_recheck', 'retired'}
FIELDS = {'id', 'revision', 'state', 'claim', 'scope', 'apply_when', 'avoid_when',
          'next_action', 'next_check', 'requires', 'sources'}
IDENTITY = re.compile(r'[A-Za-z0-9][A-Za-z0-9_.-]{0,127}\Z')
DIGEST = re.compile(r'[0-9a-f]{64}\Z')

def need(condition, message):
    if not condition:
        raise ValueError(message)

def fields(value, required, optional=frozenset()):
    need(type(value) is dict and required <= value.keys() <= required | optional,
         'Invalid or unknown fields')

def identity(value):
    need(type(value) is str and IDENTITY.fullmatch(value), 'Invalid identity')

def revision(value):
    need(type(value) is int and value > 0, 'Revision must be a positive integer')

def decode(text):
    def pairs(items):
        result = {}
        for key, value in items:
            need(key not in result, 'Duplicate JSON key')
            result[key] = value
        return result
    def constant(_):
        raise ValueError('Nonfinite JSON constant')
    def floating(raw):
        value = float(raw)
        need(math.isfinite(value), 'Nonfinite JSON number')
        return value
    return json.loads(text, object_pairs_hook=pairs, parse_constant=constant, parse_float=floating)

def record_hash(lesson):
    return hashlib.sha256(json.dumps(lesson, ensure_ascii=False, sort_keys=True,
                                    separators=(',', ':'), allow_nan=False).encode('utf-8')).hexdigest()

def projection(lessons):
    """Generate a compact projection; this alone validates or promotes nothing."""
    return [dict(id=lesson['id'], revision=lesson['revision'], record_sha256=record_hash(lesson))
            for lesson in lessons]

def source_path(root, raw):
    need(type(raw) is str and raw and not any(c in raw for c in ('\\', ':', '\x00')),
         'Use a relative POSIX source path')
    parts = raw.split('/')
    need(not PurePosixPath(raw).is_absolute() and all(p not in ('', '.', '..') for p in parts),
         'Source path escapes or is ambiguous')
    candidate = (root / raw).resolve()
    need(candidate.is_relative_to(root) and candidate != root, 'Resolved source escapes root')
    return candidate

def source_check(root, source, max_bytes):
    fields(source, {'path', 'sha256'})
    need(type(source['sha256']) is str and DIGEST.fullmatch(source['sha256']), 'Invalid source digest')
    path = source_path(root, source['path'])
    try:
        if not path.is_file():
            return 'source_unavailable'
        digest = hashlib.sha256()
        with path.open('rb') as stream:
            import os
            before = os.fstat(stream.fileno())
            if before.st_size > max_bytes:
                return 'source_read_budget'
            total = 0
            while block := stream.read(min(65536, max_bytes - total + 1)):
                total += len(block)
                if total > max_bytes:
                    return 'source_read_budget'
                digest.update(block)
            after = os.fstat(stream.fileno())
        current = path.stat()
        handle_signature = lambda s: (s.st_dev, s.st_ino, s.st_size, s.st_mtime_ns, s.st_ctime_ns)
        path_signature = lambda s: (s.st_dev, s.st_ino, s.st_size, s.st_mtime_ns)
        # Windows stat/fstat ctime meanings differ; compare ctime only on the same handle.
        if handle_signature(before) != handle_signature(after) or path_signature(after) != path_signature(current):
            return 'source_changed_during_read'
        if source_path(root, source['path']) != path:
            return 'source_changed_during_read'
        return None if digest.hexdigest() == source['sha256'] else 'source_digest_changed'
    except OSError:
        return 'source_unavailable'

def audit(packet, root, max_source_bytes=16 * 1024 * 1024):
    fields(packet, {'schema', 'lessons'}, {'index'})
    need(packet['schema'] == SCHEMA, 'Unsupported schema')
    need(type(max_source_bytes) is int and max_source_bytes > 0, 'Invalid read budget')
    root = Path(root).resolve()
    need(root.is_dir(), 'Source root unavailable')
    need(type(packet['lessons']) is list, 'Lessons must be a list')
    lessons = {}
    for lesson in packet['lessons']:
        fields(lesson, FIELDS)
        identity(lesson['id']); revision(lesson['revision'])
        need(lesson['id'] not in lessons, 'Duplicate lesson identity')
        need(type(lesson['state']) is str and lesson['state'] in STATES, 'Invalid lesson state')
        for key in FIELDS - {'id', 'revision', 'state', 'requires', 'sources'}:
            need(type(lesson[key]) is str and lesson[key].strip(), 'Missing lesson field: ' + key)
        need(type(lesson['sources']) is list and type(lesson['requires']) is list, 'Invalid lesson collections')
        for dep in lesson['requires']:
            identity(dep)
        need(len(set(lesson['requires'])) == len(lesson['requires']), 'Duplicate required dependency')
        need(lesson['state'] != 'supported' or lesson['sources'] or lesson['requires'],
             'Supported lesson has no declared evidence')
        lessons[lesson['id']] = lesson
    pending, children = {}, collections.defaultdict(list)
    for key, lesson in lessons.items():
        need(all(dep in lessons for dep in lesson['requires']), 'Unknown required dependency')
        pending[key] = len(lesson['requires'])
        for dep in lesson['requires']:
            children[dep].append(key)
    ready = collections.deque(key for key, count in pending.items() if count == 0)
    order = []
    while ready:
        key = ready.popleft(); order.append(key)
        for child in children[key]:
            pending[child] -= 1
            if pending[child] == 0:
                ready.append(child)
    need(len(order) == len(lessons), 'Cyclic required dependency')
    results = {}
    for key in order:
        lesson = lessons[key]
        reasons = []
        for source in lesson['sources']:
            reason = source_check(root, source, max_source_bytes)
            if reason:
                reasons.append(reason + ':' + source['path'])
        for dep in lesson['requires']:
            if results[dep]['binding'] != 'current' or lessons[dep]['state'] != 'supported':
                reasons.append('required:' + dep)
        if lesson['state'] in ('needs_recheck', 'retired'):
            reasons.append('declared:' + lesson['state'])
        results[key] = dict(id=key, revision=lesson['revision'], declared_state=lesson['state'],
                            binding='needs_recheck' if reasons else 'current', reasons=reasons)
    index = {}
    if 'index' in packet:
        need(type(packet['index']) is list, 'Index must be a list')
        for entry in packet['index']:
            fields(entry, {'id', 'revision', 'record_sha256'})
            identity(entry['id']); revision(entry['revision'])
            need(type(entry['record_sha256']) is str and DIGEST.fullmatch(entry['record_sha256']), 'Invalid record digest')
            need(entry['id'] not in index, 'Duplicate index identity')
            index[entry['id']] = entry
    missing = sorted(set(lessons) - set(index)) if 'index' in packet else []
    extra = sorted(set(index) - set(lessons))
    stale = sorted(key for key in set(index) & set(lessons)
                   if index[key]['revision'] != lessons[key]['revision'] or
                   index[key]['record_sha256'] != record_hash(lessons[key]))
    return dict(schema=SCHEMA, index_checked='index' in packet,
                continuity_pass=not (missing or extra or stale) if 'index' in packet else None,
                missing_index=missing, extra_index=extra, stale_index=stale,
                bindings_current=all(item['binding'] == 'current' for item in results.values()),
                lessons=[results[lesson['id']] for lesson in packet['lessons']],
                truth_verified=False, completeness_verified=False,
                limit='Declared records and required dependencies only; current hashes do not prove truth, applicability, authority or absence of undeclared conflicts.')

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('packet', type=Path)
    parser.add_argument('--root', required=True, type=Path, help='Authorized local source directory')
    parser.add_argument('--project', action='store_true', help='Emit validated compact projection to stdout')
    parser.add_argument('--max-source-bytes', type=int, default=16 * 1024 * 1024)
    parser.add_argument('--max-packet-bytes', type=int, default=8 * 1024 * 1024)
    args = parser.parse_args()
    try:
        need(args.max_packet_bytes > 0, 'Invalid packet read budget')
        with args.packet.open('rb') as stream:
            raw = stream.read(args.max_packet_bytes + 1)
        need(len(raw) <= args.max_packet_bytes, 'Packet read budget exceeded')
        packet = decode(raw.decode('utf-8-sig'))
        result = audit(packet, args.root, args.max_source_bytes)
        if args.project:
            print(json.dumps(dict(**result, proposed_index=projection(packet['lessons'])), allow_nan=False))
        else:
            print(json.dumps(result, allow_nan=False))
        return 0 if result['bindings_current'] and result['continuity_pass'] is not False else 1
    except (ValueError, OSError, TypeError, RecursionError) as error:
        print(json.dumps(dict(status='invalid_packet', error=str(error), truth_verified=False)))
        return 2

if __name__ == '__main__':
    sys.exit(main())
