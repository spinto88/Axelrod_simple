
from axelrod_py import *

N = 1024
F = 10
topology = 0.1
fraction = 1
q_z = 1000

for Z in range(0,15,2):
    # Z es el número de talibanes que se distribuyen al azar en la red   
    for metric in range(1,2,2):
        
        metric_features = metric
        rand.seed(123413)

        A = zealots_list(N,Z)

        B = 0.00
        # Strategia del campo externo (0 es medio masivo constante en el tiempo)
        strategy = 0

        #fp = open('Smax_talibanes_' + str(Z) + '_metric_' + str(metric) + '.txt', 'a')
        #fp.write('#q\tsmax\tstd\n')
        #fp.close()

        Number_of_configurations = 50

        smax_mean = []
        smax_std = []

        qrange = range(20, 90, 60)

        for q in qrange:

            smax_data = []

            for conf in range(0, Number_of_configurations):

     	        mysys = Axl_network(N, F, q, q_z, A = A, fraction = fraction, id_topology = topology)

                mysys.number_of_metric_feats = metric_features

                mysys.mass_media.b = B
                mysys.mass_media.strategy = strategy

                # mysys.evol2convergence()

                # En vez de converger le digo cuantos pasos correr
                for steps in range(0,100):

                    adherents = mysys.adherents_counter()
                    
                    fp = open('Adherentes_Z_' + str(Z) + '_metric_' + str(metric) + '_q_' + str(q) + '_conf_' + str(conf) + '.txt', 'a')
                    fp.write(str(steps*100) + '\t' + str(adherents) + '\n')
                    fp.close()
                                    
                    mysys.evolution(100)

               
                # Fragmento mas grande y estado
                smax, max_state = mysys.fragment_identifier()
                smax_data.append(smax)
    
            #fp = open('Smax_talibanes_' + str(Z) + '_metric_' + str(metric) + '.txt', 'a')
            #fp.write(str(q) + '\t' + str(np.mean(smax_data)) + '\t' + str(np.std(smax_data)) + '\n')
            #fp.close()

            smax_mean.append(np.mean(smax_data))
            smax_std.append(np.std(smax_data))


