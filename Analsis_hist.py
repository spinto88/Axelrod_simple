import numpy as np
import matplotlib.pyplot as plt
import math 

for Q in range(20,101,80):
    for campo in range(5,100,5):
        phi = float(campo)/1000
    
        name = 'distribucion_phi' + str(phi) + '_q' + str(Q)
        name2 = 'distribucion_phi' + str(phi) + '_q' + str(Q) + 'log.eps'
        data = np.loadtxt(name)

        X = []
        Y = []
        logX = []
        logY = []
        fit = []
        
        x,bins,p = plt.hist(data, bins = 1024, normed = True)

        for item in p:
            item.set_height(item.get_height()/sum(x))

        
        #bins = hist[1]
        for i in range(0,400):
            if(x[i] != 0):
                X.append(i)
                Y.append(x[i])

                    
        for i in range(1,len(Y)):
            logX.append(math.log(X[i]))
            logY.append(math.log(Y[i]))
           
        a ,b = np.polyfit(logX, logY, 1, rcond=None, full=False, w=None, cov=False)        
        
        for item in logX:
            fit.append(b + a*item)
                
        fig = plt.figure()
        plt.plot(logX,logY, 'ro-',color='b')
        plt.plot(logX,fit,'-',color='r')
        #plt.hist(data, bins = 100, normed = True)
        plt.xlabel('Tamanio del Cluster', fontsize=16)
        plt.ylabel('Frequency', fontsize=16)
        #plt.xlim(0, 10)
        #        plt.title('Z = ' + str(z) + ' b = ' + str(b))

        plt.savefig(name2)
        #plt.show()
                
                
                
      
