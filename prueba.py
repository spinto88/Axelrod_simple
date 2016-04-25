from axelrod_py import *

N = 1024
F = 10
topology = 0.1
fraction = 1
q = 10000
q_z = 10000

for z_aux in range(50,51,5):
    Z =float(z_aux)/100

    for metric in range(1,2,2):
        
        metric_features = metric
        rand.seed(123413)

        A = zealots_list(N,Z)
        
        mysys = Axl_network(N, F, q, q_z, A = A, fraction = fraction, id_topology = topology)
        
        mysys.number_of_metric_feats = metric_features
        
        for i in range(0,100):
        
            mysys.evolution(200)
            
            print mysys.adherents_counter()
