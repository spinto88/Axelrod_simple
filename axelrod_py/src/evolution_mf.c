#include "evolution_mf.h"
#include <stdio.h>

void evolution_mf(axl_network *mysys, int *neighbors, int seed)
{
	int i, j, f, r;	
        int n = mysys->nagents;
        int diff_q, diff_frac, mode_mf = mysys->mode_mf;
        double h_ab, random, fraction, b = mysys->b, phi = mysys->phi;

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
		if(random < phi && mysys->agent[i].zealot != 1)
		{
			r = 0;
			Changes[i].x = r;	
			
                        if(r <  mysys->number_of_metric_feats)
			{
				diff_frac= (int)(mysys->agent[i].feat[r] * fraction);
				Changes[i].value = (rand() % (diff_frac + 1));
				
				//Changes[i].value = mysys->agent[i].feat[r] - 1;
				//if(Changes[i].value < 0)
				//    Changes[i].value = 0;
			}
			/* Else (if it is not metric) take the exact feature of mean field.*/
			else     		        
				Changes[i].value = 0;
		}
		else
		{
			/* Normal interaction with neighbors*/
       			j = neighbors[i];

			/* Homophily between agent i and j */
			h_ab = homophily(mysys->agent[i], mysys->agent[j]);

    			random = (((double)rand())/RAND_MAX);
	   	
			/* If the interaction takes place */
	    		if((random < h_ab)&&(h_ab != 1.00))
			{
				/* Take a random feature where the agents have a different value */
				f = mysys->agent[i].f;
				fraction = mysys->agent[i].fraction;
	
				random = (((double)rand())/RAND_MAX);	
			
				if((mysys->agent[j].zealot == 1)&&(mysys->agent[i].feat[0] != mysys->agent[j].feat[0])) /*condition for zealot*/
			    		r = 0;
			   	else
				{
		    			r = rand() % f;
					while(mysys->agent[i].feat[r] == mysys->agent[j].feat[r])
				    		r = (r+1)%f;
				}			
      	    			        	
        			if((mysys->agent[i].zealot != 0)&&(r==0))
				{
        	    			/*If the agent i is a zealot, it does not change the first feature*/
					continue;    
        	    	    	}	
       	    			Changes[i].x = r;
				/* Here we looks if f in one of metric features */
                        	if(r <  mysys->number_of_metric_feats)
				{
				    //Changes[i].value = mysys->agent[i].feat[r] + (mysys->agent[j].feat[r] - mysys->agent[i].feat[r])/abs(mysys->agent[j].feat[r] - mysys->agent[i].feat[r]);
					/* Differences between Q values */
					diff_q = mysys->agent[i].feat[r] - mysys->agent[j].feat[r];
					diff_frac= (int)(diff_q * fraction);

					/* The new value is the actual value plus (less) a random value inside the difference */
					if(diff_q > 0)
						Changes[i].value = mysys->agent[j].feat[r] + (rand() % (diff_frac + 1));
					else
					{	
						/* Put the difference greater than zero */
						diff_frac = (-1 * diff_frac);
						random = (((double)rand())/RAND_MAX);
						Changes[i].value = mysys->agent[j].feat[r] - (rand() % (diff_frac + 1));
					}
				}
				/* Else (if it is not metric) take the exact feature of j */
				else     		        
					//Changes[i].value = mysys->agent[i].feat[r] + (mysys->agent[j].feat[r] - mysys->agent[i].feat[r])/abs(mysys->agent[j].feat[r] - mysys->agent[i].feat[r]);
					Changes[i].value = mysys->agent[j].feat[r];
			}
		
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
