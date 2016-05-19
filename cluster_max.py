from axelrod_py import *



N = 1024
F = 10
Q = 20
Qz = 100
b = 0.01
Z = 10

#fp = open('Cluster_maximo.txt', 'a')
#fp.write('#Z\tmf\tmean\tstd\n')
#fp.close()


rand.seed(123458)
A = zealots_list(N,Z)
        



mysys = Axl_network(n = N, f = F, q = Q, q_z = Qz, b = b, A = A, number_of_metric_feats = 1, id_topology = 1.1)

mode_mf = 1    

mysys.evol2stationary()

mysys.vaccinate()


name = 'vacunados_Z_' + str(Z) + '_mf_' + str(b) + '.jpg' 
mysys.image_vaccinated(name)

distribution, maximo = mysys.fragment_identifier(type_serch = 1)



print maximo
print distribution


