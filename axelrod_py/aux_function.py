
import random as rand

def zealots_list(N,Z):

    number_zealots = int(Z)
    A=range(N)
    B=rand.sample(A,number_zealots)
    
    return B
