import numpy as np
import matplotlib.pyplot as plt

colours=['r','g','m']
i = 0
for Q in range(10,100,30):
    name = 'distribution_axelrod' + str(Q) + '.txt'
    all_data = np.loadtxt(name)
    
    data = plt.hist(all_data, bins = 1024, normed = True)
    Z = data[0]

    X = range(0,len(Z)) 
    
    label = str(Q)
    
    plt.plot(X, Z, 'ro', color = colours[i], label=label)
    plt.xlabel('Q')
    plt.ylabel('Distribucion de Clusters')
    plt.xlim(0 , 200)
    plt.ylim(0 , 1)
    #plt.title("Densidad de clusters de no vacunados q = 600, 10 Talibanes, qz=100")
    #fig.colorbar(p)
    i = i + 1
plt.legend(loc=1)
plt.savefig('distribucion_axelrod.eps')
plt.show()
