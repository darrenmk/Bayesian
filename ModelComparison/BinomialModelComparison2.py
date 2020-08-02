import numpy as np

M1 = 1/5
M2 = np.arange(0.30,0.51,0.05)

correct = [22,100-22]

likeM1 = (M1**correct[0])*((1-M1)**correct[1])
likeM2 = np.mean([(p**correct[0])*((1-p)**correct[1]) for p in M2])

postM1 = likeM1/(likeM1+likeM2)
postM2 = likeM2/(likeM1+likeM2)

BF = postM1/postM2

BFb = 1
h = 1

while BFb >= 1:
    data = [h,100-h]
    likeM1b = (M1**data[0])*((1-M1)**data[1])
    likeM2b = np.mean([(p**data[0])*((1-p)**data[1]) for p in M2])
    postM1b = likeM1b/(likeM1b+likeM2b)
    postM2b = likeM2b/(likeM1b+likeM2b)
    BFb = postM1b/postM2b
    
    if BFb >= 1:
        h += 1
    else:
        pass
