
from axelrod_py import *

N = 1024
F = 10

rand.seed(123457)

for q in range(10, 100, 5):

    mysys = Axl_network(N, F, q, id_topology = 0.1)

    mysys.number_of_metric_feats = 1

    mysys.evol2convergence()

    smax, max_state = mysys.fragment_identifier()

    print q, smax
