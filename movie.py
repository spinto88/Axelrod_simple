from axelrod_py import *

N = 1024
F = 10
Q = 70
Qz = 100
Z = 10
rand.seed(123458)
A = zealots_list(N,Z)


mysys = Axl_network(n = N, f = F, q = Q, q_z = Qz, A = A, number_of_metric_feats = 1, id_topology = 2.1)

mysys.phi = 0.0000

mysys.set_zealots(A,type_z = 1)





#mysys.evol2convergence()



mysys.evolution(10000) 

mysys.image_opinion()
mysys.vaccinate()
mysys.image_vaccinated()

    #mysys.image_opinion()
    #mysys.vaccinate()
    #mysys.image_vaccinated()

    #print mysys.agent[1].feat[:F]
    
    #for j in range(0,mysys.agent[1].degree):
    #    print mysys.agent[mysys.agent[1].neighbors[j]].feat[:F]
    #print 

#for i in range(0,10):   
#    mysys.evolution(100) 
#    mysys.image_opinion()
#    mysys.vaccinate()
#    mysys.image_vaccinated()

mysys.set_zealots(A,type_z = 1)  


print 'listo1'
      
mysys.phi = 0.005

for i in range(0,N):
    mysys.agent[i].ff = 4
#mysys.evolution(60000)
mysys.fragment_identifier(type_search = 10) 

#mysys.evolution(88000)

for i in range(0,1000):
    print str(i)
    mysys.evolution(100)
    
    #name1 = "opinion" + str(i) 
    #name2 = "vaccinated" + str(i) 
    mysys.image_opinion()
    mysys.vaccinate()
    mysys.image_vaccinated()
    
    print mysys.fragment_identifier(type_search = 10)
    
    for item in A:
        print mysys.agent[item].feat[:F]      
        
