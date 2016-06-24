import numpy as np
import matplotlib.pyplot as plt
import math 

Q=100
phi = 0.05
    
name = 'distribucion_no_vac_phi' + str(phi) + '_q' + str(Q)
name2 = 'distribucion_phi' + str(phi) + '_q' + str(Q) + 'log.eps'
data = np.loadtxt(name)

X = []
Y = []
logX = []
logY = []
fit = []

x,bins,p = plt.hist(data, bins = 1024, normed = True)



#bins = hist[1]
for i in range(0,len(x)):
    if(x[i] != 0):
        X.append(i)
        Y.append(x[i])

            
       
fig = plt.figure()
plt.loglog(X,Y, 'ro',color='b')

plt.xlabel('Cluster size', fontsize=16)
plt.ylabel('Frequency', fontsize=16)
#plt.xlim(0, 10)
#        plt.title('Z = ' + str(z) + ' b = ' + str(b))

plt.savefig(name2)
plt.show()
        
        
        

