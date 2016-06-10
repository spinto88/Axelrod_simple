from matplotlib import pyplot as plt
import pylab
from mpl_toolkits.mplot3d import Axes3D
from numpy import *

s = 300

data = loadtxt("Cluster_topology_Q300b_0.02_cutoff90.txt")    
cluster,C,l,k,mod = data[:,0], data[:,1], data[:,2], data[:,3], data[:,4]

X = cluster

data2 = loadtxt("Cluster_topology_percolacion.txt")    
cluster2,C2,l2,k2,mod2 = data2[:,0], data2[:,1], data2[:,2], data2[:,3], data2[:,4]

X2 = cluster2 


plt.subplot(221)
plt.plot(X,C, 'ro',color='b', label="Modelo")
plt.plot(X2,C2, 's',color='r', label="Percolacion")
plt.xlabel('Cluster maximo', size = 15)
plt.xlim(0,200)
plt.ylabel('Coeficiente de clusterizacion', size = 15)
plt.tick_params(axis='x', labelsize=15)
plt.tick_params(axis='y', labelsize=15)
plt.legend(loc = 4)

plt.subplot(223)
plt.plot(X,l, 'ro',color='b', label="Modelo")
plt.plot(X2,l2, 's',color='r', label="Percolacion")
plt.xlabel('Cluster maximo', size = 15)
plt.xlim(0,200)
plt.ylabel('Distancia media', size = 15)
plt.tick_params(axis='x', labelsize=15)
plt.tick_params(axis='y', labelsize=15)
plt.legend(loc = 4)

plt.subplot(222)
plt.plot(X,k, 'ro',color='b', label="Modelo")
plt.plot(X2,k2, 's',color='r', label="Percolacion")
plt.xlabel('Cluster maximo', size = 15)
plt.xlim(0,200)
plt.ylabel('Grado Medio', size = 15)
plt.tick_params(axis='x', labelsize=15)
plt.tick_params(axis='y', labelsize=15)
plt.legend(loc = 4)

plt.subplot(224)
plt.plot(X,mod, 'ro',color='b', label="Modelo")
plt.plot(X2,mod2, 's',color='r', label="Percolacion")
plt.xlabel('Cluster maximo', size = 15)
plt.xlim(0,200)
plt.ylabel('Modularidad', size = 15)
plt.tick_params(axis='x', labelsize=15)
plt.tick_params(axis='y', labelsize=15)
plt.legend(loc = 4)

plt.savefig('cluster_topology_Q300b_0.02_cutoff90.eps')
plt.show()
