import matplotlib.pyplot as plt
import numpy as np
import math

# Data obtained from the WHO daily situation reports
canada = [15, 20, 24, 27, 30, 34, 37, 54, 60, 66, 77, 95, 110, 142, 198, 252, 341, 441, 598, 727, 873, 1087, 1328] # feb 28
usa = [50, 57, 63, 68, 75, 100, 124, 158, 221, 319, 435, 541, 704, 994, 1301, 1695, 2247, 2943, 3680, 4663, 6411, 9259, 13789, 19383, 24207] # feb 26
germany = [16, 18, 26, 48, 74, 79, 130, 165, 203, 262, 545, 670, 800, 1040, 1224, 1565, 1966, 2745, 3675, 4599, 5813, 7272, 9367, 12327, 15320, 19848, 22364] # feb 24
france = [12, 14, 18, 38, 57, 100, 130, 191, 212, 285, 423, 653, 949, 1209, 1412, 1784, 2281, 2876, 3661, 4499, 5423, 6633, 7730, 9134, 10995, 12612, 14459] # feb 24
italy = [4, 21, 79, 157, 229, 323, 470, 655, 889, 1128, 1701, 2036, 2502, 3089, 3858, 4636, 5883, 7375, 9172, 10149, 12462, 15113, 17660, 21157, 24747, 27980, 31506, 35713, 41035, 47021, 53578] # feb 20
uk = [16, 20, 23, 36, 39, 51, 89, 118, 167, 210, 277, 323, 373, 460, 594, 802, 1144, 1395, 1547, 1954, 2630, 3277, 3983, 5018] # feb 28
spain = [3, 9, 13, 25, 33, 58, 84, 114, 151, 228, 282, 401, 525, 674, 1231, 1695, 2277, 3146, 4231, 6391, 7988, 9942, 11826, 14769, 18077, 21571, 25496] # feb 24

countries = [canada,usa,germany,france,italy,uk,spain]
populations = [37.59, 327.2, 82.79, 66.99, 60.48, 66.44, 46.66] # in 100 millions

Ha = np.arange(6,10,0.1)
Hb = np.arange(20,30,0.5)
Hc = np.arange(0.4,1,0.1)

jPDF = np.zeros((len(countries),len(Ha),len(Hb),len(Hc)))
modea = np.zeros((len(countries)))
modeb = np.zeros((len(countries)))
modec = np.zeros((len(countries)))
rangeT = np.zeros((len(countries),2))

for z in range(len(countries)):
    #### change data to country of interest
    data = np.around(np.diff(countries[z])/(populations[z]/100))
    day = np.arange(len(data))
    
    # Q2
    logL = np.zeros((len(Ha),len(Hb),len(Hc)))
    normL = np.zeros((len(Ha),len(Hb),len(Hc)))
    
    for i in range(len(Ha)):
        for j in range(len(Hb)):
            for k in range(len(Hc)):
                a = round(Ha[i],2)
                b = round(Hb[j],2)
                c = round(Hc[k],2)
                p = [c/(1+math.exp(a*(b-x))) for x in day]
                logL[i,j,k] = sum([(countries[z][x])*math.log(p[x]) + ((populations[z]*1000000)-countries[z][x])*math.log(1-p[x]) for x in range(len(p))])
    
    for i in range(len(Ha)):
        for j in range(len(Hb)):
            for k in range(len(Hc)):
                normL[i,j,k] = math.exp(logL[i,j,k]-logL.max())
    
    jPDF[z,:,:,:] = normL/normL.sum() # uniform priors
    modeIdx = np.where(jPDF[z,:,:,:]==np.max(jPDF[z,:,:,:]))
    modea[z] = Ha[modeIdx[0]]
    modeb[z] = Hb[modeIdx[1]]
    modec[z] = Hc[modeIdx[2]]
    
plt.axes(title='Posterior PDF',xlabel='Doubling Time',ylabel='Posterior Probability')
plt.plot(Ha,postPDF[c,:])