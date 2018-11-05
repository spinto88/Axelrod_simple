#include "evolution_asyncro.h"

void evolution_asyncro(axl_network *mysys, int i, int j, int seed)
{
	int f, r;	
        double h_ab, random;

	/* Homophily between agent i and j */
	h_ab = homophily(mysys->agent[i], mysys->agent[j]);

    	random = (((double)rand())/RAND_MAX);
   	
	/* If the interaction takes place */
	if((random < h_ab)&&(h_ab != 1.00))
	{
		/* Take a random feature where the agents have a different value */
		f = mysys->agent[i].f;	
		r = rand() % f;
				
  	     	while(mysys->agent[i].feat[r] == mysys->agent[j].feat[r])
				r = (r+1)%f;

		mysys->agent[i].feat[r] = mysys->agent[j].feat[r];
	}

	return;
}
