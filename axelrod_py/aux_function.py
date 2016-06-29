
import random as rand
#import community

def zealots_list(N,Z):

    number_zealots = int(Z)
    A=range(N)
    B=rand.sample(A,number_zealots)
    
    return B
"""   
def avg_neigh_degree(G):
    
    mean = sum(G.degree().values())/float(len(G))
     
    return mean    
    
def get_modularity(G):
    
    partition = community.best_partition(G)
    
    return community.modularity(partition, G)    
"""
