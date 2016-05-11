import os
import ctypes as C
import networkx as nx
import random as rand
import numpy as np
import set_topology as setop
from axl_node import *
from axl_agent import *
from axl_mass_media import *


libc = C.CDLL(os.getcwd() + '/axelrod_py/libc.so')


class Axl_network(nx.Graph, C.Structure):

    """
    Axelrod network: it has nagents axelrod agents, and an amount of noise in the dynamics of the system. This class inherites from the networkx.Graph the way to be described.
    """

    _fields_ = [('nagents', C.c_int),
                ('agent', C.POINTER(Axl_agent)),
                ('noise', C.c_double),
		('number_of_metric_feats', C.c_int),
		('mass_media', Axl_mass_media),
		('b', C.c_double)]

    def __init__(self, n, f, q, q_z = 100, b = 0.0, A = [], fraction = 1.0, id_topology = 0.0, noise = 0.00, number_of_metric_feats = 0):

        """
        Constructor: initializes the network.Graph first, and set the topology and the agents' states. 
	"""
        nx.Graph.__init__(self)

        self.id_topology = id_topology
        self.topology_init(n)

        self.nagents = self.number_of_nodes()
        
        self.agent = (Axl_agent * self.nagents)()
        self.init_agents(f, q, q_z, A, fraction)

        self.mass_media = Axl_mass_media(f, q)

        self.noise = noise
	self.number_of_metric_feats = number_of_metric_feats
	self.b = b


    def topology_init(self, n):
        """
        Initialize the network's topology
        """
        setop.set_topology(self, n)


    def init_agents(self, f, q, q_z, A, fraction):
        """
        Iniatialize the agents' state.
        """
    
        for i in range(0, self.nagents):
            self.agent[i] = Axl_agent(f, q, q_z, fraction)
            if i in A:
                self.agent[i].zealot = 1
                self.agent[i].feat[0] = q_z-1
            
            self.node[i] = self.agent[i]
            
    def adherents_counter(self):
        """
        Gives number of agents with the same q for the first feature, only for the q_z given
        """
        libc.adherents_counter.argtypes = [Axl_network, C.c_int]
        libc.adherents_counter.restype = C.c_int

        q_z = self.agent[0].q_z
        
        # The adherents have a q equal to qz-1
        adherents = libc.adherents_counter(self, q_z-1)
        adherents = float(adherents)/self.nagents
        
        return adherents
    
    def adherents_distribution(self):
        """
        Gives a number of agents with the same q for the first feature, for all q
        """
        libc.adherents_counter.argtypes = [Axl_network, C.c_int]
        libc.adherents_counter.restype = C.c_int
        
        q_z = self.agent[0].q_z
        adherents = np.zeros(q_z)
        
        for q in range(0, q_z):
            adherents_q = libc.adherents_counter(self, q)
            adherents[q] = float(adherents_q)/self.nagents

        average = np.average(range(0, q_z), weights = adherents)
        desviation = 0
        for q in range(0, q_z):
            desviation += abs(average - q) * adherents[q]

        return adherents, average, desviation

    def adherents_hist(self, fname = ''):
        
        adherents = self.adherents_distribution()[0]
        q_z = self.agent[0].q_z

        import matplotlib.pyplot as plt

        figure = plt.figure(1)
        figure.clf()

        plt.hist(range(0, q_z), bins = q_z, weights = adherents, normed = True)
        plt.axis([-0.5, q_z-0.5, 0, 1.00])
        plt.xlabel('Q value of the first feature')
        plt.ylabel('Normalized histogram')
        if fname == '':
            plt.show()
        else:
	    plt.savefig(fname)
    
    def vaccinated_counter(self):
        """
        Gives number of agents that deacided to be vaccinated
        """
        vaccinated = 0
        
        for i in range(0, self.nagents):
            if (self.agent[i].vaccine == 1):
                vaccinated = vaccinated + 1 
        
        return vaccinated    
        
    def vaccinate(self):
        """
        Takes the network and decides randomly who gets the vaccine and who does not, depending on the value of the first feature of each agent
        """
        q_z = self.agent[0].q_z 
        
        for i in range(0,self.nagents):
        
            aux = rand.randint(0, q_z-1)
            
            if(aux < self.agent[i].feat[0]):
                # 0 means that the agent is not vaccinated
                self.agent[i].vaccine = 0
            else:
                self.agent[i].vaccine = 1


    def evolution(self, steps = 1):
        """
	Make steps synchronius evolutions of the system
        """

        n = self.nagents

        nodes_info = (Axl_node * n)()
        for i in range(0, n):
            nodes_info[i].degree = self.degree(i)
            nodes_info[i].neighbors = (C.c_int * self.degree(i))(*self.neighbors(i))

        libc.evol_fast.argtypes = [C.POINTER(Axl_network), C.POINTER(Axl_node), C.c_int, C.c_int]

        libc.evol_fast(C.byref(self), nodes_info, steps, rand.randint(0, 10000))


    def fragment_identifier(self, clustering_radio = 0):
        """
 	Fragment identifier: it returns the size of the biggest fragment, its state, 
	and the cluster distribution.
        It sees if the agents are neighbors and have the first feature less or equal
	than the clustering radio.
        """
       
        n = self.nagents
        libc.fragment_identifier.argtypes = [Axl_network, C.POINTER(Axl_node), C.c_int]
      
        nodes_info = (Axl_node * n)()

        # Neighbors list built
        for i in range(0, n):
            nodes_info[i].degree = self.degree(i)
            nodes_info[i].neighbors = (C.c_int * self.degree(i))(*self.neighbors(i))

	# This function puts in nodes_info[i].label the label of the node i, according to 
	# the current criteria of identifing 
        libc.fragment_identifier(self, nodes_info, clustering_radio)

        # After this, the vector labels has the label of each agent
        labels = np.zeros(n)
        for i in range(0, n):
            labels[nodes_info[i].label] += 1
        
        # Size_max is the size of the biggest fragment
        size_max = labels.max()
	# Index_max the label of the biggest fragment
        index_max = labels.argmax()

        # feat0_distribution returns a dictionary with all clusters in the system, 
	# its first feature and size
        feat0_distribution = []
        feat0_distribution_size = []
        for i in range(0, len(labels)):
            if labels[i] != 0:
                feat0_distribution.append({'First feature': self.agent[i].feat[0], 'Size': labels[i]})
                feat0_distribution_size.append(labels[i])

        if clustering_radio == 0:
            # feat is the first feature of the biggest fragment
            feat = self.agent[index_max].feat[0]
            return size_max#, feat, feat0_distribution

	else:
            # Size of the biggest fragment and size distribution
	    return size_max#, feat0_distribution_size
        

    def active_links(self):

        """
	Active links: it returns True if there are active links in the system.
        """

	n = self.nagents
	
	libc.active_links.argtypes = [Axl_network, C.POINTER(Axl_node)]
	libc.active_links.restype = C.c_int

        nodes_info = (Axl_node * n)()

	for i in range(0, n):
		nodes_info[i].degree = self.degree(i)
		nodes_info[i].neighbors = (C.c_int * self.degree(i))(*self.neighbors(i))

	return libc.active_links(self, nodes_info)


    def evol2convergence(self, check_steps = 100):
        """ 
	Evolution to convergence: the system evolves until there is no active links, checking this by check_steps. Noise must be equal to zero.
        """
        if self.noise > 0.00:
            print "Convergence cannot be reach with noise in the system"
  
        else:
   	    steps = 0
    	    while self.active_links() != 0:
                self.evolution(check_steps)
                
                steps += check_steps

	    return steps

    
    def evol2stationary(self, check_steps = 250, epsilon = 0.05):
        """
        This function manages the system to a stationary state, where 
        the average value of the adherents and the width of the distribution
        remains almost constant
        """

        average_aux = 0
        desviation_aux = 0
        stationary = 0
        steps = 0

        while stationary != 1:

            data2average = []
            data2average_desv = []
            for i in range(0, 40):
                self.evolution(check_steps)
                steps += check_steps
                data2average.append(self.adherents_distribution()[1])
                data2average_desv.append(self.adherents_distribution()[2])

            average_new = np.mean(data2average)
            desviation_new = np.mean(data2average_desv)

            distance = abs(average_new - average_aux)
            distance2 = abs(desviation_new - desviation_aux)

            print distance, distance2

            if distance < epsilon and distance2 < epsilon:
                stationary = 1
            else:
                average_aux = average_new
                desviation_aux = desviation_new
            
        return steps
    

    def image_opinion(self, fname = ''):
        """
        This method prints on screen the matrix of first features, of course the system is a square lattice.
        It is not confident if q is larger than 63.
        If fname is different of the null string, the matrix is save in a file with that name. This one can be loaded by numpy.loadtxt(fname).
        """
        if self.id_topology < 1.0:

            import matplotlib.pyplot as plt

            N = self.nagents
            n = int(N ** 0.5)
            q_z = self.agent[0].q_z
            matrix = []
            for i in range(0, n):
                row = []
                for j in range(0, n):
                    row.append(self.agent[(j + (i*n))].feat[0])
                matrix.append(row)

            if fname != '':
                np.savetxt(fname + '.txt', matrix)

            figure = plt.figure(1)
            figure.clf()
            plt.imshow(matrix, interpolation = 'nearest', vmin = 0, vmax = q_z)
            plt.colorbar()
            if fname != '':
                plt.savefig(fname + '.png')
            else:
                plt.show()

        else:
            print "The system's network is not a square lattice"
            pass
            
    def image_vaccinated(self, fname = ''):
        """
        This method prints on screen the matrix of vaccinated agents, of course the system is a square lattice.
        It is not confident if q is larger than 63.
        If fname is different of the null string, the matrix is save in a file with that name. This one can be loaded by numpy.loadtxt(fname).
        """
        if self.id_topology < 1.0:

            import matplotlib.pyplot as plt
            from matplotlib import colors

            N = self.nagents
            n = int(N ** 0.5)
            q_z = self.agent[0].q_z
            matrix = []
            for i in range(0, n):
                row = []
                for j in range(0, n):
                    row.append(self.agent[(j + (i*n))].vaccine)
                matrix.append(row)

            if fname != '':
                np.savetxt(fname + '.txt', matrix)

            cmap = colors.ListedColormap(['red', 'green'])
            bounds=[0,0.1,1]
            norm = colors.BoundaryNorm(bounds, cmap.N)

            figure = plt.figure(1)
            figure.clf()
            plt.imshow(matrix, interpolation='nearest', origin='lower',cmap=cmap, norm=norm)
            plt.colorbar(cmap=cmap, norm=norm, boundaries=bounds, ticks=[0, 1])
            if fname != '':
                plt.savefig(fname + '.png')
            else:
                plt.show()

        else:
            print "The system's network is not a square lattice"
            pass
              

    def effective_q(self):
        """
        Print a vector with the number of actual q's per feature.
        For example, if all the system share the same state, the 
        effective_q vector = [1, 1, ..., 1] of dimension f.
        """

        n = self.nagents
        f = self.agent[0].f

        effective_q = []

        for i in range(0, f):

            q_list = []
            for j in range(0, n):
                q_list.append(self.agent[j].feat[i])

            aux = set(q_list)
            effective_q.append(len(aux))

        return effective_q

