from numpy import *
import matplotlib.pyplot as plt

s = 150

data = loadtxt("Vacunados_phi.txt")                
Q,phi,vacunados,opinion = data[:,0], data[:,1], data[:,2], data[:,3] 


X = []
Y = []
Z = []
X1 = []
Y1 = []
Z1 = []

for i in range(0,len(Q)):
    if(Q[i] == 20):
        X.append(phi[i])
        Y.append(vacunados[i])
        Z.append(opinion[i])
    if(Q[i] == 100):
        X1.append(phi[i])
        Y1.append(vacunados[i])
        Z1.append(opinion[i])        

fig = plt.figure()
plt.plot(X1,Y1, 'ro',color='b', label="Vacunados")
plt.xlabel('Phi', fontsize=30)
plt.ylabel('Cantidad de agentes', fontsize=30)# Agentes', fontsize=16)
plt.plot(X1,Z1, 'ro',color='r', label="Qz > 50")
plt.xlabel('Phi', fontsize=30)
plt.ylabel('Cantidad de agentes', fontsize=30)# Agentes', fontsize=16)
plt.xlim(min(X)-0.001, 0.01)#max(X)+0.001)
plt.tick_params(axis='x', labelsize=30)
plt.tick_params(axis='y', labelsize=30)
#plt.ylim(Y.min()-0.01, phi.max()+0.01)
#plt.title("Cantidad de agentes con Qz > 50. 1024 agentes")
plt.grid()
plt.legend(loc = 4,fontsize=30)
plt.savefig('agentes_comparacion.jpg', fontsize=30)
plt.show()
