#include "evol_fast.h"

void evol_fast(axl_network *mysys, axl_node *nodes_info, int evol_type, int steps, int seed)
{
	int i, j, k, step;
	int n = mysys->nagents;

	srand(seed);

	// Perform a asynchronous step
        if(evol_type == 0)
	{
		for(step = 0; step < steps; step++)
		{
			for(k = 0; k < n; k++)
			{
	        		i = rand() % n;
				j = rand() % nodes_info[i].degree;

				evolution_asyncro(mysys, i, j, rand());
			}
		}
	}
	
	// Perform a synchronous step
        if(evol_type == 1)
	{
		int* neighbors;
		neighbors = (int *)malloc(sizeof(int) * n);
		for(step = 0; step < steps; step++)
		{
	        	for(i = 0; i < n; i++)
			{	
				j = rand() % nodes_info[i].degree;
	        	        neighbors[i] = nodes_info[i].neighbors[j];
			}

			evolution_syncro(mysys, neighbors, rand());

                	if(mysys->noise > 0.00)
				noise(mysys, rand());
		}
		free(neighbors);
	}

	return;
}
	
