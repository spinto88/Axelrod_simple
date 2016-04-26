from axelrod_py import *

N = 1024
F = 10
Q = 20

rand.seed(123457)

A = Axl_network(N, F, Q, Q, id_topology = 0.1)

A.evolution(9000)

data = A.fragment_identifier(5)

print data[0]
print data[1]

