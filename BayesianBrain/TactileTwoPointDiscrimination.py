import numpy as np
import math

n1 = [3,18,4]
n2 = [5,3,5]
n3 = [7,20,8]

def rate1(xh):
    return 20*math.exp(-((6-xh)**2+(2-2)**2)/2)

rateM1 = [rate1(4), rate1(6), rate1(8)]

def rate2(x1,x2,xh):
    return 10*math.exp(-((x1-xh)**2+(2-2)**2)/2) + 10*math.exp(-((x2-xh)**2+(2-2)**2)/2)

rateM2a = [rate2(5,7,4), rate2(5,7,6), rate2(5,7,8)]
rateM2b = [rate2(4,8,4), rate2(4,8,6), rate2(4,8,8)]
rateM2c = [rate2(3,9,4), rate2(3,9,6), rate2(3,9,8)]

def like(r,n):
    return np.prod([(math.exp(-r[i])*(r[i]**n[i]))/math.factorial(n[i]) for i in range(3)])

likeM1 = [like(rateM1,n1),like(rateM1,n2),like(rateM1,n3)]
likeM2 = [np.mean([like(rateM2a,n1),like(rateM2b,n1),like(rateM2c,n1)]),np.mean([like(rateM2a,n2),like(rateM2b,n2),like(rateM2c,n2)]),np.mean([like(rateM2a,n3),like(rateM2b,n3),like(rateM2c,n3)])]

postM1 = [M1/(M1+M2) for M1,M2 in zip(likeM1,likeM2)]
postM2 = [M2/(M1+M2) for M1,M2 in zip(likeM1,likeM2)]

BF = [M1/M2 for M1,M2 in zip(postM1,postM2)]

threec = [like(rateM2a,n3),like(rateM2b,n3),like(rateM2c,n3)]