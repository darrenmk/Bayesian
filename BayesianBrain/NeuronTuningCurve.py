import numpy as np
import math

Htheta = np.arange(1,181)
L = np.zeros((180))
thetaHat = [80,90,100]
n = [41,34,16]

# Q1b
for k in range(len(Htheta)):
    rate = [50*math.exp((-(Htheta[k]-thetaHat[t])**2)/(2*(20**2))) for t in range(len(thetaHat))]
    L[k] = np.prod([(math.exp(-rate)*(rate**n))/math.factorial(n) for rate,n in zip(rate,n)])

postPDF = L/L.sum()
mode = Htheta[np.where(postPDF == np.max(postPDF))]

sort = sorted(postPDF,reverse=True)
x = 0
idx = [None]*len(Htheta)
i = 0

while x < 0.95:
    x = x + sort[i]
    idx[i] = Htheta[np.where(postPDF==sort[i])]
    i += 1

idx = [x for x in idx if x is not None]
confidenceInterval = [min(idx),max(idx)]

# Q1c: because the actual number of spikes were drawn from a Poisson distribution where r is the rate
