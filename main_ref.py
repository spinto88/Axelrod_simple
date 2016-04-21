
# Main de referencia: Hace un barrido en q y calcula el valor del fragmento mas grande en el estado asintotico. Devuelve un archivo Smax.txt y el grafico correspondiente.
# Se le pueden agregar talibanes, campo externo, y features metricos
# ADVERTENCIA: con talibanes y campo externo, el sistema puede no converger. En ese caso hacerlo correr una determinada cantidad de pasos, y ver si llega a una estado estacionario.

from axelrod_py import *

# Numero de agentes en el sistema
N = 1024

# Numero de features
F = 10

# Identificador de topologia (0.0 Red cuadrada CPC, 0.1 paredes rigidas)
topology = 0.1

# Numero de features metricos
metric_features = 0

# Fraccion del intervalo tomado de los features metricos
# fraction = 0 es el Axelrod comun 
fraction = 1

# Fraccion de talibanes en la red
Z = 0.10

# Inicializacion de la semilla
rand.seed(123413)

# Lista de talibanes: ubicar luego de inicializar la semilla para tener siempre la misma lista
A = zealots_list(N,Z)

# Intensidad del campo externo
B = 0.00
# Strategia del campo externo (0 es medio masivo constante en el tiempo)
strategy = 0

# Ejemplo de barrido en q

fp = open('Smax.txt', 'a')
fp.write('#q\tsmax\tstd\n')
fp.close()

# Numero de configuraciones
Number_of_configurations = 1

# Listas donde guardo los promedios y barras de error
smax_mean = []
smax_std = []

# Valores que toma q
qrange = range(10, 100, 2)

for q in qrange:

    # Lista del fragmento mas grande por cada q
    smax_data = []

    for conf in range(0, Number_of_configurations):

        # Inicializo el sistema
	mysys = Axl_network(N, F, q, A = A, fraction = fraction, id_topology = topology)

        # Cantidad de features metricos
        mysys.number_of_metric_feats = metric_features

        # Parametros del medio masivo
        mysys.mass_media.b = B
        mysys.mass_media.strategy = strategy

        # Evolucion a la convergencia
        mysys.evol2convergence()

        # En vez de converger le digo cuantos pasos correr
        # mysys.evolution(15000)

        # Fragmento mas grande y estado
        smax, max_state = mysys.fragment_identifier()
        smax_data.append(smax)
    
    # Para cada q guardo el promedio del fragmento mas grande 
    fp = open('Smax.txt', 'a')
    fp.write(str(q) + '\t' + str(np.mean(smax_data)) + '\t' + str(np.std(smax_data)) + '\n')
    fp.close()

    smax_mean.append(np.mean(smax_data))
    smax_std.append(np.std(smax_data))

# Grafico
plt.errorbar(qrange, smax_mean, smax_std)
plt.show()
