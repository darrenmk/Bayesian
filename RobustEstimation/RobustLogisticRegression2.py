import matplotlib.pyplot as plt
import numpy as np
import math

# Q1a
Ha = np.arange(4,14.1,0.1)
Hb = np.arange(0.1,1.11,0.01)
dose = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 1.0, 1.5, 2.0, 2.5]
h = [0,0,1,2,4,6,8,9,9,10,10,9]
n = 10
La = np.zeros((101,101))

for i in range(len(Ha)):
    for j in range(len(Hb)):
        a = round(Ha[i],2)
        b = round(Hb[j],2)
        p = [1/(1+math.exp(a*(b-x))) for x in dose]
        P = [(p[k]**h[k])*((1-p[k])**(n-h[k])) for k in range(len(p))]
        La[i,j] = np.prod(P)

jPDFa = La/La.sum() # uniform priors

i,j = np.where(jPDFa==jPDFa.max())
modea = [round(Ha[i[0]],2),round(Hb[j[0]],3),round(jPDFa.max(),6)]

plt.axes(title='Joint Posterior PDF (2a)',xlabel='H(a)',ylabel='H(b)',xticks=np.arange(0,len(Ha),10),yticks=np.arange(0,len(Hb),10),xticklabels=(Ha[0::10]).round(3),yticklabels=(Hb[0::10]).round(3))
plt.pcolormesh(np.transpose(jPDFa))

a = modea[0]
b = modea[1]
linspacea = np.linspace(0, 2.5, 100)
curvea = [1/(1+math.exp(a*(b-x))) for x in linspacea]
doseRangea = np.arange(0,2.5,2.5/100)

plt.figure()
plt.axes(title='Best Fit Curve (2a)',xlabel='Dose (x, mg/l)',ylabel='P(success)')
plt.plot(dose,np.divide(h,n),'.')
plt.plot(doseRangea,curvea)




# Q1b
Lb = np.zeros((101,101))

for i in range(len(Ha)):
    for j in range(len(Hb)):
        a = round(Ha[i],2)
        b = round(Hb[j],2)
        p = [0.1 + 0.99*(1/(1+math.exp(a*(b-x)))) for x in dose]
        P = [(p[k]**h[k])*((1-p[k])**(n-h[k])) for k in range(len(p))]
        Lb[i,j] = np.prod(P)

jPDFb = Lb/Lb.sum() # uniform priors

i,j = np.where(jPDFb==jPDFb.max())
modeb = [round(Ha[i[0]],2),round(Hb[j[0]],3),round(jPDFb.max(),6)]

plt.axes(title='Joint Posterior PDF (2b)',xlabel='H(a)',ylabel='H(b)',xticks=np.arange(0,len(Ha),10),yticks=np.arange(0,len(Hb),10),xticklabels=(Ha[0::10]).round(3),yticklabels=(Hb[0::10]).round(3))
plt.pcolormesh(np.transpose(jPDFb))

a = modeb[0]
b = modeb[1]
linspaceb = np.linspace(0, 2.5, 100)
curveb = [1/(1+math.exp(a*(b-x))) for x in linspaceb]
doseRangeb = np.arange(0,2.5,2.5/100)

plt.figure()
plt.axes(title='Best Fit Curve (2b)',xlabel='Dose (x, mg/l)',ylabel='P(success)')
plt.plot(dose,np.divide(h,n),'.')
plt.plot(doseRangeb,curveb)