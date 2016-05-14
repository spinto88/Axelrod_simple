
from axelrod_py import *

N = 1024
F = 10
Q = 20

for Z in [10, 20, 30, 40, 50]:

    for b in [0.1, 0.2, 0.3, 0.4, 0.5]:

        rand.seed(123457)

        A = zealots_list(N, Z)

        mysys = Axl_network(N, F, Q, id_topology = 1.1, number_of_metric_feats = 1, b = b, A = A)

        data = []
        fname = 'Top1.1_Z' + str(Z) + '_b' + str(b) + '.dat'

        for conf in range(0, 20):

            mysys.evol2stationary()

            data.append(mysys.adherents_distribution()[0])

        np.savetxt(fname, data)
