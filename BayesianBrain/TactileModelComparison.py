import numpy as np
import math

xhat = [8,8,8,10,10,10,12,12,12]
yhat = [8,10,12,8,10,12,8,10,12]

trial1 = [9,20,21,24,21,45,12,23,21]
trial2 = [23,23,20,23,38,19,16,16,12]
trial3 = [21,18,16,19,25,21,19,22,2]
trial4 = [28,30,22,34,12,8,15,14,8]

def rate(x,y,xh,yh):
    return 10*math.exp(-((x-xh)**2+(y-yh)**2)/8)

rateA = [rate(8.5,8,xh,yh)+rate(11.5,8,xh,yh)+rate(9.25,10,xh,yh)+rate(10.75,10,xh,yh)+rate(10,12,xh,yh) for xh,yh in zip(xhat,yhat)]
rateV = [rate(10,8,xh,yh)+rate(9.25,10,xh,yh)+rate(10.75,10,xh,yh)+rate(8.5,12,xh,yh)+rate(11.5,12,xh,yh) for xh,yh in zip(xhat,yhat)]
rateL = [rate(8,12,xh,yh)+rate(8,10,xh,yh)+rate(8,8,xh,yh)+rate(10,8,xh,yh)+rate(12,8,xh,yh) for xh,yh in zip(xhat,yhat)]
rateT = [rate(8,12,xh,yh)+rate(10,12,xh,yh)+rate(12,12,xh,yh)+rate(10,10,xh,yh)+rate(10,8,xh,yh) for xh,yh in zip(xhat,yhat)]
rateX = [rate(8,12,xh,yh)+rate(12,12,xh,yh)+rate(10,10,xh,yh)+rate(8,8,xh,yh)+rate(12,8,xh,yh) for xh,yh in zip(xhat,yhat)]

def like(rate,trial):
    return np.prod([(math.exp(-rate[i])*(rate[i]**trial[i]))/math.factorial(trial[i]) for i in range(9)])

L1 = [like(rateA,trial1),like(rateV,trial1),like(rateL,trial1),like(rateT,trial1),like(rateX,trial1)]
post1 = L1/sum(L1)

L2 = [like(rateA,trial2),like(rateV,trial2),like(rateL,trial2),like(rateT,trial2),like(rateX,trial2)]
post2 = L2/sum(L2)

L3 = [like(rateA,trial3),like(rateV,trial3),like(rateL,trial3),like(rateT,trial3),like(rateX,trial3)]
post3 = L3/sum(L3)

L4 = [like(rateA,trial4),like(rateV,trial4),like(rateL,trial4),like(rateT,trial4),like(rateX,trial4)]
post4 = L4/sum(L4)