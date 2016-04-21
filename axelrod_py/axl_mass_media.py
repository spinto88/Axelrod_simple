import os
import ctypes as C
import random as rand

import axl_agent
import axl_network

libc = C.CDLL(os.getcwd() + '/axelrod_py/libc.so')

class Axl_mass_media(C.Structure):

    _fields_ = [('f', C.c_int),
		('q', C.c_int),
		('feat', C.POINTER(C.c_int)),
                ('b', C.c_double),
                ('strategy', C.c_int),
                ('edit_secc', C.c_int),
                ('edit_line', C.c_int)]


    def __init__(self, f, q, b = 0.00, strategy = 0, edit_secc = 0, edit_line = 0):
        self.f = f
        self.q = q
        self.feat = (C.c_int * f)()
        self.b = b
        self.strategy = strategy
        self.edit_secc = edit_secc
        self.edit_line = edit_line
        self.init_agent()


    def init_agent(self):
        for i in range(0,self.f):
            self.feat[i] = rand.randint(0, self.q-1)
        self.feat[self.edit_secc] = self.edit_line

    def set_edit_line(self, new_edit_line):
        
        self.feat[self.edit_secc] = new_edit_line
        self.edit_line = new_edit_line

    def homophily(self, other):

        libc.homophily_mm.argtypes = [Axl_mass_media, axl_agent.Axl_agent]
        libc.homophily_mm.restype = C.c_double

        return libc.homophily_mm(self, other)

    def adaptation(self, axl_net):

        libc.adaptation.argtypes = [C.POINTER(Axl_mass_media), axl_network.Axl_network, C.c_int]
        libc.adaptation.restype = C.c_int
   
        changes = 0 
        if self.strategy != 0:    
            for feat2change in range(0, self.f):
                changes += libc.adaptation(C.byref(self), axl_net, feat2change)
            self.feat[self.edit_secc] = self.edit_line    

        else:
            pass

        return changes

    def followers(self, axl_net):

        libc.followers_counter.argtypes = [Axl_mass_media, axl_network.Axl_network]
        libc.followers_counter.restype = C.c_int

        followers = libc.followers_counter(self, axl_net)

	return float(followers)/axl_net.nagents


    def mean_homophily_mm(self, axl_net):

        libc.mean_homophily_mm.argtypes = [Axl_mass_media, axl_network.Axl_network]
        libc.mean_homophily_mm.restype = C.c_double

        return libc.mean_homophily_mm(self, axl_net)

    def mean_homophily_followers(self, axl_net):
       
        libc.mean_homophily_followers.argtypes = [Axl_mass_media, axl_network.Axl_network]
        libc.mean_homophily_followers.restype = C.c_double

        return libc.mean_homophily_followers(self, axl_net)

