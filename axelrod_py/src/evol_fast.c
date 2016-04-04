
#include "evol_fast.h"

void evol_fast(axl_network *mysys, axl_node *nodes_info, int steps, int seed)
{
	int i, j, step;
	int n = mysys->nagents;
	int *neighbors;

	neighbors = (int *)malloc(sizeof(int) * n);

	srand(seed);

	for(step = 0; step < steps; step++)
	{
	        for(i = 0; i < n; i++)
		{
			j = rand() % nodes_info[i].degree;
	                neighbors[i] = nodes_info[i].neighbors[j];
		}

		evolution(mysys, neighbors, rand());

                if(mysys->noise > 0.00)
			noise(mysys, rand());

	}

	free(neighbors);

	return;
}
	
