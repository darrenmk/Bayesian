import matplotlib.pyplot as plt

# Q2a
nFish = [x for x in range(40,401)]
Hp = [20/x for x in range(40,401)]
h = 2
n = 10
mode = nFish[Hp.index(h/n)] # is 100

# Q2b
L = [0]*361
i = 0

for p in Hp:
    L[i] = (p**h)*((1-p)**(n-h)) # we can ignore the binomial coef
    i += 1

postPDFb = [l/sum(L) for l in L] # uniform priors
MAPb = [nFish[postPDFb.index(max(postPDFb))],max(postPDFb)]

plt.axes(title='Posterior PDF (2b)',xlabel='H(number of fish)',ylabel='Posterior Probability')
plt.plot(nFish,postPDFb)
sorted_b = sorted(postPDFb,reverse=True)
x = 0
idx = [None]*361
i = 0

while x < 0.95:
    x = x + sorted_b[i]
    idx[i] = postPDFb.index(sorted_b[i])
    i += 1

idx = [x for x in idx if x is not None]
range_b = [nFish[min(idx)], nFish[max(idx)]] # this is the 95% confidence interval

# Q2c
h = 8
n = 40
L = [0]*361
i = 0

for p in Hp:
    L[i] = (p**h)*((1-p)**(n-h)) # we can ignore the binomial coef
    i += 1

postPDFc = [l/sum(L) for l in L] # uniform priors
MAPc = [nFish[postPDFc.index(max(postPDFc))],max(postPDFc)]

plt.axes(title='Posterior PDF (2c)',xlabel='H(number of fish)',ylabel='Posterior Probability')
plt.plot(nFish,postPDFc)
sorted_c = sorted(postPDFc,reverse=True)
x = 0
idx = [None]*361
i = 0

while x < 0.95:
    x = x + sorted_c[i]
    idx[i] = postPDFc.index(sorted_c[i])
    i += 1

idx = [x for x in idx if x is not None]
range_c = [nFish[min(idx)], nFish[max(idx)]] # this is the 95% confidence interval