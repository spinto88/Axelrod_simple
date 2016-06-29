
from axelrod_py import *

N = 2500
F = 10
Q = 1000

rand.seed(123457)

A = zealots_list(N, Z = 10)

mysys = Axl_network(n = N, f = F, q = Q, ff = 0, A = A)

mysys.evol_opinion = 1
mysys.opinion_included = 1
mysys.phi = 0.01

mysys.set_topology(2.1, rewiring = 0)

for i in range(1000):

    mysys.evolution(100)

    mysys.image_opinion()
    
