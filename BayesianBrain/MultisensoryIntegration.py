import numpy as np
import math
import matplotlib.pyplot as plt
np.set_printoptions(precision=4)

xpos = np.arange(-5,5.01,.01)
xv = -.1
xa = .1
sigmav = 1.5
sigmaa = 2

Lv = [(1/(sigmav*math.sqrt(2*math.pi)))*math.exp((-(xv-s)**2)/(2*(sigmav**2))) for s in xpos] # likelihood function of visual estimate
La = [(1/(sigmaa*math.sqrt(2*math.pi)))*math.exp((-(xa-s)**2)/(2*(sigmaa**2))) for s in xpos] # likelihood function of auditory estimate

Lc = [a*v for a,v in zip(La,Lv)] # likelihood function of combined estimate
Lc1 = [(x/sum(Lc))/.01 for x in Lc] # likelihood function of combined estimate

mu = ((xv/(sigmav**2))+(xa/(sigmaa**2)))/((1/(sigmav**2))+(1/(sigmaa**2)))
var = 1/((1/(sigmav**2))+(1/(sigmaa**2)))

Lc2 = [(1/(math.sqrt(var)*math.sqrt(2*math.pi)))*math.exp((-(mu-s)**2)/(2*var)) for s in xpos]

plt.axes(xticks=np.arange(0,1001,100), xticklabels=np.arange(-5,5,1))
plt.plot(likev,color='blue')
plt.plot(likea,color='red')
plt.plot(likec1,color='green')

MAP = [xpos[Lc2.index(max(Lc2))],max(Lc2)]
