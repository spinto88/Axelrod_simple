from axelrod_py import *



N = 1024
F = 10
Q = 20
Qz = 100
b = 0.2
Z = 10
A = zealots_list(N,Z)

rand.seed(123458)

    
mysys = Axl_network(n = N, f = F, q = Q, q_z = Qz, b = b, A = A, number_of_metric_feats = 1, id_topology = 0.1)

average = []    

steps, average, stationary = mysys.evol2stationary()


fig = plt.figure(1)
fig.clf()
plt.plot(average)
#plt.savefig('Z' + str(int(data[i][0])) + '_b' + str(b) + '.eps')

