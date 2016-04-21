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

    def __init__(self, n, f, q, fraction = 0.0, id_topology = 0.0, noise = 0.00, number_of_metric_feats = 0):
        """
        Constructor: initializes the network.Graph first, and set the topology and the agents' states. 
	"""
        nx.Graph.__init__(self)

        self.id_topology = id_topology
        self.topology_init(n)

        self.nagents = self.number_of_nodes()
        
        self.agent = (Axl_agent * self.nagents)()
        self.init_agents(f, q, fraction)

        self.mass_media = Axl_mass_media(f, q)

        self.noise = noise
	self.number_of_metric_feats = number_of_metric_feats


    def topology_init(self, n):
        """
        Initialize the network's topology
        """
        setop.set_topology(self, n)


    def init_agents(self, f, q, fraction):
        """
        Iniatialize the agents' state.
        """
    
        for i in range(0, self.nagents):
            self.agent[i] = Axl_agent(f, q, fraction)
            self.node[i] = self.agent[i]


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


    def fragment_identifier(self):
        """
 	Fragment identifier: it returns the size of the biggest fragment and its state.
        """
        
        n = self.nagents
        libc.fragment_identifier.argtypes = [Axl_network, C.POINTER(Axl_node)]
      
        nodes_info = (Axl_node * n)()

        for i in range(0, n):
            nodes_info[i].degree = self.degree(i)
            nodes_info[i].neighbors = (C.c_int * self.degree(i))(*self.neighbors(i))

        libc.fragment_identifier(self, nodes_info)

        labels = np.zeros(n)
        for i in range(0, n):
            labels[nodes_info[i].label] += 1

        size_max = labels.max()
        index_max = labels.argmax()
        feats = self.agent[index_max].feat[:self.agent[index_max].f]

        return labels.max(), feats

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

    def image(self):

        if self.id_topology < 1.0:

            import matplotlib.pyplot as plt

            if self.agent[0].q > 63:
                print "Q >= 64, the number of colours available is not enough"

            N = self.nagents
            n = int(N ** 0.5)
            matrix = []
            for i in range(0, n):
                row = []
                for j in range(0, n):
                    row.append(self.agent[(j + (i*n))].feat[0])
                matrix.append(row)

            plt.imshow(matrix, interpolation = 'nearest')
            plt.show()

        else:
            print "The system's network is not a square lattice"
            pass
                    
