import numpy as np
import math

xhat = [8,8,8,10,10,10,12,12,12] # location of the neuron receptive fields on x axis
yhat = [8,10,12,8,10,12,8,10,12] # location of the neuron receptive fields on y axis

trial = [9,20,21,24,21,45,12,23,21] # number of spikes from each neuron on a trial

def rate(x,y,xh,yh):
    return 10*math.exp(-((x-xh)**2+(y-yh)**2)/8) 
    # calculate the expected firing rate given a tactile location at x and y, and receptive field at xhat and yhat

rateA = [rate(8.5,8,xh,yh)+rate(11.5,8,xh,yh)+rate(9.25,10,xh,yh)+rate(10.75,10,xh,yh)+rate(10,12,xh,yh) for xh,yh in zip(xhat,yhat)] # model for the letter A
rateV = [rate(10,8,xh,yh)+rate(9.25,10,xh,yh)+rate(10.75,10,xh,yh)+rate(8.5,12,xh,yh)+rate(11.5,12,xh,yh) for xh,yh in zip(xhat,yhat)] # model for the letter V
rateL = [rate(8,12,xh,yh)+rate(8,10,xh,yh)+rate(8,8,xh,yh)+rate(10,8,xh,yh)+rate(12,8,xh,yh) for xh,yh in zip(xhat,yhat)] # model for the letter L
rateT = [rate(8,12,xh,yh)+rate(10,12,xh,yh)+rate(12,12,xh,yh)+rate(10,10,xh,yh)+rate(10,8,xh,yh) for xh,yh in zip(xhat,yhat)] # model for the letter T
rateX = [rate(8,12,xh,yh)+rate(12,12,xh,yh)+rate(10,10,xh,yh)+rate(8,8,xh,yh)+rate(12,8,xh,yh) for xh,yh in zip(xhat,yhat)] # model for the letter X

def like(rate,trial):
    return np.prod([(math.exp(-rate[i])*(rate[i]**trial[i]))/math.factorial(trial[i]) for i in range(9)]) 
    # calculate the likelihood of the model (rate over all points) given a trial

L = [like(rateA,trial),like(rateV,trial),like(rateL,trial),like(rateT,trial),like(rateX,trial)] # calculate the likelihood of each model on this trial
post = L/sum(L) # normalize to get the posterior probability of each model on this trial
