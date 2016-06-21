from axelrod_py import *

N = 2500
F = 10
Q = 80
Qz = 100
Z = 10
rand.seed(123458)
A = zealots_list(N,Z)


mysys = Axl_network(n = N, f = F, ff = 0, q = Q, q_z = Qz, A = A, id_topology = 2.1)

#Primera etapa
mysys.evol_opinion = 0
steps = mysys.evol2convergence() 

mysys.image_opinion()
vaccinated = mysys.vaccinate()
vaccinated = mysys.image_vaccinated()

#Segunda etapa
mysys.set_number_of_fixed_features(ff = F - 1)
mysys.evol_opinion = 1
mysys.opinion_included = 1
mysys.phi = 0.005

explosion = 0
for i in range(2000):

    mysys.evolution(1000)
    steps = steps + (i+1)*1000

    mysys.image_opinion()
    vaccinated = mysys.vaccinate()
    mysys.image_vaccinated()
    
            

