import matplotlib.pyplot as plt
import numpy as np
import math

# Q1a
Ha = np.arange(0.03,3.0,0.03)
Hb = np.arange(5,15.1,0.1)

amp = [2,8,10,14,18]
sData = [[5,6,8,10,10],[6,6,8,10,10],[5,6,8,10,9]]
n = 10
L = np.zeros((100,101,3))

for i in range(len(Ha)):
    for j in range(len(Hb)):
        for s in range(len(sData)):
            a = round(Ha[i],2)
            b = round(Hb[j],2)
            p = [0.5*(1+(1/(1+math.exp(a*(b-x))))) for x in amp]
            P = [(p[k]**sData[s][k])*((1-p[k])**(n-sData[s][k])) for k in range(len(p))]
            L[i,j,s] = np.prod(P)

jointPostPDF1 = L[:,:,0]/L[:,:,0].sum() # uniform priors
jointPostPDF2 = L[:,:,1]/L[:,:,1].sum() # uniform priors
jointPostPDF3 = L[:,:,2]/L[:,:,2].sum() # uniform priors


i,j = np.where(jointPostPDF1==jointPostPDF1.max())
mode1 = [round(Ha[i[0]],2),round(Hb[j[0]],3),round(jointPostPDF1.max(),6)]

a = 1.11
b = 9.5
x = np.linspace(2, 18, 160)
curve = [0.5*(1+(1/(1+math.exp(a*(b-val))))) for val in x]
ampRange = np.arange(2,18,16/160)

plt.figure()
plt.axes(title='Best Fit Curve (Participant 1)',xlabel='Amplitude (micrometers)',ylabel='P(success)')
plt.plot(amp,np.divide(sData[0],n),'.')
plt.plot(ampRange,curve)


i,j = np.where(jointPostPDF2==jointPostPDF2.max())
mode2 = [round(Ha[i[0]],2),round(Hb[j[0]],3),round(jointPostPDF2.max(),6)]

a = 1.11
b = 9.5
x = np.linspace(2, 18, 160)
curve = [0.5*(1+(1/(1+math.exp(a*(b-val))))) for val in x]
ampRange = np.arange(2,18,16/160)

plt.figure()
plt.axes(title='Best Fit Curve (Participant 2)',xlabel='Amplitude (micrometers)',ylabel='P(success)')
plt.plot(amp,np.divide(sData[1],n),'.')
plt.plot(ampRange,curve)





i,j = np.where(jointPostPDF3==jointPostPDF3.max())
mode3 = [round(Ha[i[0]],2),round(Hb[j[0]],3),round(jointPostPDF3.max(),6)]

a = 0.3
b = 9.6
x = np.linspace(2, 18, 160)
curve = [0.5*(1+(1/(1+math.exp(a*(b-val))))) for val in x]
ampRange = np.arange(2,18,16/160)

plt.figure()
plt.axes(title='Best Fit Curve (Participant 3)',xlabel='Amplitude (micrometers)',ylabel='P(success)')
plt.plot(amp,np.divide(sData[2],n),'.')
plt.plot(ampRange,curve)






# Q1b

for i in range(len(Ha)):
    for j in range(len(Hb)):
        for s in range(len(sData)):
            a = round(Ha[i],2)
            b = round(Hb[j],2)
            p = [0.01 + 0.49*(1+(1/(1+math.exp(a*(b-x))))) for x in amp]
            P = [(p[k]**sData[s][k])*((1-p[k])**(n-sData[s][k])) for k in range(len(p))]
            L[i,j,s] = np.prod(P)

jointPostPDF1 = L[:,:,0]/L[:,:,0].sum() # uniform priors
jointPostPDF2 = L[:,:,1]/L[:,:,1].sum() # uniform priors
jointPostPDF3 = L[:,:,2]/L[:,:,2].sum() # uniform priors


i,j = np.where(jointPostPDF1==jointPostPDF1.max())
MAP1 = [round(Ha[i[0]],2),round(Hb[j[0]],3),round(jointPostPDF1.max(),6)]

a = 1.14
b = 9.5
x = np.linspace(2, 18, 160)
curve = [0.01 + 0.49*(1+(1/(1+math.exp(a*(b-val))))) for val in x]
ampRange = np.arange(2,18,16/160)

plt.figure()
plt.axes(title='Robust Best Fit Curve (Participant 1)',xlabel='Amplitude (micrometers)',ylabel='P(success)')
plt.plot(amp,np.divide(sData[0],n),'.')
plt.plot(ampRange,curve)



i,j = np.where(jointPostPDF2==jointPostPDF2.max())
MAP2 = [round(Ha[i[0]],2),round(Hb[j[0]],3),round(jointPostPDF2.max(),6)]

a = 1.14
b = 9.5
x = np.linspace(2, 18, 160)
curve = [0.01 + 0.49*(1+(1/(1+math.exp(a*(b-val))))) for val in x]
ampRange = np.arange(2,18,16/160)

plt.figure()
plt.axes(title='Robust Best Fit Curve (Participant 2)',xlabel='Amplitude (micrometers)',ylabel='P(success)')
plt.plot(amp,np.divide(sData[1],n),'.')
plt.plot(ampRange,curve)



i,j = np.where(jointPostPDF3==jointPostPDF3.max())
MAP3 = [round(Ha[i[0]],2),round(Hb[j[0]],3),round(jointPostPDF3.max(),6)]

a = 1.11
b = 9.5
x = np.linspace(2, 18, 160)
curve = [0.01 + 0.49*(1+(1/(1+math.exp(a*(b-val))))) for val in x]
ampRange = np.arange(2,18,16/160)

plt.figure()
plt.axes(title='Robust Best Fit Curve (Participant 3)',xlabel='Amplitude (micrometers)',ylabel='P(success)')
plt.plot(amp,np.divide(sData[2],n),'.')
plt.plot(ampRange,curve)