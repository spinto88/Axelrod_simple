from axelrod_py import *

N = 1024
F = 10
q=20
q_z = 100

rand.seed(123413)

mysys = Axl_network(N, F, q, q_z)

mysys.evolution(100)

A=mysys.adherents_distribution(q_z) 

print A
