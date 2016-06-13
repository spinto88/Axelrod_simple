
from axelrod_py import *

N = 1024
F = 10
Q = 20

rand.seed(123457)

mysys = Axl_network(N, F, Q)

mysys.set_topology(id_topology = 3.1)

for number_of_no_vaccine in range(N):

    fname = 'Distribution' + str(number_of_no_vaccine) + '.dat'
    fname2 = 'Smax' + str(number_of_no_vaccine) + '.dat'

    for conf in range(1000):

        for i in range(N):
            mysys.agent[i].vaccine = 1

        no_vaccine = rand.sample(range(N), number_of_no_vaccine)

        for i in no_vaccine:
            mysys.agent[i].vaccine = 0

        data = mysys.fragment_identifier(type_search = 1)

        distribution = data[0]
        smax = data[1]

        fp = open(fname, 'a')
        for i in distribution:
            if i[0] == 0:
                fp.write(str(i[1]) + '\n')
        fp.close()
        
        fp = open(fname2, 'a')
        fp.write(str(smax) + '\n')
        fp.close()

