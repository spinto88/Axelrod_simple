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

    _fields_ = [('nagents', C.c_int),
                ('agent', C.POINTER(Axl_agent)),
                ('noise', C.c_double)]


    def __init__(self, n, f, q, id_topology = 0.0, noise = 0.00):

        nx.Graph.__init__(self)

        self.nagents = n
        self.id_topology = id_topology
        self.topology_init()
        n = self.nagents

        self.agent = (Axl_agent * n)()
        for i in range(0, n):
            self.agent[i] = Axl_agent(f,q)
            self.node[i] = self.agent[i]
        self.noise = noise
        self.init_net()


    def topology_init(self):

        setop.set_topology(self)


    def init_net(self):
    
        libc.init_net.argtypes = [C.POINTER(Axl_network), C.c_int]        
        libc.init_net(C.byref(self), rand.randint(0, 10000))


    def evolution(self, steps = 1):

        n = self.nagents

        libc.evol_fast.argtypes = [C.POINTER(Axl_network), C.POINTER(Axl_node), C.c_int, C.c_int]

        nodes_info = (Axl_node * n)()
        for i in range(0, n):
            nodes_info[i].degree = self.degree(i)
            nodes_info[i].neighbors = (C.c_int * self.degree(i))(*self.neighbors(i))

        libc.evol_fast(C.byref(self), nodes_info, steps, rand.randint(0, 10000))


    def fragment_identifier(self):
        
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

	n = self.nagents
	
	libc.active_links.argtypes = [Axl_network, C.POINTER(Axl_node)]
	libc.active_links.restype = C.c_int

        nodes_info = (Axl_node * n)()

	for i in range(0, n):
		nodes_info[i].degree = self.degree(i)
		nodes_info[i].neighbors = (C.c_int * self.degree(i))(*self.neighbors(i))

	return libc.active_links(self, nodes_info)


    def evol2convergence(self, check_steps = 100):

	steps = 0
	while self.active_links() != 0:
            self.evolution(check_steps)
            steps += check_steps

	return steps
