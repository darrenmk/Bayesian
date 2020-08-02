import numpy as np
import math

mu1 = 0
Hmu2 = [1,2,3,4]
Hsigma = [1,2,3]

data = [0,0,0,0,0,0,0,0] # data goes here

like1 = np.zeros((3))
like2 = np.zeros((4,3))

# first we must generate a posterior PDF for A and B
for i in range(len(Hmu2)):
    for j in range(len(Hsigma)):
        mu2 = Hmu2[i]
        sigma = Hsigma[j]
        like1[j] = np.prod([(1/(sigma*math.sqrt(2*math.pi)))*math.exp(-((x-mu1)**2/(2*sigma**2))) for x in data])
        like2[i,j] = np.prod([(1/(sigma*math.sqrt(2*math.pi)))*math.exp(-((x-mu2)**2/(2*sigma**2))) for x in data])

likeM1 = np.mean(like1)
likeM2 = np.mean(like2)

postM1 = likeM1/(likeM1+likeM2)
postM2 = likeM2/(likeM1+likeM2)

BF = postM2/postM1
