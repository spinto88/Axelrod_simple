import os
import ctypes as C
import networkx as nx
import random as rand
import numpy as np
import set_topology as setop
from axl_node import *
from axl_agent import *


libc = C.CDLL(os.getcwd() + '/axelrod_py/libc.so')


class Axl_network(nx.Graph, C.Structure):

    """
    Axelrod network: it has nagents axelrod agents, and an amount of noise in the dynamics of the system. This class inherites from the networkx.Graph the way to be described.
    """

    _fields_ = [('nagents', C.c_int),
                ('agent', C.POINTER(Axl_agent)),
                ('noise', C.c_double)]

    def __init__(self, n, f, q, id_topology = 0.0, noise = 0.00):
        """
        Constructor: initializes the network.Graph first, and set the topology and the agents' states. 
	"""
        nx.Graph.__init__(self)

        self.id_topology = id_topology
        self.topology_init(n)

        self.nagents = self.number_of_nodes()
        
        self.agent = (Axl_agent * self.nagents)()
        self.init_agents(f, q)

        self.noise = noise

    def topology_init(self, n):
        """
        Initialize the network's topology
        """
        am = setop.set_topology(self, n)

        self.adjacency_matrix = am


    def init_agents(self, f, q):
        """
        Iniatialize the agents' state.
        """
    
        for i in range(self.nagents):
            self.agent[i] = Axl_agent(f, q)

        nodes_info = (Axl_node * self.nagents)()
        for i in range(self.nagents):
            nodes_info[i].degree = self.degree(i)
            nodes_info[i].neighbors = (C.c_int * self.degree(i))(*self.neighbors(i))

	self.nodes_info = nodes_info

    def evolution(self, steps = 1, evol_type = 'syncro'):
        """
	Make steps synchronius evolutions of the system
        """

        n = self.nagents

        libc.evol_fast.argtypes = [C.POINTER(Axl_network), C.POINTER(Axl_node), C.c_int, C.c_int, C.c_int]

        if evol_type == 'syncro':
	    et = 1 

        libc.evol_fast(C.byref(self), self.nodes_info, et, steps, rand.randint(0, 10000))


    def fragment_identifier(self):
        """
 	Fragment identifier: it returns the size of the biggest fragment and its state.
        """
        
        n = self.nagents
        libc.fragment_identifier.argtypes = [Axl_network, C.POINTER(Axl_node)]
      
        libc.fragment_identifier(self, self.nodes_info)

        labels = np.zeros(n)
        for i in range(0, n):
            labels[self.nodes_info[i].label] += 1

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

	return libc.active_links(self, self.nodes_info)

    def corr_matrix(self):

        cm = np.zeros([self.nagents, self.nagents], dtype = np.float)

        for i in range(self.nagents):
            for j in range(i+1, self.nagents):
                cm[i][j] = self.agent[i].homophily(self.agent[j])

        cm += cm.T
        for i in range(self.nagents):
            cm[i][i] = 1.00

        return cm


    def evol2convergence(self, check_steps = 100, evol_type = 'syncro'):
        """ 
	Evolution to convergence: the system evolves until there is no active links, checking this by check_steps. Noise must be equal to zero.
        """
        if self.noise > 0.00:
            print "Convergence cannot be reach with noise in the system"
  
        else:
   	    steps = 0
    	    while self.active_links() != 0:
                self.evolution(check_steps, evol_type)
                steps += check_steps

	    return steps

    def one_step_evol(self, i, j):
        """
	Make one asynchronius step
        """

        if j in list(self.neighbors(i)):
            libc.evolution_asyncro.argtypes = [C.POINTER(Axl_network), C.c_int, C.c_int, C.c_int]

	    libc.evolution_asyncro(C.byref(self), i, j, rand.randint(0, 10000))
