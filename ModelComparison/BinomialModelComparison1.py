import numpy as np

Ho1 = np.arange(0.05,1,.1)
Ho2A = Ho1*(1/5)
Ho2B = Ho1*(2/5)

o1 = [n1,k-n1] # fill in values
o2 = [n2,k-n2] # fill in values

likeM1 = np.mean([((p**o1[0])*((1-p)**o1[1]))*((p**o2[0])*((1-p)**o2[1])) for p in Ho1])
likeM2 = np.mean([((p1**o1[0])*((1-p1)**o1[1])*(p2**o2[0])*((1-p2)**o2[1])) for p1,p2 in zip(Ho1,Ho2A)] + [((p1**o1[0])*((1-p1)**o1[1])*(p2**o2[0])*((1-p2)**o2[1])) for p1,p2 in zip(Ho1,Ho2B)])

postM1 = likeM1/(likeM1+likeM2)
postM2 = likeM2/(likeM1+likeM2)

BF = postM2/postM1
