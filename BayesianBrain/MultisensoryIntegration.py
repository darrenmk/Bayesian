import numpy as np
import math
import matplotlib.pyplot as plt
np.set_printoptions(precision=4)

xpos = np.arange(-5,5.01,.01)
xv = -.1
xa = .1
sigmav = 1.5
sigmaa = 2

likev = [(1/(sigmav*math.sqrt(2*math.pi)))*math.exp((-(xv-s)**2)/(2*(sigmav**2))) for s in xpos]
likea = [(1/(sigmaa*math.sqrt(2*math.pi)))*math.exp((-(xa-s)**2)/(2*(sigmaa**2))) for s in xpos]

likec = [a*v for a,v in zip(likea,likev)]
likec1 = [(x/sum(likec))/.01 for x in likec]

mu = ((xv/(sigmav**2))+(xa/(sigmaa**2)))/((1/(sigmav**2))+(1/(sigmaa**2)))
var = 1/((1/(sigmav**2))+(1/(sigmaa**2)))

likec2 = [(1/(math.sqrt(var)*math.sqrt(2*math.pi)))*math.exp((-(mu-s)**2)/(2*var)) for s in xpos]

plt.axes(xticks=np.arange(0,1001,100), xticklabels=np.arange(-5,5,1))
plt.plot(likev,color='blue')
plt.plot(likea,color='red')
plt.plot(likec1,color='green')

mode = [xpos[likec1.index(max(likec1))],max(likec1)]