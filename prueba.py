
from axelrod_py import *

N = 1024
F = 10
Q = 20

rand.seed(1234510)

for i in range(1000):

    mysys = Axl_network(n = N, f = F, q = Q, rewiring = 1)

    mysys.set_topology(2.0)

#print mysys.agent[0].opinion_links[:8]
#print mysys.agent[0].feat[:10]
#print mysys.agent[0].opinion_degree

    mysys.evolution(10)

#    dist = []
#    for i in range(N):
#        dist.append(mysys.agent[i].opinion_degree)

#plt.hist(dist, range = [0, 40], bins = 40)
#plt.show()

