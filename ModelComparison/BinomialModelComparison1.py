import numpy as np

Hpc = np.arange(0.05,1,.1)
HmacA = Hpc*(1/5)
HmacB = Hpc*(2/5)

o1 = [20,50]
o2 = [5,65]

likeM1 = np.mean([((p**o1[0])*((1-p)**o1[1]))*((p**o2[0])*((1-p)**o2[1])) for p in Hpc])
likeM2 = np.mean([((p1**o1[0])*((1-p1)**o1[1])*(p2**o2[0])*((1-p2)**o2[1])) for p1,p2 in zip(Hpc,HmacA)] + [((p1**o1[0])*((1-p1)**o1[1])*(p2**o2[0])*((1-p2)**o2[1])) for p1,p2 in zip(Hpc,HmacB)])

postM1 = likeM1/(likeM1+likeM2)
postM2 = likeM2/(likeM1+likeM2)

BF = postM2/postM1
