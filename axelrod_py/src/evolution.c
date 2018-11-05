#include "evolution.h"

void evolution(axl_network *mysys, int *neighbors, int seed)
{
	int i, j, f, r;	
        int n = mysys->nagents;
        int diff_q;
        double h_ab, random;

        /* Struct feature which has the feature to change and the new value */
	struct Feature
	{
		int x;
		int value;
	} *Changes;

	srand(seed);
	
	/* Initialization of vector changes */
	Changes = (struct Feature *)malloc(sizeof(struct Feature)*n);
	for(i=0;i<n;i++)
	{
		Changes[i].x = -1;
		Changes[i].value = -1;
	}

	for(i=0;i<n;i++)
	{ 
		/* j is the neighbour which i interacts */
       	        j = neighbors[i];
                
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

			Changes[i].x = r;
			Changes[i].value = mysys->agent[j].feat[r];
	    	
	 	}

	}
	/* Updating of the network in a synchronic way */
	for(i=0;i<n;i++)
	{
		r = Changes[i].x;
		if(r!=-1)
			mysys->agent[i].feat[r] = Changes[i].value;
	}


        free(Changes);

	return;
}
