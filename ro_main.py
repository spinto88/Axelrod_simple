
from axelrod_py import *

N = 1024
F = 10
topology = 3.1
fraction = 1
q_z = 100
metric = 0
Bmf = 0.01
metric_features = metric
Z = 10

rand.seed(123413)

A = zealots_list(N,Z)

B1 = 0.00

# Strategia del campo externo (0 es medio masivo constante en el tiempo)
strategy = 0

fp = open('Smax.txt','a')
fp.write('#q\tsmax\tno_vaccinated\n')
fp.close()

Number_of_configurations = 10

q = 300

smax_data = []
vaccinated_data = []

for mf in range(0, Number_of_configurations):

	mysys = Axl_network(N, F, q, q_z, b= Bmf, A = A, fraction = fraction, id_topology = topology)

    mysys.number_of_metric_feats = metric_features

    mysys.mass_media.b = B1
    mysys.mass_media.strategy = strategy
    
    set_initial_state_equal(feature = 0)
    
    mysys.evol2convergence()

    mysys.vaccinate()

    vaccinated = 1024 - mysys.vaccinated_counter()  
    
    vaccinated_data.append(vaccinated)
    
    mysys.set_topology(id_topology = 2.1)
    # Fragmento mas grande y estado
    smax = mysys.fragment_identifier(type_search = 10)
    smax_data.append(smax)
    
               
fp = open('Smax.txt','a')
fp.write(str(q) + '\t' + str(np.mean(smax_data)) + '\t' + str(np.mean(vaccinated_data)) + '\n')
fp.close()

                


