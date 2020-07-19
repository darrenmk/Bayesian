import numpy as np
import math

playerA = [42,38,44,43,44]
playerB = [45,43,42,43,46]

Hmu = np.arange(30,51,1)
Hsigma = np.arange(1,10.45,0.45)
likeA = np.zeros((21,21))
likeB = np.zeros((21,21))

# first we must generate a posterior PDF for A and B
for i in range(len(Hmu)):
    for j in range(len(Hsigma)):
        mu = round(Hmu[i],2)
        sigma = round(Hsigma[j],2)
        likeA[i,j] = np.prod([(1/(sigma*math.sqrt(2*math.pi)))*math.exp(-((x-mu)**2/(2*sigma**2))) for x in playerA])
        likeB[i,j] = np.prod([(1/(sigma*math.sqrt(2*math.pi)))*math.exp(-((x-mu)**2/(2*sigma**2))) for x in playerB])

jPDFa = likeA/likeA.sum()
muPDFa = np.sum(jPDFa,axis=1)

jPDFb = likeB/likeB.sum()
muPDFb = np.sum(jPDFb,axis=1)

# now we calculate P(A<B|D)
postBgreater = sum([muPDFa[a]*sum(muPDFb[a+1:]) for a in range(len(Hmu)-1)])
postAgreater = sum([muPDFb[a]*sum(muPDFa[a+1:]) for a in range(len(Hmu)-1)])
postEqual = sum([muPDFa[a]*muPDFb[a] for a in range(len(Hmu))])

#Q1b
mu1 = 46.5-43.5
mu2 = 43.5-46.5
sigma = math.sqrt((2**2)+(2.5**2))
x = 2.7

like1 = (1/(sigma*math.sqrt(2*math.pi)))*math.exp(-((x-mu1)**2/(2*sigma**2)))
like2 = (1/(sigma*math.sqrt(2*math.pi)))*math.exp(-((x-mu2)**2/(2*sigma**2)))

post1 = like1/(like1+like2)
post2 = like2/(like1+like2)