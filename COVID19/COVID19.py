import matplotlib.pyplot as plt
import numpy as np
import math

# Data obtained from the WHO daily situation reports
canada = [15, 20, 24, 27, 30, 34, 37, 54, 60, 66, 77, 95, 110, 142, 198, 252, 341, 441, 598, 727, 873, 1087, 1328, 1470, 2091, 2792, 3409, 4043, 4757, 5655, 6320, 7448, 8612, 9731, 11283, 12375] # feb 28
usa = [50, 57, 63, 68, 75, 100, 124, 158, 221, 319, 435, 541, 704, 994, 1301, 1695, 2247, 2943, 3680, 4663, 6411, 9259, 13789, 19383, 24207, 33592, 43781, 54856, 68211, 85435, 104126, 123578, 143491, 163788, 188530, 215003, 244877, 277161] # feb 26
germany = [16, 18, 26, 48, 74, 79, 130, 165, 203, 262, 545, 670, 800, 1040, 1224, 1565, 1966, 2745, 3675, 4599, 5813, 7272, 9367, 12327, 15320, 19848, 22364, 24873, 29056, 32991, 37323, 43938, 50871, 57695, 62435, 66885, 71808, 77981, 84794, 91159] # feb 24
france = [12, 14, 18, 38, 57, 100, 130, 191, 212, 285, 423, 653, 949, 1209, 1412, 1784, 2281, 2876, 3661, 4499, 5423, 6633, 7730, 9134, 10995, 12612, 14459, 16018, 19856, 22304, 25233, 29155, 32964, 37575, 40174, 44550, 52128, 56989, 59105, 82165] # feb 24
italy = [4, 21, 79, 157, 229, 323, 470, 655, 889, 1128, 1701, 2036, 2502, 3089, 3858, 4636, 5883, 7375, 9172, 10149, 12462, 15113, 17660, 21157, 24747, 27980, 31506, 35713, 41035, 47021, 53578, 59138, 63927, 69176, 74386, 80589, 86498, 92472, 97689, 101739, 105792, 110574, 115242, 119827] # feb 20
uk = [16, 20, 23, 36, 39, 51, 89, 118, 167, 210, 277, 323, 373, 460, 594, 802, 1144, 1395, 1547, 1954, 2630, 3277, 3983, 5018, 5683, 6650, 8077, 9529, 11658, 14543, 17089, 19522, 22141, 25150, 29474, 33718, 38168] # feb 28
spain = [3, 9, 13, 25, 33, 58, 84, 114, 151, 228, 282, 401, 525, 674, 1231, 1695, 2277, 3146, 4231, 6391, 7988, 9942, 11826, 14769, 18077, 21571, 25496, 28768, 35136, 42058, 49515, 57786, 65719, 73235, 80110, 87956, 95923, 104118, 112065, 119199] # feb 24

countries = [canada,usa,germany,france,italy,uk,spain]
populations = [37.59, 327.2, 82.79, 66.99, 60.48, 66.44, 46.66] # in 100 millions

HA = np.arange(1,11,0.05)
HT = np.arange(3,4,0.01)

jPDF = np.zeros((len(countries),len(HA),len(HT)))
postPDF = np.zeros((len(countries),len(HT)))
modeA = np.zeros((len(countries)))
modeT = np.zeros((len(countries)))
rangeT = np.zeros((len(countries),2))

for c in range(len(countries)):
    #### change data to country of interest
    data = np.around(np.diff(countries[c])/(populations[c]/100))
    day = np.arange(len(data))
    
    # Q2
    logL = np.zeros((len(HA),len(HT)))
    normL = np.zeros((len(HA),len(HT)))
    
    logfac = lambda x: (x - 1.5) * math.log(x - 1) - (x - 1) + 0.5 * math.log(2*math.pi) + 1.0/(12*(x-1)) if x else 0
    for i in range(len(HA)):
        for j in range(len(HT)):
            A = round(HA[i],2)
            T = round(HT[j],2)
            lambdas = [A*(2**(t/T)) for t in day]
            logL[i,j] = np.sum([(-lambdas[x]+data[x]*math.log(lambdas[x])-logfac(data[x])) for x in range(len(lambdas))])
    
    for i in range(len(HA)):
        for j in range(len(HT)):
            normL[i,j] = math.exp(logL[i,j]-logL.max())
    
    jPDF[c,:,:] = normL/normL.sum() # uniform priors
    modeIdx = np.where(jPDF[c,:,:]==np.max(jPDF[c,:,:]))
    modeA[c] = HA[modeIdx[0]]
    modeT[c] = HT[modeIdx[1]]
    postPDF[c,:] = list(np.sum(jPDF[c,:,:],axis=0))
    
    sort = sorted(postPDF[c,:],reverse=True)
    x = 0
    idx = [None]*len(HT)
    i = 0
    
    while x < 0.95:
        x = x + sort[i]
        idx[i] = HT[np.where(postPDF[c,:]==sort[i])]
        i += 1
    
    idx = [x for x in idx if x is not None]
    rangeT[c,0] = min(idx)
    rangeT[c,1] = max(idx) # this is the 95% confidence interval for T

plt.axes(title='Posterior PDF (Spain)',xlabel='Doubling Time',ylabel='Posterior Probability')
plt.plot(HT,postPDF[c,:])