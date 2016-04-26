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
		('mass_media', Axl_mass_media)]

    def __init__(self, n, f, q, q_z, A = [], fraction = 0.0, id_topology = 0.0, noise = 0.00, number_of_metric_feats = 0):

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
        Counts the number of agents that have the same first feature q_z
        """
        libc.adherents_counter.argtypes = [Axl_network]
        libc.adherents_counter.restype = C.c_int
        
        adherents = libc.adherents_counter(self)
        adherents = float(adherents)/self.nagents
        
        return adherents

    def evolution(self, steps = 1):
        """
	Make steps synchronius evolutions of the system
        """

        n = self.nagents

        libc.evol_fast.argtypes = [C.POINTER(Axl_network), C.POINTER(Axl_node), C.c_int, C.c_int]

        nodes_info = (Axl_node * n)()
        for i in range(0, n):
            nodes_info[i].degree = self.degree(i)
            nodes_info[i].neighbors = (C.c_int * self.degree(i))(*self.neighbors(i))

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
            return size_max, feat, feat0_distribution

	else:
            # Size of the biggest fragment and size distribution
	    return size_max, feat0_distribution_size
        

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

    def image(self, fname = ''):
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
            plt.savefig(fname + '.eps')

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

