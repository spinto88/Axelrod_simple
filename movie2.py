from axelrod_py import *

N = 2500
F = 10
Q = 80
Qz = 100
Z = 10
rand.seed(123458)
A = zealots_list(N,Z)


for campo in range(1,3,1):

    phi = float(campo)/1000
    steps_data = []

    name = 'Vacunados_phi' + str(phi) + '.txt'

    fp = open(name,'a')
    fp.write('#tiempo\tvacunados\n')
    fp.close()

    mysys = Axl_network(n = N, f = F, ff = 0, q = Q, q_z = Qz, A = A, id_topology = 2.1)

    #Primera etapa
    mysys.evol_opinion = 0
    steps = mysys.evol2convergence() 

    #mysys.image_opinion()
    vaccinated = mysys.vaccinate()
    #vaccinated = mysys.image_vaccinated()

    fp = open(name,'a')
    fp.write(str(steps) + '\t' + str(vaccinated) + '\n')
    fp.close() 

    #Segunda etapa
    mysys.set_number_of_fixed_features(ff = F - 1)
    mysys.evol_opinion = 1
    mysys.opinion_included = 1
    mysys.phi = phi

    explosion = 0
    for i in range(2000):

        mysys.evolution(1000)
        steps = steps + 1000

        #mysys.image_opinion()
        vaccinated = mysys.vaccinate()
        #mysys.image_vaccinated()
        
        fp = open(name,'a')
        fp.write(str(steps) + '\t' + str(vaccinated) + '\n')
        fp.close()            

