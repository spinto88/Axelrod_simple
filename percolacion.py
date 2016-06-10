from axelrod_py import *

N = 2500
F = 10
Q = 300
Qz = 100
b = 0.0
Z = 20
rand.seed(123458)
A = zealots_list(N,Z)


name = 'Cluster_topology_percolacion.txt'
fp = open(name,'a')
fp.write('#cluster\tC\tl\tk\tmod\n')
fp.close()
    
for vacunados in range(0,N + 1,100):
    maximo_data = []
    avg_clust_data = []
    avg_spl_data = []
    avg_k_data = []
    mod_data = []
    for configuracion in range(0,1):
        
        B = zealots_list(N,vacunados)
        
        mysys = Axl_network(n = N, f = F, q = Q, q_z = Qz, b = b, A = A, number_of_metric_feats = 1, id_topology = 3.1)

        mysys.mode_mf = 1
        average = []    
        
        for i in B:
            mysys.agent[i].vaccine = 1
        
        S, maximo, distribution = mysys.subgraph_max()
        maximo_data.append(maximo)
        
        #coeficiente medio de clusterizacion
        S_ud = S.to_undirected()
        ccs =  nx.clustering(S_ud)
        avg_clust = sum(ccs.values()) / len(ccs)
        avg_clust_data.append(avg_clust)
        
        #Distancia mas corta media
        avg_spl = nx.average_shortest_path_length(S)
        avg_spl_data.append(avg_spl)
        
        #Grado medio de nodos
        avg_k = avg_neigh_degree(S)
        avg_k_data.append(avg_k)
        
        #Modularidad
        mod = get_modularity(S)
        mod_data.append(mod)
        
    fp = open(name,'a')
    fp.write(str(np.mean(maximo_data)) + '\t' + str(np.mean(avg_clust_data)) + '\t' + str(np.mean(avg_spl_data)) + '\t' + str(np.mean(avg_k_data)) + '\t' + str(np.mean(mod_data)) + '\n')
    fp.close()
