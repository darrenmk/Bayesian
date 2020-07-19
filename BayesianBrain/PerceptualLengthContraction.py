import numpy as np
import math
import matplotlib.pyplot as plt
np.set_printoptions(precision=4)

sigmas = 1
sigmav = 10
lm = 9
t = 0.2

tau = sigmas/sigmav
lstar = lm/(1+2*(tau/t)**2)

time = (math.sqrt(2)*tau*math.sqrt(8))/math.sqrt(1)

binwidth = 0.1
l = np.arange(-10,15.1,binwidth)

#2a
sigmas2 = math.sqrt(2*sigmas)
sigmav2 = t*sigmav

likes = [(1/(sigmas2*math.sqrt(2*math.pi)))*math.exp((-(lm-s)**2)/(2*(sigmas2**2))) for s in l]
likev = [(1/(sigmav2*math.sqrt(2*math.pi)))*math.exp((-(0-s)**2)/(2*(sigmav2**2))) for s in l]

likec0 = [s*v for s,v in zip(likes,likev)]
likec = [(x/sum(likec0))/binwidth for x in likec0]

plt.axes(title='Perceptual Length (b)', xlabel='Candidate l (cm)', ylabel='Probability Density', xticks=np.arange(0,251,10), xticklabels=np.arange(-10,15,1))
plt.plot(likes,color='red')
plt.plot(likev,color='blue')
plt.plot(likec,color='green')
