import matplotlib.pyplot as plt

# Example 1
Hp = [round(x/100-0.005,3) for x in range(1,101)]
h = 0 # number of successes
n = 0 # number of trials
La = [0]*100
i = 0

for p in Hp:
    La[i] = (p**h)*((1-p)**(n-h)) # we can ignore the binomial coef
    i += 1

postPDFa = [l/sum(La) for l in La] # uniform priors
MAPa = [Hp[postPDFa.index(max(postPDFa))],max(postPDFa)]

plt.axes(title='Posterior PDF (1a)',xlabel='H(p)',ylabel='Posterior Probability')
plt.plot(Hp,postPDFa)
sorted_a = sorted(postPDFa,reverse=True)
x = 0
idx = [None]*100
i = 0

while x < 0.95:
    x = x + sorted_a[i]
    idx[i] = postPDFa.index(sorted_a[i])
    i += 1

idx = [x for x in idx if x is not None]
range_a = [Hp[min(idx)], Hp[max(idx)]] # this is the 95% confidence interval


# Example 2
h = 11
n = 12
Lb = [0]*100
i = 0

for p in Hp:
    Lb[i] = (p**h)*((1-p)**(n-h)) # we can ignore the binomial coef
    i += 1

postPDFb = [l/sum(Lb) for l in Lb] # uniform priors
MAPb = [Hp[postPDFb.index(max(postPDFb))],max(postPDFb)]

plt.axes(title='Posterior PDF (1b)',xlabel='H(p)',ylabel='Posterior Probability')
plt.plot(Hp,postPDFb)
sorted_b = sorted(postPDFb,reverse=True)
x = 0
idx = [None]*100
i = 0

while x < 0.95:
    x = x + sorted_b[i]
    idx[i] = postPDFb.index(sorted_b[i])
    i += 1

idx = [x for x in idx if x is not None]
range_b = [Hp[min(idx)], Hp[max(idx)]] # this is the 95% confidence interval
