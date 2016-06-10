
#include "evol_fast.h"

void evol_fast(axl_network *mysys, int steps, int seed)
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
			j = rand() % mysys->agent[i].degree;
	                neighbors[i] = mysys->agent[i].neighbors[j];

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


		if(mysys->b == 0.00 && mysys->phi == 0.00)
			evolution(mysys, neighbors, rand());
		else if(mysys->phi != 0.00)
			evolution_mf(mysys, neighbors, rand());
	    else if(mysys->b != 0.00)
            evolution_mfb(mysys, neighbors, rand());

                if(mysys->noise > 0.00)
			noise(mysys, rand());

	}

	free(neighbors);

	return;
}
	
