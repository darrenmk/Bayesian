import matplotlib.pyplot as plt
import numpy as np
import math

# Q2
HA = np.arange(5,15.5,0.5)
HG = np.arange(1000,7001,300)
gain = [0,500,1000,2000,3000]
goals = [10,11,14,20,28]
L = np.zeros((21,21))

for i in range(len(HA)):
    for j in range(len(HG)):
        A = round(HA[i],2)
        G = round(HG[j],2)
        lambdas = [A*(2**(g/G)) for g in gain]
        P = [((math.e**-lambdas[x])*(lambdas[x]**goals[x]))/math.factorial(goals[x]) for x in range(len(lambdas))]
        L[i,j] = np.prod(P)

jointPostPDF = L/L.sum() # uniform priors
postPDFoverG = list(np.sum(jointPostPDF,axis=0)) # sum rows = margianlize over A

MAP = [HG[postPDFoverG.index(max(postPDFoverG))],max(postPDFoverG)]

plt.axes(title='Posterior PDF (2)',xlabel='H(G)',ylabel='Posterior Probability')
plt.plot(HG,postPDFoverG)
sort = sorted(postPDFoverG,reverse=True)
x = 0
idx = [None]*len(HG)
i = 0

while x < 0.95:
    x = x + sort[i]
    idx[i] = postPDFoverG.index(sort[i])
    i += 1

idx = [x for x in idx if x is not None]
rangeG = [HG[min(idx)], HG[max(idx)]] # this is the 95% confidence interval for G