from axelrod_py import *

N = 1024
F = 10
Q = 20
Qz = 100
b = 0.1
Z = 10
rand.seed(123458)
A = zealots_list(N,Z)
    
mysys = Axl_network(n = N, f = F, q = Q, q_z = Qz, b = b, A = A, number_of_metric_feats = 1, id_topology = 1.1)

print mysys.neighbors(0)
print nx.degree_histogram(mysys)

for i in range(0,1000):
    mysys.evolution(1000)
    try:
        data_average = mysys.adherents_distribution()[1]
    except:
        print mysys.adherents_distribution()[0]
    average.append(data_average)
