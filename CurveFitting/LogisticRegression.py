import matplotlib.pyplot as plt
import numpy as np
import math

# Q1a
Ha = np.arange(4,14.5,0.5)
Hb = np.arange(0.1,1.15,0.05)
dose = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 1.0, 1.5, 2.0]
h = [0,0,1,2,4,6,8,9,9,10,10]
n = 10
L = np.zeros((21,21))

for i in range(len(Ha)):
    for j in range(len(Hb)):
        a = round(Ha[i],2)
        b = round(Hb[j],2)
        p = [1/(1+math.exp(a*(b-x))) for x in dose]
        P = [(p[k]**h[k])*((1-p[k])**(n-h[k])) for k in range(len(p))]
        L[i,j] = np.prod(P)

jointPostPDFa = L/L.sum() # uniform priors

i,j = np.where(jointPostPDFa==jointPostPDFa.max())
MAPa = [round(Ha[i[0]],2),round(Hb[j[0]],3),round(jointPostPDFa.max(),6)]

plt.axes(title='Joint Posterior PDF (1a)',xlabel='H(a)',ylabel='H(b)',xticks=np.arange(0,len(Ha),2),yticks=np.arange(0,len(Hb),2),xticklabels=Ha[0::2]-0.25,yticklabels=(Hb[0::2]-0.025).round(3))
plt.pcolormesh(np.transpose(jointPostPDFa))

a = 7.5
b = 0.55
x = np.linspace(0, 2, 100)
curve = [1/(1+math.exp(a*(b-val))) for val in x]
doseRange = np.arange(0,2,2/100)

plt.figure()
plt.axes(title='Best fit curve (1a)',xlabel='Dose (x, mg/l)',ylabel='P(success)')
plt.plot(dose,np.divide(h,n),'.')
plt.plot(doseRange,curve)


# Q1b
Ha = np.arange(4,14.5,0.5)
Hb = np.arange(0.1,1.15,0.05)
dose = [0.1, 0.3, 0.5, 0.7, 1.0, 2.0]
h = [0,1,4,8,9,10]
n = 10
L = np.zeros((21,21))

for i in range(len(Ha)):
    for j in range(len(Hb)):
        a = round(Ha[i],2)
        b = round(Hb[j],2)
        p = [1/(1+math.exp(a*(b-x))) for x in dose]
        P = [(p[k]**h[k])*((1-p[k])**(n-h[k])) for k in range(len(p))]
        L[i,j] = np.prod(P)

jointPostPDFb = L/L.sum() # uniform priors

i,j = np.where(jointPostPDFb==jointPostPDFb.max())
MAPb = [round(Ha[i[0]],2),round(Hb[j[0]],3),round(jointPostPDFb.max(),6)]

plt.axes(title='Joint Posterior PDF (1b)',xlabel='H(a)',ylabel='H(b)',xticks=np.arange(0,len(Ha),2),yticks=np.arange(0,len(Hb),2),xticklabels=Ha[0::2]-0.25,yticklabels=(Hb[0::2]-0.025).round(3))
plt.pcolormesh(np.transpose(jointPostPDFb))

a = 7.5
b = 0.55
x = np.linspace(0, 2, 100)
curve = [1/(1+math.exp(a*(b-val))) for val in x]
doseRange = np.arange(0,2,2/100)

plt.figure()
plt.axes(title='Best fit curve (1b)',xlabel='Dose (x, mg/l)',ylabel='P(success)')
plt.plot(dose,np.divide(h,n),'.')
plt.plot(doseRange,curve)