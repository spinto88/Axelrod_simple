from axelrod_py import *

N = 1024
F = 10
Q = 20
b = 0.25
Z = 20

id_topology = 1.1

rand.seed(123451)

A = zealots_list(N, Z)

mysys = Axl_network(n = N, f = F, q = Q, b = b, A = A, id_topology = id_topology, number_of_metric_feats = 1)

plt.ion()

for i in range(0, 101):

    mysys.adherents_hist()

    mysys.evolution(10000)

    plt.title('Z = 20 Phi = 0.30 Step = ' + str(i * 10000))

#print mysys.evol2stationary()

#mysys.adherents_hist()
