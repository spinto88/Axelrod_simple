import networkx as nx
import random as rnd
import ctypes as C

def set_topology(G, id_topology, parameters = {}):
 
    # Reset the graph
    for edge in G.edges():
        G.remove_edge(edge[0], edge[1])

    if id_topology == 0.0:
        """ 
	Complete graph.
	"""
        number_of_nodes = G.number_of_nodes()
        nx.complete_graph(number_of_nodes, G)


    elif id_topology == 1.0:
        """ 
        Square lattice with periodic bounded conditions. The number of N nodes is aproximated by the nearest perfect square.
        """
        n = int(G.number_of_nodes() ** 0.5)
        number_of_nodes = n * n
        if number_of_nodes != G.number_of_nodes():
            G.remove_nodes_from(range(number_of_nodes, G.number_of_nodes()))

        for i in range(0, number_of_nodes):
            x = i % n
            y = i / n
	    neigh1 = (x + 1) % n + y * n
	    neigh2 = x + ((y + 1) % n) * n
            G.add_edge(i, neigh1)
            G.add_edge(i, neigh2)
    

    elif id_topology == 1.1:
        """ 
	Square lattice with rigid walls (finit lattice, without PBC).
	"""
        n = int(G.number_of_nodes() ** 0.5)
        number_of_nodes = n * n
        if number_of_nodes != G.number_of_nodes():
            G.remove_nodes_from(range(number_of_nodes, G.number_of_nodes()))
	    
	for i in range(0, number_of_nodes):
           Neigh1 = i + n
           Neigh2 = i + 1
           if(Neigh1 < number_of_nodes):
               G.add_edge(i, Neigh1)
	   if((Neigh2 % n) != 0):
	       G.add_edge(i, Neigh2)

        
    elif id_topology == 2.0:
	"""
	Square lattice with periodic bounded conditions, first and second neighbors
	"""
        n = int(G.number_of_nodes() ** 0.5)
        number_of_nodes = n * n
        if number_of_nodes != G.number_of_nodes():
            G.remove_nodes_from(range(number_of_nodes, G.number_of_nodes()))

        set_topology(G, id_topology = 1.0)		

        for i in range(0, number_of_nodes):
            x = i % n
            y = i / n
            neigh3 = (x + 1) % n + ((y + 1) % n) * n
 	    neigh4 = (x - 1 + n) % n + ((y + 1 + n) % n) * n		
            G.add_edge(i, neigh3)
            G.add_edge(i, neigh4)

		
    elif id_topology == 2.1:
        """ 
	Square lattice with rigid walls (finit lattice, without PBC), first and second neighbors.
	"""
        n = int(G.number_of_nodes() ** 0.5)
        number_of_nodes = n * n
        if number_of_nodes != G.number_of_nodes():
            G.remove_nodes_from(range(number_of_nodes, G.number_of_nodes()))


        set_topology(G, id_topology = 1.1)
	    
	for i in range(0, number_of_nodes):
           Neigh3 = i + 1 + n
	   Neigh4 = i - 1 + n		
           if(Neigh3 < number_of_nodes and (Neigh3 % n) != 0):
	       G.add_edge(i,Neigh3)
           if(Neigh4 < number_of_nodes and ((Neigh4 + 1) % n) != 0):
               G.add_edge(i,Neigh4)

