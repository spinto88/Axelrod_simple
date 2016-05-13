
from axelrod_py import *

N = 1024
F = 10
topology = 0.1
fraction = 1
q_z = 100
metric = 1

for Bmf2 in range(0,50,20):
    Bmf = float(Bmf2)/100  
    metric_features = metric

    for Z in range(0,35,10):    
    
        rand.seed(123413)

        A = zealots_list(N,Z)

        B1 = 0.00
        #Bmf = 0.5
        # Strategia del campo externo (0 es medio masivo constante en el tiempo)
        strategy = 0

        fp = open('Adherentes_Smax_mf_' + str(Bmf) + '_Z_' + str(Z) + '.txt', 'a')
        fp.write('#q\tsmax\tstd\tadherents\tstd\tvaccinated\tstd\n')
        fp.close()

        Number_of_configurations = 50

        smax_mean = []
        smax_std = []

        qrange = range(10, 100, 5)

        for q in qrange:

            smax_data = []
            adherents_data = []
            vaccinated_data = []

            for conf in range(0, Number_of_configurations):

                mysys = Axl_network(N, F, q, q_z, b= Bmf, A = A, fraction = fraction, id_topology = topology)

                mysys.number_of_metric_feats = metric_features

                mysys.mass_media.b = B1
                mysys.mass_media.strategy = strategy
                # mysys.evol2convergence()

                # En vez de converger le digo cuantos pasos correr

                #for steps in range(0,50):
                    #mysys.vaccinate()                    
                    #mysys.image_opinion('network_opinion_step_' + str(steps) + '_q_' + str(q) + '_Z_' + str(Z) + '_mf_' + str(Bmf))
                    #mysys.image_vaccinated('network_vaccinated_step_'+ str(steps) + '_q_' + str(q) + '_Z_' + str(Z) + '_mf_' + str(Bmf))

                mysys.evolution_mf(20000)
                
                mysys.vaccinate()

                vaccinated = mysys.vaccinated_counter()  
                vaccinated_data.append(vaccinated)
                
                adherents = mysys.adherents_counter(1)  # da los agentes con primer feature (x-1)
                adherents_data.append(adherents)
                 
                # Fragmento mas grande y estado
                smax = mysys.fragment_identifier()
                smax_data.append(smax)
               
            fp = open('Adherentes_Smax_mf_' + str(Bmf) + '_Z_' + str(Z) + '.txt', 'a')
            fp.write(str(q) + '\t' + str(np.mean(smax_data)) + '\t' + str(np.std(smax_data)) + '\t' + str(np.mean(adherents_data)) + '\t' + str(np.std(adherents_data)) + '\t' + str(np.mean(vaccinated_data)) + '\t' + str(np.std(vaccinated_data)) + '\n')
            fp.close()

                #smax_mean.append(np.mean(smax_data))
                #smax_std.append(np.std(smax_data))


