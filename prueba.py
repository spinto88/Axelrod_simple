from axelrod_py import *

N = 25
F = 10
Q = 20

id_topology = 3.1

G = Axl_network(n = N, f = F, q = Q, id_topology = id_topology)

for i in range (0,25,6):
    print str(i)
    print G.neighbors(i)
