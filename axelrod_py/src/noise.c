
#include "noise.h"

int noise(axl_network *mysys, int seed)
{
	/* Noise function: it makes random changes in the agents
	with a rate equal to mysys->noise, which is the 
	probability that an agent's feature chosen at random takes a 
	value between 0 and q-1 
	This function returns the number of changes performed in a synchronic 
	adaptation */

	int i, j;
        int f, q;
        int n = mysys->nagents;
        int changes = 0;
        double r = mysys->noise;

	srand(seed);
	
	for(i=0; i<n; i++)
	{ 
		f = mysys->agent[i].f;
                q = mysys->agent[i].q;

		j = rand() % f;
		if((((double)rand())/RAND_MAX) < r)
		{
			mysys->agent[i].feat[j] = rand() % q;
			changes++;
		}
	}

	return changes;
}
