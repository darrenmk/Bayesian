import matplotlib.pyplot as plt
import numpy as np
import math

#Q4a
Hpi = np.arange(3,3.201,0.005)
Hsigma = np.arange(1,7.1,0.4)
diameter = [10,20,30,40,50,60]
circumference = [34,61,95,124,148,190]
estimate = [i/j for i,j in zip(circumference,diameter)]
La = np.zeros((41,16))

for i in range(len(Hpi)):
    for j in range(len(Hsigma)):
        pi = round(Hpi[i],2)
        sigma = round(Hsigma[j],2)
        Px = [(1/sigma*math.sqrt(2*math.pi))*math.exp(-(((circumference[x]-pi*diameter[x])**2)/(2*sigma**2))) for x in range(len(circumference))]
        La[i,j] = np.prod(Px)

jPDFa = La/La.sum() # uniform priors

plt.axes(title='Joint Posterior PDF (4a)',xlabel='H(pi)',ylabel='H(sigma)',xticks=np.arange(0,len(Hpi),5),yticks=np.arange(0,len(Hsigma),5),xticklabels=(Hpi[0::5]).round(4),yticklabels=(Hsigma[0::5]).round(4))
plt.pcolormesh(np.transpose(jPDFa))

i,j = np.where(jPDFa==jPDFa.max())
modea = [round(Hpi[i[0]],2),round(Hsigma[j[0]],3),round(jPDFa.max(),6)]



#Q4b
Lb = np.zeros((41,16))

for i in range(len(Hpi)):
    for j in range(len(Hsigma)):
        pi = round(Hpi[i],2)
        sigma = round(Hsigma[j],2)
        Px = [(0.1*(1/15*math.sqrt(2*math.pi))*math.exp(-(((circumference[x]-pi*diameter[x])**2)/(2*15**2))) + 0.9*(1/sigma*math.sqrt(2*math.pi))*math.exp(-(((circumference[x]-pi*diameter[x])**2)/(2*sigma**2)))) for x in range(len(circumference))]
        Lb[i,j] = np.prod(Px)

jPDFb = Lb/Lb.sum() # uniform priors

plt.axes(title='Joint Posterior PDF (4b)',xlabel='H(pi)',ylabel='H(sigma)',xticks=np.arange(0,len(Hpi),5),yticks=np.arange(0,len(Hsigma),2),xticklabels=(Hpi[0::5]).round(4),yticklabels=(Hsigma[0::2]).round(4))
plt.pcolormesh(np.transpose(jPDFb))

i,j = np.where(jPDFb==jPDFb.max())
modeb = [round(Hpi[i[0]],2),round(Hsigma[j[0]],3),round(jPDFb.max(),6)]

