
from axelrod_py import *

N = 1024
F = 10
topology = 0.1
fraction = 1
q_z = 100
metric = 1

for Bmf2 in range(0,50,60):
    Bmf = float(Bmf2)/100  
    metric_features = metric

    for Z in range(0,1,10):    
    
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

        qrange = range(10, 40, 50)

        for q in qrange:

            Adherents = []
            adherents_data = []
                        
            for conf in range(0, Number_of_configurations):

                mysys = Axl_network(N, F, q, q_z, b= Bmf, A = A, fraction = fraction, id_topology = topology)

                mysys.number_of_metric_feats = metric_features

                mysys.mass_media.b = B1
                mysys.mass_media.strategy = strategy
                               
                mysys.evolution_mf(20000)
                          
                Adherents = mysys.adherents_distribution(q_z)
                
                for item in Adherents:
                    adherents_data[item].append(item[1])
                
                
            fp = open('Adherentes_q_' + str(q) + '.txt', 'a')
            for item in Adherents:
                fp.write(str(item[0]) + '\t' + str(np.mean(item[1])) + '\n')
            fp.close()
                 
                # Fragmento mas grande y estado



