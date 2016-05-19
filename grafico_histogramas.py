from axelrod_py import *

N = 1024
F = 10
Q = 20
b = 0
Z = 10

# Red cuadrada sin CPC
id_topology = 1.1

rand.seed(123457)

A = zealots_list(N, Z)

mysys = Axl_network(n = N, f = F, q = Q, b = b, A = A, id_topology = id_topology, number_of_metric_feats = 1)

# Modo del campo externo: 0.reactivo, 1.activo
mysys.mode_mf = 1

# Grafica en forma interactiva
plt.ion()

for i in range(0, 101):

    mysys.adherents_hist()

    mysys.evolution(100)

