
#include "evol_fast.h"

void evol_fast(axl_network *mysys, axl_node *nodes_info, int steps, int seed)
{
	int i, j, step;
	int n = mysys->nagents;
	int *neighbors;
	axl_mass_media *mm = &(mysys->mass_media);

	neighbors = (int *)malloc(sizeof(int) * n);

	srand(seed);

	for(step = 0; step < steps; step++)
	{

		/* Select a lattice neighbors */
	        for(i = 0; i < n; i++)
		{
			j = rand() % nodes_info[i].degree;
	                neighbors[i] = nodes_info[i].neighbors[j];

		}

		if(mysys->mass_media.b != 0.00)
		{
			for(i = 0; i < n; i++)
			{
				/* Maybe the neighbour chosen is the Mass Media... */
				if(((double)rand())/RAND_MAX < mysys->mass_media.b)
					neighbors[i] = -1;
			}
		}

		if(mysys->mass_media.strategy != 0)
		{
			/* Adaptation of the mass media */
			for(i = 0; i < mysys->mass_media.f; i++)
				adaptation(mm, *(mysys), i);
		}

		evolution(mysys, neighbors, rand());

                if(mysys->noise > 0.00)
			noise(mysys, rand());

	}

	free(neighbors);

	return;
}
	
