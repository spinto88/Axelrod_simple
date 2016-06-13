#include "evolution.h"
#include <stdio.h>

void evolution(axl_network *mysys, int *neighbors, int seed)
{
	int i, j, f, r, ff, k, sum;	
        int n = mysys->nagents;
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

		/* Normal interaction with neighbors*/
       		j = neighbors[i];

		f = mysys->agent[i].f;
		ff = mysys->agent[i].ff;

		/* Homophily between agent i and j. It's not include the opinion as a feature. */
		h_ab = homophily(mysys->agent[i], mysys->agent[j], 0);
					    
    		random = (((double)rand())/RAND_MAX);

		/* This is to fix some feature. If ff = 0 no change is made. */
		f = f - ff;

		/* Checks that the variable features are not all equal, like a reduced homophily*/
	        sum = 0;
	        for(k = 0; k < f; k++)
	        {
		        if(mysys->agent[i].feat[k] == mysys->agent[j].feat[k])
			        sum++;
	        }
	   		   	
		/* If the interaction takes place */
	 	if((random < h_ab) && (sum != f))
		{
			r = rand() % f;
			while(mysys->agent[i].feat[r] == mysys->agent[j].feat[r])
				r = (r + 1) % f;
      	    			        
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
