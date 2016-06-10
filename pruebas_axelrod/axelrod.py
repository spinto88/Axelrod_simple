from axelrod_py import *

N = 1024
F = 11

rand.seed(123458)

for Q in range(40,100,10):

    for configuration in range(0,100):
        name = 'distribution_axelrod' + str(Q) + '.txt'
         
        mysys = Axl_network(n = N, f = F, q = Q, number_of_metric_feats = 0, id_topology = 1.1)

        mysys.evol2convergence()
        size_max,distribution = mysys.fragment_identifier(type_search = 10) 

        fp = open(name,'a')
        for item in distribution:
            fp.write(str(item) + '\n')
        fp.close()
    
