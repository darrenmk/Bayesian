import numpy as np
import matplotlib.pyplot as plt

M1 = 0.7
M2 = 0.4

pebbles = [6,5,7,7,5,3,6,8,5,7]

likeM1 = np.product([(0.7**h)*((1-0.7)**(10-h)) for h in pebbles])
likeM2 = np.zeros((10))

for f in range(len(pebbles)):
    fish = pebbles[f]
    notFish = pebbles[:f] + pebbles[f+1:]
    likeM2[f] = np.product([(0.4**fish)*((1-0.4)**(10-fish))] + [(0.7**h)*((1-0.7)**(10-h)) for h in notFish])

likeM2 = np.sum(likeM2)/10

postM1 = likeM1/(likeM1+likeM2)
postM2 = likeM2/(likeM1+likeM2)

BF = postM2/postM1

#Q5b
location = [0,1,2,3,4,5,6,7,8,9]

likeM2b = np.zeros((10))

for f in range(len(pebbles)):
    fish = pebbles[f]
    notFish = pebbles[:f] + pebbles[f+1:]
    likeM2b[f] = np.product([(0.4**fish)*((1-0.4)**(10-fish))] + [(0.7**h)*((1-0.7)**(10-h)) for h in notFish])

postM2b = likeM2b/likeM2b.sum()
plt.axes(title='Posterior PDF (Q5b)',xlabel='yLocation',ylabel='Posterior Probability')
plt.plot(postM2b)