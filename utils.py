import numpy as np
from math import factorial as fact


def norm(a):
    return ((1+np.arange(len(a)))*a).sum()

def card(a):
    return a.sum()

def magn(a):
    return ((2+np.arange(len(a)))*a).sum()



def partial(i,a):
    if i==2:
        return a - np.eye(1,len(a),0,dtype=int)[0]
    return a + np.eye(1,len(a),i-3,dtype=int)[0] - np.eye(1,len(a),i-2,dtype=int)[0]



def partialterm(l,i,b):
    if i==2:
        return l-magn(b)+1
    return b[i-3]+1




