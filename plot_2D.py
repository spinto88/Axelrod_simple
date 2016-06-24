from numpy import *
import matplotlib.pyplot as plt

s = 150

data = loadtxt("Inc_Vacunados_phi.txt")                

X = []
Y = []
Z = []
X1 = []
Y1 = []
Z1 = []

Q = []
phi = []
vacunados = []
opinion = []
smax = []

for Q2 in [20,120]:
    for campo in range(0,40):
        phi2 = float(campo)/10000
        vacunados_data = []
        opinion_data = []
        smax_data = []
        for i in range(0,len(data[:,0])):
            if(data[i,0] == Q2 and data[i,1] == phi2):
                vacunados_data.append(data[i,2])
                opinion_data.append(data[i,4])
                smax_data.append(data[i,6])
        Q.append(Q2)
        phi.append(phi2)
        vacunados.append(mean(vacunados_data))
        opinion.append(mean(opinion_data))
        smax.append(mean(smax_data))                    
            
for i in range(0,len(Q)):
    if(Q[i] == 20):
        X.append(phi[i])
        Y.append(vacunados[i])
        Z.append(opinion[i])
    if(Q[i] == 120):
        X1.append(phi[i])
        Y1.append(vacunados[i])
        Z1.append(opinion[i])        

fig = plt.figure()
plt.plot(X,Y, 'ro',color='b', label="Q=20")
plt.xlabel('Phi', fontsize=16)
plt.ylabel('Cantidad de opinion', fontsize=16)# Agentes', fontsize=16)
plt.plot(X1,Y1, 'ro',color='r', label="Q=100")
plt.xlabel('Phi', fontsize=16)
plt.ylabel('Cantidad de vacunados', fontsize=16)# Agentes', fontsize=16)
plt.xlim(min(X)-0.001, max(X)+0.001)
#plt.ylim(Y.min()-0.01, phi.max()+0.01)
#plt.title("Cantidad de agentes con Qz > 50. 1024 agentes")
plt.legend(loc = 4)
#plt.savefig('vacunados_zoom.jpg')
plt.show()
