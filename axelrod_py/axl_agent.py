import os
import ctypes as C
import random as rand

libc = C.CDLL(os.getcwd() + '/axelrod_py/libc.so')


class Axl_agent(C.Structure):
    """
    Axelrod agent: it is caracterized by f features, which can adopt q traits.
    """
    _fields_ = [('f', C.c_int),
		('q', C.c_int),
                ('feat', C.POINTER(C.c_int))]

    def __init__(self, f, q):
        """
        Constructor: f number of features, q number of traits per feature.
        """
        self.f = f
        self.q = q
        self.feat = (C.c_int * f)()
        self.init_agent()

    def init_agent(self):
        for i in range(0, self.f):
            self.feat[i] = rand.randint(0, self.q-1)

    def homophily(self, other):
        """
        This method returns the homophily of an agent respect to other one.
        """
        libc.homophily.argtypes = [Axl_agent, Axl_agent]
        libc.homophily.restype = C.c_double

        return libc.homophily(self, other)
