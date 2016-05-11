from axelrod_py import *

N = 1024
F = 10
Q = 20
Qz = 100

rand.seed(123458)

for Z in [10, 25, 35, 50]:

    A = zealots_list(N, Z)

    for b in [0.10, 0.20, 0.30, 0.40]:
    
        mysys = Axl_network(n = N, f = F, q = Q, q_z = Qz, b = b, A = A, number_of_metric_feats = 1, id_topology = 0.1)

        tau = mysys.evol2stationary()

        fp = open('data_tau.txt','a')
        fp.write(str(Z) + '\t' + str(b) + '\t' + str(tau) + '\n')
        fp.close()
