import numpy as np
import math
import seaborn as sns
import matplotlib.pyplot as plt

# Q2a
Hmu = [12,24,36]
Hsigma = [1,1.5]
speed = [16, 33, 19, 31, 27, 21, 15, 31]
likelihoods = np.zeros((3,2))

for i in range(len(Hmu)):
    for j in range(len(Hsigma)):
        mu = round(Hmu[i],2)
        sigma = round(Hsigma[j],2)
        Px = [(1/(sigma*math.sqrt(2*math.pi)))*math.exp(-((x-mu)**2/(2*sigma**2))) for x in speed]
        likelihoods[i,j] = np.prod(Px)

jPDFa = likelihoods/likelihoods.sum() # uniform priors
plt.axes(title='Joint Posterior PDF (2a)')
sns.heatmap(jPDFa,xticklabels=Hsigma,yticklabels=Hmu)

# Q2b
logLikelihoods = np.zeros((3,2))
normLikelihoods = np.zeros((3,2))

for i in range(len(Hmu)):
    for j in range(len(Hsigma)):
        mu = round(Hmu[i],2)
        sigma = round(Hsigma[j],2)
        logLikelihoods[i,j] = 8*(math.log(1/(sigma*math.sqrt(2*math.pi))))-(1/(2*sigma**2))*sum([(x-mu)**2 for x in speed])

for i in range(len(Hmu)):
    for j in range(len(Hsigma)):
        normLikelihoods[i,j] = math.exp(logLikelihoods[i,j]-logLikelihoods.max())

jPDFb = normLikelihoods/normLikelihoods.sum() # uniform priors
plt.axes(title='Joint Posterior PDF (2b)')
sns.heatmap(jPDFb,xticklabels=Hsigma,yticklabels=Hmu)