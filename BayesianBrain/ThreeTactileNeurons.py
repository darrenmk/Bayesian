import numpy as np
import math

sigma = 1 # this is the receptive field, larger means the neuron is receptive to stimuli that are farther away

def rate1(xh):
    return 20*math.exp(-((6-xh)**2+(2-2)**2)/(2*(sigma**2)))

rateM1 = [rate1(4), rate1(6), rate1(8)]

def rate2(x1,x2,xh):
    return 10*math.exp(-((x1-xh)**2+(2-2)**2)/(2*(sigma**2))) + 10*math.exp(-((x2-xh)**2+(2-2)**2)/(2*(sigma**2)))

rateM2a = [rate2(5,7,4), rate2(5,7,6), rate2(5,7,8)]
rateM2b = [rate2(4,8,4), rate2(4,8,6), rate2(4,8,8)]
rateM2c = [rate2(3,9,4), rate2(3,9,6), rate2(3,9,8)]

sampleA = np.random.poisson(lam=tuple(rateM2a), size=(100, 3)) # number of trials for config A
sampleB = np.random.poisson(lam=tuple(rateM2b), size=(100, 3)) # number of trials for config B
sampleC = np.random.poisson(lam=tuple(rateM2c), size=(100, 3)) # number of trials for config C

def like(r,n):
    return np.prod([(math.exp(-r[i])*(r[i]**n[i]))/math.factorial(n[i]) for i in range(3)])

# config A
likeM1a = [like(rateM1,sampleA[i]) for i in range(100)]
likeM2a = [like(rateM2a,sampleA[i]) for i in range(100)]

postM1a = [M1/(M1+M2) for M1,M2 in zip(likeM1a,likeM2a)]
postM2a = [M2/(M1+M2) for M1,M2 in zip(likeM1a,likeM2a)]

BFa = [M2/M1 for M1,M2 in zip(postM1a,postM2a)]
pCorrectA = len([i for i in BFa if i > 1]) / len(BFa)

# config B
likeM1b = [like(rateM1,sampleB[i]) for i in range(100)]
likeM2b = [like(rateM2b,sampleB[i]) for i in range(100)]

postM1b = [M1/(M1+M2) for M1,M2 in zip(likeM1b,likeM2b)]
postM2b = [M2/(M1+M2) for M1,M2 in zip(likeM1b,likeM2b)]

BFb = [M2/M1 for M1,M2 in zip(postM1b,postM2b)]
pCorrectB = len([i for i in BFb if i > 1]) / len(BFb)

## config C
likeM1c = [like(rateM1,sampleC[i]) for i in range(100)]
likeM2c = [like(rateM2c,sampleC[i]) for i in range(100)]

postM1c = [M1/(M1+M2) for M1,M2 in zip(likeM1c,likeM2c)]
postM2c = [M2/(M1+M2) for M1,M2 in zip(likeM1c,likeM2c)]

BFc = [M2/M1 for M1,M2 in zip(postM1c,postM2c)]
pCorrectC = len([i for i in BFc if i > 1]) / len(BFc)

