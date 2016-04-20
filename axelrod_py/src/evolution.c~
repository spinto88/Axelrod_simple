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
			
			/* Here we looks if f in one of metric features */
                        if(r <  mysys->number_of_metric_feats)
			{
				/* Differences between Q values */
				diff_q = mysys->agent[i].feat[r] - mysys->agent[j].feat[r];

				/* The new value is the actual value plus (less) a random value inside the difference */
				if(diff_q > 0)
					Changes[i].value = mysys->agent[i].feat[r] - (rand() % (diff_q + 1));
				else
				{	
					/* Put the difference greater than zero */
					diff_q = (-1 * diff_q);
					Changes[i].value = mysys->agent[i].feat[r] + (rand() % (diff_q + 1));
				}
			}
			/* Else (if it is not metric) take the exact feature of j */
			else     		        
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
