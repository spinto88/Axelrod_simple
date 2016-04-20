
from axelrod_py import *

N = 1024
F = 10
fraction = 1

rand.seed(123413)


fp = open('Prueba.txt', 'a')
fp.write('#q\tsmax\tstd\n')
fp.close()

for q in range(10, 100, 2):

    smax_data = []

    for conf in range(0, 1):

        mysys = Axl_network(N, F, q, fraction, id_topology = 0.1)

        mysys.number_of_metric_feats = 1

        mysys.evol2convergence()

        smax, max_state = mysys.fragment_identifier()

        smax_data.append(smax)
        
        
        
    fp = open('Prueba.txt', 'a')
    fp.write(str(q) + '\t' + str(np.mean(smax_data)) + '\t' + str(np.std(smax_data)) + '\n')
    fp.close()
