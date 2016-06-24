from axelrod_py import *

N = 1024
F = 10
Qz = 100
Z = 10
rand.seed(123458)
A = zealots_list(N,Z)

name = 'Vacunados_phi.txt'

fp = open(name,'a')
fp.write('#Q\tphi\tvacunados\topinion\n')
fp.close()

for Q in range(100,101,80):
    for campo in range(0,50,1):
        phi = float(campo)/10000
        vacunados_data = []
        opinion_data = []
        distribution = []
        
        for configuracion in range(0,100):
        
            vacunados_predata = []
            opinion_predata = []
            
            mysys = Axl_network(n = N, f = F, ff = 0, q = Q, q_z = Qz, A = A, id_topology = 2.1)

            #Segunda etapa
            mysys.evol_opinion = 1  #evolucionar la opinion
            mysys.opinion_included = 1    #incluir la opinion en la homofilia
            mysys.phi = phi

            mysys.evolution(200000)

            #mysys.image_opinion()
            #vaccinated = mysys.vaccinate()
            #mysys.image_vaccinated()
                    
            for i in range(100):
                mysys.evolution(1000)
                vacunados_predata.append(mysys.vaccinate())
                
                opinion = 0
                for j in range(0,N):
                    if(mysys.agent[j].opinion > 50):
                        opinion = opinion + 1
                        
                opinion_predata.append(opinion)
                no_vacunados = mysys.fragment_identifier(type_search = 1)[1]
                
                for item in no_vacunados:
                    distribution.append(item)  

            
            vacunados_data.append(np.mean(vacunados_predata)) 
            opinion_data.append(np.mean(opinion_predata))           
                            
        fp = open(name,'a')
        fp.write(str(Q) + '\t' + str(phi) + '\t' + str(np.mean(vacunados_data)) + '\t' + str(np.mean(opinion_data)) + '\n')
        fp.close() 
        
        name2 = 'distribucion_no_vac_phi' + str(phi) + '_q' + str(Q)
        fp = open(name2,'a')
        for item in distribution:
            fp.write(str(item) + '\n')
        fp.close()            

