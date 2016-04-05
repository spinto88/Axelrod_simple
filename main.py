
from axelrod_py import *

N = 1000
F = 10

rand.seed(123458)


for q in range(60, 61):

    mysys = Axl_network(N, F, q, id_topology = 0.1)
    mysys.noise = 0.001

    mysys.evolution(5000)

    smax, max_state = mysys.fragment_identifier()

    print q, smax, max_state


