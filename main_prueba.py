from axelrod_py import *

N = 1024
F = 10
Q = 300
Qz = 100
b = 0.02
Z = 10
rand.seed(123458)
A = zealots_list(N,Z)


name = 'Cluster_topology_Q' + str(Q) + 'b_' + str(b) +'_cutoff90.txt'

fp = open(name,'a')
fp.write('#cluster\tC\tl\tk\tmod\tno_vaccinated\n')
fp.close()

data = []
fname = 'Top1.1_Z' + str(Z) + '_b' + str(b) + '_Q' + str(Q) + '_cutoff90.dat'

for configuracion in range(0,1000):

    mysys = Axl_network(n = N, f = F, q = Q, q_z = Qz, b = b, A = A, number_of_metric_feats = 0, id_topology = 3.1)

    mysys.mode_mf = 1
    average = []    

    mysys.evolution(100)
    
    data.append(mysys.adherents_distribution()[0])        
    
    fp = open(name,'a')
    fp.write(str(maximo) + '\t' + str(avg_clust) + '\t' + str(avg_spl) + '\t' + str(avg_k) + '\t' + str(mod) + '\t' + str(no_vaccinated) + '\n')
    fp.close()
    

np.savetxt(fname, data)
