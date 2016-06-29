import os
import ctypes as C
import networkx as nx
import random as rand
import numpy as np
import set_topology as setop
from axl_agent import *
#from axl_mass_media import *


libc = C.CDLL(os.getcwd() + '/axelrod_py/libc.so')


class Axl_network(nx.Graph, C.Structure):

    """
    Axelrod network: it has nagents axelrod agents, and an amount of noise in the dynamics of the system. This class inherites from the networkx.Graph the way to be described.
    """
    _fields_ = [('nagents', C.c_int),
                ('agent', C.POINTER(Axl_agent)),
                ('noise', C.c_double),
		('phi', C.c_double),
		('evol_opinion', C.c_int),
                ('opinion_included', C.c_int),
		('rewiring', C.c_int)]

    def __init__(self, n, f, q, q_z = 100, ff = 0, id_topology = 'Nan', net_parameters = {}, phi = 0.0, A = [], noise = 0.00):
        """
        Constructor: initializes the network.Graph first, and set the topology and the agents' states. 
	"""
        # Init graph properties
        nx.Graph.__init__(self)
        nx.empty_graph(n, self)

        # Init agents' states
        self.init_agents(n, f, q, q_z, A, ff)

        # Set noise rate or number of metric features
        self.noise = noise
 
        # Init mass media or external scalar field
	self.phi = phi
        self.n = n
        self.q_z = q_z
        # Init topology
        if id_topology != 'Nan':
            self.set_topology(id_topology, net_parameters)

        self.evol_opinion = 0
        self.opinion_included = 0
   

    def subgraph_max(self):
        # Return a copy of 
        
        #self.set_topology(id_topology = 2.1)
        maximo, distribution, label_max = self.fragment_identifier(type_search = 1)

        nbunch = []
        
        for i in range(0,self.n):
            if (self.agent[i].label == label_max):
                nbunch.append(i)
        
        H = nx.Graph()
	
        for i in nbunch:
            H.add_node(i)
            for j in range(0,self.agent[i].degree):
                node = self.agent[i].neighbors[j]
                if((i>node) and (node in nbunch)):
                    H.add_edge(i,node)
      
        return H, maximo, distribution 


    def set_topology(self, id_topology, parameters = {}, rewiring = 0):
        """
        Set the network's topology
        """
        self.id_topology = id_topology

        setop.set_topology(self, id_topology, parameters)

        self.nagents = self.number_of_nodes()

        self.rewiring = rewiring

        for i in range(0, self.number_of_nodes()):
            self.agent[i].contact_degree = self.degree(i)
            self.agent[i].contact_links = (C.c_int * self.degree(i))(*self.neighbors(i))

            if self.rewiring == 1:
                self.agent[i].opinion_degree = 8
                self.agent[i].opinion_links = (C.c_int * 200)()

            self.node[i] = self.agent[i]	    

	if self.rewiring == 1:
	    libc.init_network.argtypes = [C.POINTER(Axl_network)]
	    libc.init_network(C.byref(self))


    def init_agents(self, n, f, q, q_z, A, ff):
        """
        Iniatialize the agents' state.
        """
        self.nagents = n
        self.agent = (Axl_agent * self.nagents)()
    
        for i in range(0, self.nagents):
            self.agent[i] = Axl_agent(f, q, q_z, ff)
                        
        for j in A:
            self.agent[j].zealot = 1
            self.agent[j].opinion = q_z


    def set_zealots(self, A, type_z):

        for item in A:
            self.agent[item].zealot = type_z
            self.agent[item].opinion = self.q_z

            
    def set_initial_state_equal(self, feature):

        for i in range(0, self.nagents):

            if self.agent[i].zealot == 0:
                self.agent[i].feat[0] = feature


    def set_number_of_fixed_features(self, ff):
    
        for i in range(0, self.nagents):
            self.agent[i].ff = ff


    def adherents_counter(self):
        """
        Gives number of agents with the same q for the opinion, only for the q_z given
        """
        libc.adherents_counter.argtypes = [Axl_network, C.c_int]
        libc.adherents_counter.restype = C.c_int

        q_z = self.q_z
        
        # The adherents have a q equal to qz
        adherents = libc.adherents_counter(self, q_z)
        adherents = float(adherents)/self.nagents
        
        return adherents
    

    def adherents_distribution(self):
        """
        Gives a number of agents with the same q for the first feature, for all q
        """
        libc.adherents_counter.argtypes = [Axl_network, C.c_int]
        libc.adherents_counter.restype = C.c_int
        
        q_z = self.q_z

        adherents = np.zeros(q_z + 1)        
        for q in range(0, q_z + 1):
            adherents[q] += float(libc.adherents_counter(self, q)) / self.nagents
        
        average = np.average(range(0, q_z + 1), weights = adherents)
        desviation = 0
        for q in range(0, q_z + 1):
            desviation += abs(average - q) * adherents[q]

        return adherents, average, desviation
        
    
    def adherents_hist(self, fname = ''):
        
        adherents = self.adherents_distribution()[0]
        q_z = self..q_z

        import matplotlib.pyplot as plt

        plt.ion()
        figure = plt.figure(1)
        figure.clf()

        plt.hist(range(0, q_z + 1), bins = q_z + 1, weights = adherents, normed = True)
        plt.xlabel('Q value of the opinion')
        plt.ylabel('Normalized histogram')
        if fname == '':
            figure.canvas.draw()
        else:
	    plt.savefig(fname)

    
    def vaccinated_counter(self):
        """
        Gives number of agents that deacided to be vaccinated
        """
        vaccinated = 0
        
        for i in range(0, self.nagents):
            if (self.agent[i].vaccine == 1):
                vaccinated = vaccinated + 1 
        
        return vaccinated    

        
    def vaccinate(self):
        """
        Takes the network and decides randomly who gets the vaccine and who does not, depending on the value of the first feature of each agent
        """
        q_z = self..q_z 
        
        for i in range(0,self.nagents):
        
            aux = rand.randint(1, q_z)
            
            if(aux <= self.agent[i].opinion):
                # 0 means that the agent is not vaccinated
                self.agent[i].vaccine = 0
            else:
                self.agent[i].vaccine = 1


    def evolution(self, steps = 1):
        """
	Make steps synchronius evolutions of the system
        """

        libc.evol_fast.argtypes = [C.POINTER(Axl_network), C.c_int, C.c_int]

        libc.evol_fast(C.byref(self), steps, rand.randint(0, 10000))


    def fragment_identifier(self, clustering_radio = 0, type_search = 0, opinion_links_included = 0):
        """
 	Fragment identifier: it returns the size of the biggest fragment, its state, 
	and the cluster distribution.
        It sees if the agents are neighbors and have the first feature less or equal
	than the clustering radio.
        """
       
        n = self.nagents
        libc.fragment_identifier.argtypes = [C.POINTER(Axl_network), C.c_int, C.c_int]      

	# This function puts in nodes_info[i].label the label of the node i, according to 
	# the current criteria of identifing 
        if self.rewiring != 1:
            opinion_links_included = 0

        libc.fragment_identifier(C.byref(self), clustering_radio, type_search, opinion_links_included)

        # After this, the vector labels has the label of each agent
        labels = np.zeros(n)
        for i in range(0, n):
            labels[self.agent[i].label] += 1
        
        # Size_max is the size of the biggest fragment
        size_max = labels.max()
	# Index_max the label of the biggest fragment
        index_max = labels.argmax()

        # feat0_distribution returns a dictionary with all clusters in the system, 
	# its first feature and size
        if(type_search == 0):
            opinion_distribution = []
            opinion_distribution_size = []
            for i in range(0, len(labels)):
                if labels[i] != 0:
                    opinion_distribution.append({'First feature': self.agent[i].opinion, 'Size': labels[i]})
                    opinion_distribution_size.append(labels[i])
        elif(type_search == 1):
            vaccine_distribution = []
           
            for i in range(0, len(labels)):
                if labels[i] != 0:
                    vaccine_distribution.append([self.agent[i].vaccine,labels[i],i])
        elif(type_search == 10):
            cluster_distribution = []
           
            for i in range(0, len(labels)):
                if labels[i] != 0:
                    cluster_distribution.append(labels[i])        
                    
                    
        if(clustering_radio == 0 and type_search == 0):
            # feat is the first feature of the biggest fragment
            feat = self.agent[index_max].feat[0]
            return size_max, feat, feat0_distribution
       	elif(clustering_radio != 0 and type_search == 0):
            # Size of the biggest fragment and size distribution
	    return size_max, feat0_distribution_size
	elif(type_search == 1):
	    # Returns Size cluster max no vaccinated, distribution of vaccinated and not, label of the cluster max of no vaccinated
            no_vaccine_data = []
            no_vaccine_label = []
            for item in vaccine_distribution:
                if(item[0] == 0):
                    no_vaccine_data.append(item[1])
                    no_vaccine_label.append(item[2])
            if(no_vaccine_data == []):
                no_vaccine_data.append(0)
            
            return np.max(no_vaccine_data),no_vaccine_data,no_vaccine_label[no_vaccine_data.index(np.max(no_vaccine_data))]
	elif(type_search == 10):
	    return size_max, cluster_distribution           


    def active_links(self, opinion_links_included = 0):

        """
	Active links: it returns True if there are active links in the system.
        """
	
	libc.active_links.argtypes = [Axl_network, C.c_int]
	libc.active_links.restype = C.c_int

	return libc.active_links(self, opinion_links_included)


    def evol2convergence(self, check_steps = 1000):
        """ 
	Evolution to convergence: the system evolves until there is no active links, checking this by check_steps. Noise must be equal to zero.
        """
        if self.noise > 0.00:
            return "Convergence cannot be reach with noise in the system"

        if self.rewiring == 1:
            opinion_links_included = 1
        else:
            opinion_links_included = 0
 
        steps = 0
    	while self.active_links(opinion_links_included) != 0:
            self.evolution(check_steps)
                
            steps += check_steps

	return steps

    
    def evol2stationary(self, epsilon = 0.01):
        """
        This function manages the system to a stationary state, where 
        the average value of the adherents and the width of the distribution
        remains almost constant
        """

        average_aux = 0
        stationary = 0
        steps = 0
        data3average = []

        while stationary != 1:

            data2average = []
            
            self.evolution(1000)
            steps += 1000
            for i in range(0, 10):
                self.evolution(10)
                steps += 10
                data2average.append(self.adherents_distribution()[1])
                
            for num in data2average:
                    data3average.append(num)
                                        
            average_new = np.mean(data2average)

            m = abs(average_new - average_aux)
            
            if m < epsilon:
                stationary = 1
            else:        
                average_aux = average_new
            
        return steps, data3average 
    

    def image_opinion(self, fname = ''):
        """
        This method prints on screen the matrix of first features, of course the system is a square lattice.
        It is not confident if q is larger than 63.
        If fname is different of the null string, the matrix is save in a file with that name. This one can be loaded by numpy.loadtxt(fname).
        """
        if self.id_topology < 3.2:

            import matplotlib.pyplot as plt

            N = self.nagents
            n = int(N ** 0.5)
            q_z = self.agent[0].q_z
            matrix = []
            for i in range(0, n):
                row = []
                for j in range(0, n):
                    row.append(self.agent[(j + (i*n))].opinion)
                matrix.append(row)

            if fname != '':
                np.savetxt(fname + '.txt', matrix)

            plt.ion()
            figure = plt.figure(1)
            figure.clf()
            plt.imshow(matrix, interpolation = 'nearest', vmin = 0, vmax = q_z)
            plt.colorbar()
            if fname != '':
                plt.savefig(fname + '.png')
            else:
                figure.canvas.draw()

        else:
            print "The system's network is not a square lattice"
            pass
    
        
    def image_vaccinated(self, fname = ''):
        """
        This method prints on screen the matrix of vaccinated agents, of course the system is a square lattice.
        It is not confident if q is larger than 63.
        If fname is different of the null string, the matrix is save in a file with that name. This one can be loaded by numpy.loadtxt(fname).
        """
        if self.id_topology < 3.2:

            import matplotlib.pyplot as plt
            from matplotlib import colors

            N = self.nagents
            n = int(N ** 0.5)
            q_z = self.agent[0].q_z
            matrix = []
            for i in range(0, n):
                row = []
                for j in range(0, n):
                    row.append(self.agent[(j + (i*n))].vaccine)
                matrix.append(row)

            if fname != '':
                np.savetxt(fname + '.txt', matrix)

            plt.ion()
            cmap = colors.ListedColormap(['red', 'green'])
            bounds=[0, 0.1, 1]
            norm = colors.BoundaryNorm(bounds, cmap.N)

            figure = plt.figure(2)
            figure.clf()

            cmap = colors.ListedColormap(['red', 'green'])
            bounds=[0, 0.1, 1]
#            plt.imshow(matrix, interpolation='nearest', origin='lower',cmap=cmap, norm=norm)

            plt.imshow(matrix, interpolation = 'nearest', cmap = cmap, norm = norm)

            plt.colorbar(cmap=cmap, norm=norm, boundaries=bounds, ticks=[0, 1])

            if fname != '':
                plt.savefig(fname + '.png')
            else:
                figure.canvas.draw()

        else:
            print "The system's network is not a square lattice"
            pass
              

    def effective_q(self):
        """
        Print a vector with the number of actual q's per feature.
        For example, if all the system share the same state, the 
        effective_q vector = [1, 1, ..., 1] of dimension f.
        """

        n = self.nagents
        f = self.agent[0].f

        effective_q = []

        for i in range(0, f):

            q_list = []
            for j in range(0, n):
                q_list.append(self.agent[j].feat[i])

            aux = set(q_list)
            effective_q.append(len(aux))

        return effective_q


    def extract_network(self):

        graph = nx.Graph()

        for i in range(self.number_of_nodes()):

            for j in range(self.agent[i].contact_degree):

                k = self.agent[i].contact_links[j]
                if i < k:
                    graph.add_edge(i, k)

            for j in range(self.agent[i].opinion_degree):

                k = self.agent[i].opinion_links[j]
                if i < k:
                    graph.add_edge(i, k)

        return graph    
