
from axelrod_py import *

N = 1024
F = 10
Q = 20
Qz = 100

rand.seed(123458)

A = zealots_list(N, Z = 0)

mysys = Axl_network(n = N, f = F, q = Q, q_z = Qz, b = 0.0, A = A, number_of_metric_feats = 1, id_topology = 0.1)

mysys.evolution(10000)
print mysys.adherents_distribution()
print np.average(range(0, Qz), weights = mysys.adherents_distribution())
mysys.adherents_hist()

