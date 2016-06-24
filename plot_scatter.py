from numpy import *
import matplotlib.pyplot as plt

s = 150

data = loadtxt("Vacunados_phi.txt")                
Q,phi,vacunados,opinion = data[:,0], data[:,1], data[:,2], data[:,3] 

fig = plt.figure()
plt.scatter(phi, opinion, c=Q, s=s/3, marker='s',  alpha=.6, edgecolors='none')
plt.xlabel('Phi', fontsize=16)
plt.ylabel('Vacunados', fontsize=16)
#plt.xlim(Q.min()-1, Q.max()+1)
#plt.ylim(phi.min()-0.01, phi.max()+0.01)
plt.title("Cantidad de agentes con Qz > 50. 1024 agentes")
plt.colorbar()
plt.savefig('opinion.jpg')
plt.show()
