
from axelrod_py import *

N = 1024
F = 10

rand.seed(123457)

for q in range(10, 80, 5):

    mysys = Axl_network(N, F, q, id_topology = 0.0)

    mysys.evol2convergence()
    smax, state = mysys.fragment_identifier()

    print q, smax

