import networkx as nx
import random as rnd
import ctypes as C

def set_topology(G, id_topology, parameters = {}, opinion_links = 'No'):
 
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

	
    elif id_topology == 3.0:
	"""
	Square lattice with periodic bounded conditions, first, second and third neighbors
	"""
	
        n = int(G.number_of_nodes() ** 0.5)
        number_of_nodes = n * n
        if number_of_nodes != G.number_of_nodes():
            G.remove_nodes_from(range(number_of_nodes, G.number_of_nodes()))

	set_topology(G, id_topology = 2.0)

        if opinion_links == 'Yes':
            for i in range(0, number_of_nodes):
                G.agent[i].degree_contact = G.degree(i)
                G.agent[i].contact_links = (C.c_int * G.degree(i))(*G.neighbors(i))

        for i in range(0, number_of_nodes):
            x = i % n
            y = i / n
            neigh5 = (x + 2) % n + y * n
	    neigh6 = x + ((y + 2) % n) * n
            neigh7 = (x + 2) % n + ((y + 2) % n) * n
 	    neigh8 = (x - 2 + 2 * n) % n + ((y + 2 + 2 * n) % n) * n
            	
            G.add_edge(i, neigh5)
            G.add_edge(i, neigh6)
            G.add_edge(i, neigh7)
            G.add_edge(i, neigh8)

        if opinion_links == 'Yes':
            for i in range(0, number_of_nodes):
                G.agent[i].degree_opinion = G.degree(i) - G.agent[i].degree_contact
                opinion_links_list = G.neighbors(i)
                for j in range(0, G.agent[i].degree_contact):
                    opinion_links_list.remove(G.agent[i].contact_links[j])
                G.agent[i].opinion_links = (C.c_int * G.agent[i].degree_opinion)(*opinion_links_list)
        

    elif id_topology == 3.1:
        """ 
	Square lattice with rigid walls (finit lattice, without PBC), first, second and third neighbors.
	"""
        n = int(G.number_of_nodes() ** 0.5)
        number_of_nodes = n * n
        if number_of_nodes != G.number_of_nodes():
            G.remove_nodes_from(range(number_of_nodes, G.number_of_nodes()))
	    
        set_topology(G, id_topology = 2.1)

        if opinion_links == 'Yes':
            for i in range(0, number_of_nodes):
                G.agent[i].degree_contact = G.degree(i)
                G.agent[i].contact_links = (C.c_int * G.degree(i))(*G.neighbors(i))

	for i in range(0, number_of_nodes):
           Neigh5 = i + 2
	   Neigh6 = i + 2 + 2 * n
           Neigh7 = i + 2 * n
	   Neigh8 = i - 2 + 2 * n		

           if((Neigh5 % n) != 0 and ((Neigh5 - 1) % n) != 0):
	       G.add_edge(i,Neigh5)
           if(((Neigh6 % n) != 0 and ((Neigh6 - 1) % n) != 0) and Neigh6 < number_of_nodes):
               G.add_edge(i,Neigh6)
           if(Neigh7 < number_of_nodes):
	       G.add_edge(i,Neigh7)
           if((((Neigh8 + 1) % n) != 0 and ((Neigh8 + 2) % n) != 0) and Neigh8 < number_of_nodes):
               G.add_edge(i,Neigh8)

        if opinion_links == 'Yes':
            for i in range(0, number_of_nodes):
                G.agent[i].opinion_degree = G.degree(i) - G.agent[i].degree_contact
                opinion_links_list = G.neighbors(i)
                for j in range(0, G.agent[i].degree_contact):
                    opinion_links_list.remove(G.agent[i].contact_links[j])
                G.agent[i].opinion_links = (C.c_int * G.agent[i].degree_opinion)(*opinion_links_list)

    else:
        print "Topology is not set correctly"
