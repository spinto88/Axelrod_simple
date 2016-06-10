from matplotlib import pyplot as plt
import pylab
from mpl_toolkits.mplot3d import Axes3D
from numpy import *

s = 300

data = loadtxt("distribution_Q600b_0.07.txt")    

cluster_size = data

cluster_size_Y = plt.hist(cluster_size, bins = 1024, normed = True)
Y = cluster_size_Y[0]

X = range(0,len(Y)) 

all_data = []

for no_vac in range(1,1023,10):
    name = '/home/rkiman/Documents/my_axelrod/Comparacion_Medus/Data_percolation2_1/Distribution' + str(no_vac) + '.dat'
    data_aux = loadtxt(name)
    for item in data_aux:
        all_data.append(item) 

data = plt.hist(all_data, bins = 1024, normed = True)
Z = data[0]

X2 = range(0,len(Z))  
   
plt.loglog(X, Y, 'ro', label="Modelo")
plt.loglog(X2, Z, 'ro',color='blue', marker='s', label="Percolacion")
plt.xlabel('Tamanio del cluster de no vacunados')
plt.ylabel('Densidad')
plt.xlim(0 , 1100)
#plt.ylim(10 , 1000)
plt.title("Densidad de clusters de no vacunados q = 600, 10 Talibanes, qz=100")
#fig.colorbar(p)
plt.legend(loc=1)
plt.savefig('densidad_Q600b_0.07.eps')
plt.show()
