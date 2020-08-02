import matplotlib.pyplot as plt
import numpy as np
import math

H_mu = np.arange(160,265,5)
H_sigma = np.arange(10,45,5)
L = np.zeros((21,7))
weights = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Li = [0]*len(weights)

i = 0
for mu in H_mu:
    j = 0
    for sigma in H_sigma:
        z = 0
        for x in weights:
            Li[z] = (1/sigma*math.sqrt(2*math.pi))*math.exp(-((x-mu)**2/(2*sigma**2)))
            z += 1
        L[i,j] = np.prod(Li)
        j += 1
    i += 1

postPDF = [l/sum(sum(L)) for l in L] # uniform priors

postPDFm = [0]*21
for x in range(0,21):
    postPDFm[x] = sum(postPDF[x])

MAP = [H_mu[postPDFm.index(max(postPDFm))],max(postPDFm)]

plt.axes(title='Posterior PDF (5)',xlabel='H(mu)',ylabel='Posterior Probability')
plt.plot(H_mu,postPDFm)

sort = sorted(postPDFm,reverse=True)
x = 0
idx = [None]*21
i = 0

while x < 0.95:
    x = x + sort[i]
    idx[i] = postPDFm.index(sort[i])
    i += 1

idx = [x for x in idx if x is not None]
ranges = [H_mu[min(idx)], H_mu[max(idx)]] # this is the 95% confidence interval

h = 0
healthy = 0
borderline = 0
unhealthy = 0

for val in postPDFm:
    if H_mu[h] <= 182.5:
        healthy += postPDFm[h]
    elif 182.5 < H_mu[h] <= 202.5:
        borderline += postPDFm[h]
    elif H_mu[h] > 202.5:
        unhealthy += postPDFm[h]
    h += 1
