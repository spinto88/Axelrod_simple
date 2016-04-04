
import ctypes as C


class Axl_node(C.Structure):
     """
     Axelrod node: information about its degree and neighbors
     """
     _fields_ = [('degree', C.c_int),
                 ('label', C.c_int),
                 ('neighbors', C.POINTER(C.c_int))]
