import os
import ctypes as C
import random as rand

libc = C.CDLL(os.getcwd() + '/axelrod_py/libc.so')


class Axl_agent(C.Structure):
    """
    Axelrod agent: it is caracterized by a cultural vector feat, with f features, which each can adopt q different traits.
    """

    _fields_ = [('f', C.c_int),
		('q', C.c_int),
                ('q_z', C.c_int),
		('fraction', C.c_double),
		('ff', C.c_int),
                ('feat', C.POINTER(C.c_int)),
                ('zealot', C.c_double),
                ('vaccine', C.c_int),
		('degree', C.c_int),
		('label', C.c_int),
		('neighbors', C.POINTER(C.c_int)),
                ('degree_contact', C.c_int),
                ('contact_links', C.POINTER(C.c_int)),
                ('degree_opinion', C.c_int),
		('opinion_links', C.POINTER(C.c_int))]


    def __init__(self, f, q, q_z, fraction, ff):
        """
        Constructor: f number of features, q number of traits per feature, q_z number of traits of the first feature only.
        """
        self.f = f
        self.q = q
        self.q_z = q_z   
        self.fraction = fraction
        self.ff = ff
	self.init_agent()
        self.zealot = 0
        self.vaccine = 0

    def init_agent(self):
        """
	Initialize the agent's state with a random one.
	"""
        self.feat = (C.c_int * self.f)()
        self.feat[0] = rand.randint(0, self.q_z-1)
        	    
        for i in range(1, self.f):
            self.feat[i] = rand.randint(0, self.q-1)
      

    def homophily(self, other):
        """
        This method returns the homophily of an agent respect to other one.
        """
        libc.homophily.argtypes = [Axl_agent, Axl_agent]
        libc.homophily.restype = C.c_double

        return libc.homophily(self, other)
