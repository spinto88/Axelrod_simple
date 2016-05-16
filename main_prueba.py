from axelrod_py import *



N = 1024
F = 10
Q = 20
Qz = 100
b = 0.1
Z = 10
rand.seed(123458)
A = zealots_list(N,Z)



    
mysys = Axl_network(n = N, f = F, q = Q, q_z = Qz, b = b, A = A, number_of_metric_feats = 1, id_topology = 1.1)

average = []    

steps, average = mysys.evol2stationary()

fig = plt.figure(1)
fig.clf()
plt.plot(average)
plt.show()

for i in range(0,1000):
    mysys.evolution(1000)
    data_average = mysys.adherents_distribution()[1]
    average.append(data_average)
    
fig = plt.figure(2)
fig.clf()
plt.plot(average)
plt.show()
#plt.savefig('Z' + str(int(data[i][0])) + '_b' + str(b) + '.eps')

