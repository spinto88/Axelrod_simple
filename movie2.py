from axelrod_py import *

N = 10000
F = 10
Q = 20
Qz = 100
Z = 10
rand.seed(123458)
A = zealots_list(N,Z)

mysys = Axl_network(n = N, f = F, ff = 0, q = Q, q_z = Qz, A = A, id_topology = 2.1)

#mysys.evol_opinion = 1
#mysys.phi = 0.0001

#mysys.set_zealots(A, type_z = 1)

#mysys.evolution(10000) 

mysys.image_opinion()
mysys.vaccinate()
mysys.image_vaccinated()

mysys.evol_opinion = 1
mysys.phi = 0.001

for i in range(1000):

    mysys.image_opinion()
    mysys.vaccinate()
    mysys.image_vaccinated()
    mysys.evolution(1000)
