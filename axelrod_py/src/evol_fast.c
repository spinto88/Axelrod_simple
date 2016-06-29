
#include "evol_fast.h"

void evol_fast(axl_network *mysys, int steps, int seed)
{
	int i, j, step;
	int n = mysys->nagents;
	int *neighbors;
	int total_degree;
	double random;

	neighbors = (int *)malloc(sizeof(int) * n);

	srand(seed);

	for(step = 0; step < steps; step++)
	{

		/* Select a lattice neighbors */
	        for(i = 0; i < n; i++)
		{
			if(mysys->rewiring == 0)
			{
				j = rand() % mysys->agent[i].contact_degree;
	        	        neighbors[i] = mysys->agent[i].contact_links[j];
			}

			else if(mysys->rewiring == 1)
			{ 			
				total_degree = mysys->agent[i].contact_degree + mysys->agent[i].opinion_degree;

				random = ((double)rand()) / RAND_MAX;

				if(random < (((double)mysys->agent[i].contact_degree) / total_degree))
				{
					j = rand() % mysys->agent[i].contact_degree;
		        	        neighbors[i] = mysys->agent[i].contact_links[j];
				}
				else
				{
					j = rand() % mysys->agent[i].opinion_degree;
				        neighbors[i] = mysys->agent[i].opinion_links[j];	
				}
			}

		}

		if(mysys->evol_opinion == 0)
			evolution(mysys, neighbors, rand());
                else if(mysys->evol_opinion == 1)
			evolution_op(mysys, neighbors, rand());
		
		if(mysys->rewiring == 1)
			rewiring(mysys, rand());

                if(mysys->noise > 0.00)
			noise(mysys, rand());

	}

	free(neighbors);

	return;
}
	
