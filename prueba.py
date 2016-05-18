
from axelrod_py import *


mysys = Axl_network(n = 102, f = 10, q = 20, id_topology = 2.1)

print mysys.nagents
print mysys.number_of_nodes()
print nx.degree_histogram(mysys)

