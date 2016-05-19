
from axelrod_py import *

N = 1024
F = 10
topology = 0.1
fraction = 1
q_z = 100
metric = 1

for Bmf2 in range(0,50,5):
    Bmf = float(Bmf2)/1000  
    metric_features = metric

    for Z in range(0,35,2):    
    
        rand.seed(123413)

        A = zealots_list(N,Z)

        B1 = 0.00
        #Bmf = 0.5
        # Strategia del campo externo (0 es medio masivo constante en el tiempo)
        strategy = 0

        fp = open('Distribucion_q_20.txt', 'a')
        fp.write('#Z\tmf\tdistribucion\tvaccinated\n')
        fp.close()

        Number_of_configurations = 50

        qrange = range(20, 30, 15)

        for q in qrange:

            vaccinated_data = []
            size_data = []
            
            for conf in range(0, Number_of_configurations):

                mysys = Axl_network(n = N, f = F, q = q, q_z = q_z, b = Bmf, A = A, number_of_metric_feats = 1, id_topology = 1.1)

                mysys.mode_mf = 1
                mysys.mass_media.b = B1
                mysys.mass_media.strategy = strategy

                mysys.evol2stationary()[1]
                
                mysys.vaccinate()

                vaccinated = mysys.vaccinated_counter()  
                vaccinated_data.append(vaccinated)
                
                fragments_data = fragment_identifier(clustering_radio = 10)[2]
                
                for item in fragments_data:
                    if(item[0]==0):
                        size_data.append(item[1])
                
                max_size_data.append(np.max(size_data))
                           
                                   
            fp = open('Adherentes_Smax_q_20.txt', 'a')
            fp.write(str(Z) + '\t' + str(Bmf) + '\t' + str(np.mean(average_data)) + '\t' + str(np.mean(vaccinated_data)) + '\n')
            fp.close()

                #smax_mean.append(np.mean(smax_data))
                #smax_std.append(np.std(smax_data))


