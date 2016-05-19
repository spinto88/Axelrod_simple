
from axelrod_py import *

rand.seed(123459)

A = zealots_list(1024, 20)
b = 0.20

mysys = Axl_network(n = 1024, f = 10, q = 20, A = A, b = b, mode_mf = 0, number_of_metric_feats = 1)

mysys.set_topology(id_topology = 1.1, opinion_links = 'No')

mysys.set_initial_state_equal()

for i in range(0,100):

#    mysys.rewiring()
    mysys.evolution(100)
    mysys.adherents_hist()    
