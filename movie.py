from axelrod_py import *

N = 1024
F = 10
Q = 170
Qz = 100
Z = 10
rand.seed(123458)
A = zealots_list(N,Z)


mysys = Axl_network(n = N, f = F, ff = 0, q = Q, q_z = Qz, A = A, id_topology = 2.1)

mysys.set_topology(id_topology = 3.1, opinion_links = 'Yes')

mysys.image_opinion()
mysys.vaccinate()
mysys.image_vaccinated()

mysys.evol_opinion = 1  #evolucionar la opinion
mysys.opinion_included = 1    #incluir la opinion en la homofilia
mysys.phi = 0

for i in range(0,10000):

    mysys.evolution(1000)
   # mysys.rewiring()

    mysys.image_opinion()
    mysys.vaccinate()
    mysys.image_vaccinated()
    
   
        
