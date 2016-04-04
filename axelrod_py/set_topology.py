import networkx as nx
import random as rnd

def set_topology(G, bin_p = 0.00, bara_m = 0.00, p_sw = 0.00):

    if G.id_topology == 0.0:
        """ 
        Square lattice with periodic bounded conditions
        """
        nagents = G.nagents
        n = int(nagents ** 0.5)
        nagents = n*n
        if nagents != G.nagents:
            print 'The number of agents must be a perfect square'
            print 'The number is set to ' + str(nagents) + ' agents'
       	G.nagents = nagents
        for i in range(0, nagents):
            x = i % n
            y = i / n
	    neigh1 = (x + 1) % n + y * n
	    neigh2 = x + ((y + 1) % n) * n
            G.add_edge(i, neigh1)
            G.add_edge(i, neigh2)
    
    elif G.id_topology == 0.1:
        """ 
	Square lattice with rigid walls (finit lattice, without PBC)
	"""
        nagents = G.nagents
        n = int(nagents ** 0.5)
        nagents = n * n
        if nagents != G.nagents:
            print 'The number of agents must be a perfect square'
            print 'The number is set to ' + str(nagents) + ' agents'
        G.nagents = nagents
	    
	for i in range(0, nagents):
           Neigh1 = i + n
           Neigh2 = i + 1
           if(Neigh1 < nagents):
               G.add_edge(i, Neigh1)
	   if((Neigh2 % n) != 0):
	       G.add_edge(i, Neigh2)


    elif G.id_topology == 1.0:
        """ 
	Complete graph
	"""
        nagents = G.nagents
        nx.complete_graph(nagents, G)

    """
    elif id_topology == 2.0:

        def binomial_graph(G,p):
            N = G.N
            Aux = nx.binomial_graph(N,p)
            for i in range(0,N):
                Vec = Aux.edge[i].keys()
                for j in Vec:
                    G.add_edge(i,j)

        binomial_graph(G, bin_p)

    elif  id_topology == 3.0:

        def barabasi_albert_graph(G,m):
            N = G.N
            Aux = nx.barabasi_albert_graph(N,m)
            for i in range(0,N):
                Vec = Aux.edge[i].keys()
                for j in Vec:
                    G.add_edge(i,j)

        barabasi_albert_graph(G,bara_m)


    elif id_topology == 4.0:

        def square_small_world(G,p):    
            N = G.N
            n = int(N**0.5)
            N = n*n
            if N != G.N:
               print 'El N seleccionado debe ser un cuadrado perfecto'
               print 'Se aproxima N = ', N
               G.N = N
            for i in range(0,N):
                x = i%n
                y = i/n
                G.add_edge(i,(x+1)%n+y*n)
                G.add_edge(i,x+((y+1)%n)*n)
                for j in range(i+1,G.N):
                    if rnd.random() < p:
                        G.add_edge(i,j)

        square_small_world(G,p_sw)
        """	    
