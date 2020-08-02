import matplotlib.pyplot as plt
import numpy as np
import math

#Q3
Hpi = np.arange(3,3.301,0.0075)
Hsigma = np.arange(1,6)
data = [29/10,62/20,96/30,123/40,159/50]
d = [10,20,30,40,50]
L = np.zeros((41,5))

for i in range(len(Hpi)):
    for j in range(len(Hsigma)):
        pi = round(Hpi[i],2)
        sigma = round(Hsigma[j],2)
        circum = [a*b for a,b in zip(data,d)]
        P = [(1/sigma*math.sqrt(2*math.pi))*math.exp(-(((circum[w]-pi*d[w])**2)/(2*sigma**2))) for w in range(len(circum))]
        L[i,j] = np.prod(P)

jointPostPDF = L/L.sum() # uniform priors
postPDFoverPi = list(np.sum(jointPostPDF,axis=1)) # sum rows = margianlize over A

MAP = [Hpi[postPDFoverPi.index(max(postPDFoverPi))],max(postPDFoverPi)]

plt.axes(title='Posterior PDF (3)',xlabel='H(pi)',ylabel='Posterior Probability')
plt.plot(Hpi,postPDFoverPi)
sort = sorted(postPDFoverPi,reverse=True)
x = 0
idx = [None]*len(Hpi)
i = 0

while x < 0.95:
    x = x + sort[i]
    idx[i] = postPDFoverPi.index(sort[i])
    i += 1

idx = [x for x in idx if x is not None]
rangePi = [Hpi[min(idx)], Hpi[max(idx)]] # this is the 95% confidence interval for G
