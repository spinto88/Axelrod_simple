import numpy as np
import matplotlib.pyplot as plt

#zrange = range(0, 31, 5)
#brange = np.linspace(0.00, 0.09, 10)

zrange = [10]
brange = [0.05]




data = np.loadtxt('Top1.1_Z10_b0.07_Q600.dat')

histo = np.zeros(100)

for i in range(len(data)):
    histo += data[i]

#        plt.clf()
data = plt.hist(range(100), bins = 100, weights = histo, normed = True)
plt.xlabel('First feature')
plt.ylabel('Frequency')
#        plt.title('Z = ' + str(z) + ' b = ' + str(b))
plt.savefig('Z10_b0.07_Q600.eps')
plt.show()
                
