
from axelrod_py import *

N = 1024
F = 10
topology = 0.1
fraction = 1
q_z = 100

for z_aux in range(10,11,5):
    Z =float(z_aux)/100

    for metric in range(1,2,2):
        
        metric_features = metric
        rand.seed(123413)

        A = zealots_list(N,Z)

        B = 0.00
        # Strategia del campo externo (0 es medio masivo constante en el tiempo)
        strategy = 0

        fp = open('Smax_talibanes_' + str(Z) + '_metric_' + str(metric) + '.txt', 'a')
        fp.write('#q\tsmax\tstd\n')
        fp.close()

        Number_of_configurations = 200

        smax_mean = []
        smax_std = []

        qrange = range(10, 200, 2)

        for q in qrange:

            smax_data = []

            for conf in range(0, Number_of_configurations):

     	        mysys = Axl_network(N, F, q, q_z, A = A, fraction = fraction, id_topology = topology)

                mysys.number_of_metric_feats = metric_features

                mysys.mass_media.b = B
                mysys.mass_media.strategy = strategy

                mysys.evol2convergence()

                # En vez de converger le digo cuantos pasos correr
                # mysys.evolution(15000)
                
               
                # Fragmento mas grande y estado
                smax, max_state = mysys.fragment_identifier()
                smax_data.append(smax)
    
            fp = open('Smax_talibanes_' + str(Z) + '_metric_' + str(metric) + '.txt', 'a')
            fp.write(str(q) + '\t' + str(np.mean(smax_data)) + '\t' + str(np.std(smax_data)) + '\n')
            fp.close()

            smax_mean.append(np.mean(smax_data))
            smax_std.append(np.std(smax_data))

        # Grafico
        plt.errorbar(qrange, smax_mean, smax_std)
        plt.show()
