from axelrod_py import *

data = np.loadtxt('data_tau.txt')

N = 1024
F = 10
Q = 20
Qz = 100

rand.seed(123458)

for i in range(0, len(data)):

    A = zealots_list(N, Z = int(data[i][0]))
    b = data[i][1]
    tau = data[i][2]
    
    mysys = Axl_network(n = N, f = F, q = Q, q_z = Qz, b = b, A = A, number_of_metric_feats = 1, id_topology = 0.1)

    average = []    
    
    for j in range(0, int(tau / 100)):

        mysys.evolution(100)
        average.append(mysys.adherents_distribution()[1])

    fig = plt.figure(1)
    fig.clf()
    plt.plot(average)
    plt.savefig('Z' + str(int(data[i][0])) + '_b' + str(b) + '.eps')

