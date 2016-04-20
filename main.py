
from axelrod_py import *

N = 64
F = 10

rand.seed(123457)


fp = open('Data_smax.txt', 'a')
fp.write('#q\tsmax\tstd\n')
fp.close()

for q in range(10, 100, 5):

    smax_data = []

    for conf in range(0, 50):

        mysys = Axl_network(N, F, q, id_topology = 0.1)

        mysys.number_of_metric_feats = 1

        mysys.evol2convergence()

        smax, max_state = mysys.fragment_identifier()

        smax_data.append(smax)
        
        
        
    fp = open('Data_smax.txt', 'a')
    fp.write(str(q) + '\t' + str(np.mean(smax_data)) + '\t' + str(np.std(smax_data)) + '\n')
    fp.close()
