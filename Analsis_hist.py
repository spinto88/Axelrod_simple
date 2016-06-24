import numpy as np
import matplotlib.pyplot as plt

#zrange = range(0, 31, 5)
#brange = np.linspace(0.00, 0.09, 10)

zrange = [10]
brange = [0.05]




for Q in range(20,101,80):
    for campo in range(0,100,5):
        phi = float(campo)/1000
    
        name = 'distribucion_phi' + str(phi) + '_q' + str(Q)
        name2 = 'distribucion_phi' + str(phi) + '_q' + str(Q) + 'hist.eps'
        data = np.loadtxt(name)

        histo = np.zeros(100)

        for i in range(len(data)):
            histo += data[i]

        #        plt.clf()
        data = plt.hist(data, bins = 100, normed = True)
        plt.xlabel('First feature')
        plt.ylabel('Frequency')
        #plt.xlim(0, 500)
        #        plt.title('Z = ' + str(z) + ' b = ' + str(b))
        plt.savefig(name2)
        plt.show()
                
