import matplotlib.pyplot as plt
import numpy as np
import math

Hlambda = [x/5 for x in range(5,105)]
L = np.zeros((100,4))
patrons = [12,10,14,11]
i = 0

for myLambda in Hlambda:
    j = 0
    for k in patrons:
        L[i,j] = ((math.e**-myLambda)*(myLambda**k))/math.factorial(k)
        j += 1
    i += 1

multiL = L[:,0]*L[:,1]*L[:,2]*L[:,3]

postPDF = [l/sum(multiL) for l in multiL] # uniform priors
MAP = [Hlambda[postPDF.index(max(postPDF))],max(postPDF)]

plt.axes(title='Posterior PDF (4)',xlabel='H(lambda)',ylabel='Posterior Probability')
plt.plot(Hlambda,postPDF)
x = 0
i = 0

while x < 0.7469:
    x = x + postPDF[i]
    i += 1

nFish = Hlambda[i-1]