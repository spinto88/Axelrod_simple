
from axelrod_py import *
import cPickle as pk

rand.seed(123459)

for Z in range(0, 36, 5):

    A = zealots_list(1024, Z)

    for b in [0.00, 0.10, 0.20, 0.25, 0.30, 0.40, 0.50]:

        for conf in range(0, 50):

            mysys = Axl_network(n = 100, f = 10, q = 20, A = A, b = b, mode_mf = 0, number_of_metric_feats = 1)

            mysys.set_topology(id_topology = 1.1, opinion_links = 'No')

            mysys.set_initial_state_equal()

            for i in range(0, 5):

                mysys.evolution(100000)

                distribution = mysys.adherents_distribution()[0] 
                
                mysys.vaccinate()

		distribution_vaccine = mysys.fragment_identifier(type_search = 1)[0]
                smax_no_vaccine = mysys.fragment_identifier(type_search = 1)[1]
                number_of_vaccines = mysys.vaccinated_counter()

                fname = 'Z' + str(Z) + '_b' + str(b) + '_conf' + str(conf) + '_step' + str(i) + '.dat'
                fp = open(fname, 'a')
                data = [distribution, distribution_vaccine, smax_no_vaccine, number_of_vaccines]
                pk.dump(data, fp)
                





