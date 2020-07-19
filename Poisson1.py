import matplotlib.pyplot as plt
import numpy as np
import math

# Q3a
Hlambda = [x for x in range(1,16)]
L = [0]*15
k = 5
i = 0

for myLambda in Hlambda:
    L[i] = ((math.e**-myLambda)*(myLambda**k))/math.factorial(k)
    i += 1

postPDFa = [l/sum(L) for l in L] # uniform priors
MAPa = [Hlambda[postPDFa.index(max(postPDFa))],max(postPDFa)]

plt.axes(title='Posterior PDF (3a)',xlabel='H(lambda)',ylabel='Posterior Probability')
plt.plot(Hlambda,postPDFa)
sorted_a = sorted(postPDFa,reverse=True)
x = 0
idx = [None]*15
i = 0

while x < 0.949:
    x = x + sorted_a[i]
    idx[i] = postPDFa.index(sorted_a[i])
    i += 1

idx = [x for x in idx if x is not None]
range_a = [Hlambda[min(idx)], Hlambda[max(idx)]] # this is the 95% confidence interval

# Q3b
Lb = np.zeros((15,5))
for k in range(0,5):
    i = 0
    for myLambda in Hlambda:
        Lb[i,k] = ((math.e**-myLambda)*(myLambda**k))/math.factorial(k)
        i += 1

Lb_sum = np.sum(Lb,axis=1)
pLessThan5 = sum(Lb_sum * postPDFa)

# Q3c i
Li = [0]*15
k = 7
i = 0
priorPDFi = postPDFa

for myLambda in Hlambda:
    Li[i] = ((math.e**-myLambda)*(myLambda**k))/math.factorial(k)
    i += 1

myProduct = [a*b for a,b in zip(priorPDFi,Li)] # multiply posterior PDF (new priors) by likelihoods
postPDFi = [x/sum(myProduct) for x in myProduct]
MAPi = [Hlambda[postPDFi.index(max(postPDFi))],max(postPDFi)]

plt.axes(title='Posterior PDF (3c)',xlabel='H(Lambda)',ylabel='Posterior Probability')
plt.plot(Hlambda,postPDFi)

# Q3c ii
Lii = [0]*15
k = [5,7]
i = 0

for myLambda in Hlambda:
    Lii[i] = ((math.e**-myLambda)*(myLambda**k[0]))/math.factorial(k[0]) * ((math.e**-myLambda)*(myLambda**k[1]))/math.factorial(k[1])
    i += 1

postPDFii = [l/sum(Lii) for l in Lii] # uniform priors
MAPii = [Hlambda[postPDFii.index(max(postPDFii))],max(postPDFii)]

plt.plot(Hlambda,postPDFii)

# Q3c iii
Liii = [0]*15
k = 6
i = 0

for myLambda in Hlambda:
    Liii[i] = (((math.e**-myLambda)*(myLambda**k))/math.factorial(k))**2
    i += 1

postPDFiii = [l/sum(Liii) for l in Liii] # uniform priors
MAPiii = [Hlambda[postPDFiii.index(max(postPDFiii))],max(postPDFiii)]

plt.plot(Hlambda,postPDFiii)