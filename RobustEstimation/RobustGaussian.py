import matplotlib.pyplot as plt
import numpy as np
import math

# Q3a
Hmu = np.arange(30,50.1,1)
Hsigma = np.arange(1,10.1,0.45)
s = [42,38,44,43,44]
La = np.zeros((21,21))

for i in range(len(Hmu)):
    for j in range(len(Hsigma)):
        mu = round(Hmu[i],2)
        sigma = round(Hsigma[j],2)
        Px = [(1/sigma*math.sqrt(2*math.pi))*math.exp(-((x-mu)**2/(2*sigma**2))) for x in s]
        La[i,j] = np.prod(Px)

jPDFa = La/La.sum() # uniform priors
plt.axes(title='Joint Posterior PDF (3a)',xlabel='H(mu)',ylabel='H(sigma)',xticks=np.arange(0,len(Hmu),2),yticks=np.arange(0,len(Hsigma),2),xticklabels=Hmu[0::2]-0.50,yticklabels=(Hsigma[0::2]-0.0225).round(4))
plt.pcolormesh(np.transpose(jPDFa))

muPDFa = [sum(jPDFa[z,:]) for z in range(len(Hmu))]
plt.axes(title='Posterior PDF (3a)',xlabel='H(mu)',ylabel='Posterior Probability')
plt.plot(Hmu,muPDFa)

modea = [Hmu[muPDFa.index(max(muPDFa))],max(muPDFa)]



# Q3b
s2 = [42,38,44,43,44,30]
Lb = np.zeros((21,21))

for i in range(len(Hmu)):
    for j in range(len(Hsigma)):
        mu = round(Hmu[i],2)
        sigma = round(Hsigma[j],2)
        Px = [(1/sigma*math.sqrt(2*math.pi))*math.exp(-((x-mu)**2/(2*sigma**2))) for x in s2]
        Lb[i,j] = np.prod(Px)

jPDFb = Lb/Lb.sum() # uniform priors
plt.axes(title='Joint Posterior PDF (3b)',xlabel='H(mu)',ylabel='H(sigma)',xticks=np.arange(0,len(Hmu),2),yticks=np.arange(0,len(Hsigma),2),xticklabels=Hmu[0::2]-0.50,yticklabels=(Hsigma[0::2]-0.0225).round(4))
plt.pcolormesh(np.transpose(jPDFb))

muPDFb = [sum(jPDFb[z,:]) for z in range(len(Hmu))]
plt.axes(title='Posterior PDF (3b)',xlabel='H(mu)',ylabel='Posterior Probability')
plt.plot(Hmu,muPDFb)

modeb = [Hmu[muPDFb.index(max(muPDFb))],max(muPDFb)]



# Q3c
Lc = np.zeros((21,21))

for i in range(len(Hmu)):
    for j in range(len(Hsigma)):
        mu = round(Hmu[i],2)
        sigma = round(Hsigma[j],2)
        Px = [0.1 + 0.9*(1/sigma*math.sqrt(2*math.pi))*math.exp(-((x-mu)**2/(2*sigma**2))) for x in s2]
        Lc[i,j] = np.prod(Px)

jPDFc = Lc/Lc.sum() # uniform priors
plt.axes(title='Joint Posterior PDF (3c)',xlabel='H(mu)',ylabel='H(sigma)',xticks=np.arange(0,len(Hmu),2),yticks=np.arange(0,len(Hsigma),2),xticklabels=Hmu[0::2]-0.50,yticklabels=(Hsigma[0::2]-0.0225).round(4))
plt.pcolormesh(np.transpose(jPDFc))

muPDFc = [sum(jPDFc[z,:]) for z in range(len(Hmu))]
plt.axes(title='Posterior PDF (3c)',xlabel='H(mu)',ylabel='Posterior Probability')
plt.plot(Hmu,muPDFc)

modec = [Hmu[muPDFc.index(max(muPDFc))],max(muPDFc)]

