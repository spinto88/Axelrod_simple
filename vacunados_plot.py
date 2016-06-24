from matplotlib import pyplot as plt
import pylab
from mpl_toolkits.mplot3d import Axes3D
from numpy import *

s = 300

data = loadtxt("Cluster_topology_Q600b_0.07.txt")    


cluster_size = data[:,0]
no_vaccine = data[:,5]


Z = []
X2 = []
for no_vac in range(1,1023,10):
    name = '/home/rkiman/Documents/my_axelrod/Comparacion_Medus/Data_percolation2_1/Smax' + str(no_vac) + '.dat'
    data_aux = loadtxt(name)
    Z.append(mean(data_aux))
    X2.append(no_vac)
   
plt.semilogy(no_vaccine,cluster_size , 'ro', label="Modelo")
plt.semilogy(X2, Z, 'ro',color='blue', marker='s', label="Percolacion")
plt.xlabel('No vacunados')
plt.ylabel('Tamanio del cluster max')
plt.xlim(0 , 0.02)
#plt.ylim(10 , 1000)
#plt.title("Densidad de clusters de no vacunados q = 300, 10 Talibanes, qz=100")
#fig.colorbar(p)
plt.legend(loc=1)
plt.savefig('no_vacunados_Q600b_0.07.eps')
plt.show()
