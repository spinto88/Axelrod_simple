
from axelrod_py import *

rand.seed(123459)

mysys = Axl_network(n = 1024, f = 10, q = 20)

mysys.set_topology(id_topology = 3.0, opinion_links = 'Yes')
"""
print mysys.agent[0].contact_links[:8]
print mysys.agent[0].opinion_links[:8]

print nx.degree_histogram(mysys)
"""
for i in range(0, 100):

    mysys.rewiring()
    mysys.evolution(100)

"""
print nx.degree_histogram(mysys)
print mysys.agent[0].contact_links[:8]
print mysys.agent[0].opinion_links[:mysys.agent[0].degree_opinion]
"""
