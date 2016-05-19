from axelrod_py import *

N = 1024
F = 10
Q = 20
Qz = 100
b = 0.01
Z = 10
rand.seed(123458)
A = zealots_list(N,Z)


for Z in range(0,15,10):
    for campo in range(0,10,2):
        b = float(campo)/100    
        mysys = Axl_network(n = N, f = F, q = Q, q_z = Qz, b = b, A = A, number_of_metric_feats = 1, id_topology = 1.1)

        mysys.mode_mf = 1
        average = []    

        steps, average = mysys.evol2stationary()

        for i in range(0,1000):
            mysys.evolution(1000)
            data_average = mysys.adherents_distribution()[1]
            average.append(data_average)
            
        fig = plt.figure(1)
        fig.clf()
        plt.plot(average)
        plt.xlabel('Tiempo')
        plt.ylabel('Valor medio de la distribucion')
        plt.title('Evolucion del valor medio de la distribucion \n de adherentes a cada qz, con campo activo')
        plt.savefig('Z_' + str(Z) + '_b_' + str(b) + '.jpg')


