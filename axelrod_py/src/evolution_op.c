#include "evolution_op.h"
#include <stdio.h>

void evolution_op(axl_network *mysys, int *neighbors, int seed)
{
	int i, j, f, r, ff, k, sum;	
        int n = mysys->nagents;
        int diff_q;
        double h_ab, random;
	double phi = mysys->phi;
	int opinion_included = mysys->opinion_included;

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
   		random = (((double)rand())/RAND_MAX);

		if(random < phi)
		{
			if(mysys->agent[i].zealot == 0)
			{
				// f - ff is the way to indicate that the opinion must be changed
				Changes[i].x = mysys->agent[i].f - mysys->agent[i].ff;
				Changes[i].value = rand() % (mysys->agent[i].opinion + 1);
			}
		}

		else
		{
			/* Normal interaction with neighbors*/
       			j = neighbors[i];

			f = mysys->agent[i].f;
			ff = mysys->agent[i].ff;

			/* Homophily between agent i and j. It's not include the opinion as a feature. */
			h_ab = homophily(mysys->agent[i], mysys->agent[j], opinion_included);
					    
			f = f - ff; // This is to fix some features, if ff = 0 no change is made

    			random = (((double)rand())/RAND_MAX);

			/* Checks that the variable features are not all equal, like a reduced homophily*/
	                sum = 0;
		        for(k = 0; k < f; k++)
		        {
			        if(mysys->agent[i].feat[k] == mysys->agent[j].feat[k])
				        sum++;
		        }
	   		   	
			/* If the interaction takes place */
	    		if(random < h_ab)
			{	
				r = -1;
				/* Condition for zealot: the zealot looks for changing the opinion of the other agent */ 
				if(mysys->agent[j].zealot == 1) 
				{
					if(mysys->agent[i].opinion != mysys->agent[j].opinion)
			    			r = f;
					else
					{
						if(sum != f)
						{
							r = rand() % f;
							while(mysys->agent[i].feat[r] == mysys->agent[j].feat[r])
							 	r = (r + 1) % f;
						}
					}
				}
		   		else
				{
					if(sum != f)
					{
			    			r = rand() % (f + 1);
						if(r == f)
						{
							if(mysys->agent[i].opinion == mysys->agent[j].opinion)
							{
								r = (r + 1) % f;
								while(mysys->agent[i].feat[r] == mysys->agent[j].feat[r])
							    		r = (r + 1) % f;
							}
						}
						else
						{ 
							while(mysys->agent[i].feat[r] == mysys->agent[j].feat[r])
								r = (r + 1) % f;
						}
					}
					else
						r = f;			
				}
      	   			        
				Changes[i].x = r;	

        			if((mysys->agent[i].zealot != 0) && (r == f))
        	    		/* If the agent i is a zealot, it does not change the opinion */
					Changes[i].x = -1;
				else
				{
					/* Here we looks if r is the opinion feature */
	                        	if(r == f)
					{
						/* Differences between opinino values */
						diff_q = mysys->agent[i].opinion - mysys->agent[j].opinion;

						/* The new value is the actual value plus (less) a random value inside the difference */
						if(diff_q > 0)
							Changes[i].value = mysys->agent[j].opinion + (rand() % (diff_q + 1));
						else
							Changes[i].value = mysys->agent[j].opinion - (rand() % (abs(diff_q) + 1));
					}				
					/* Else (if it is not metric) take the exact feature of j */
					else     		        
						Changes[i].value = mysys->agent[j].feat[r];
				}
			}	
		}
	}

	/* Updating of the network in a synchronic way */
	for(i=0;i<n;i++)
	{
		r = Changes[i].x;
		if(r!=-1)
		{
			f = mysys->agent[i].f;
			ff = mysys->agent[i].ff;
			f = f - ff;

			if(r == f)
				mysys->agent[i].opinion = Changes[i].value;
			else
				mysys->agent[i].feat[r] = Changes[i].value;
		}
	}

        free(Changes);

	return;
}
