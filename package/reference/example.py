"""Source-free runnable example: known arithmetic, not a physical benchmark."""
import json,math
from rel_localization.runner import predict,evaluate,SEMANTICS
def fixture():
    landmarks={'6':[4.,1.],'7':[1.,4.]};duration=8.;od=[[t,.12,.025] for t in range(9)]
    def pose(t):return [.12/.025*math.sin(.025*t),.12/.025*(1-math.cos(.025*t)),.025*t]
    observations=[]
    for i in range(1,16):
        t=i*.5;k='6' if i%2 else '7';x,y,th=pose(t);dx=landmarks[k][0]-x;dy=landmarks[k][1]-y
        observations.append([t,int(k),math.hypot(dx,dy)+(.45 if i==8 else .015*(-1)**i),math.atan2(dy,dx)-th])
    packet={'schema':'planar-range-bearing-v1','semantics':SEMANTICS.copy(),'duration':duration,'initial':[0.,0.,0.],'odometry':od,'observations':observations,'landmarks':landmarks}
    reference=[[i*.1,*pose(i*.1)] for i in range(81)]
    return packet,reference
if __name__=='__main__':
    packet,reference=fixture();result=predict(packet);print(json.dumps({'scope':'Synthetic engineering illustration only','metrics':evaluate(result['poses'],reference),'counts':result['counts'],'whole_prediction_wall_seconds':result['whole_prediction_wall_seconds']},indent=2))
