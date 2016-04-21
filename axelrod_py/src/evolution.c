#include "evolution.h"

void evolution(axl_network *mysys, int *neighbors, int seed)
{
	int i, j, f, r;	
        int n = mysys->nagents;
        int diff_q, diff_frac;
        double h_ab, random, fraction;

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
                /* j == -1 is the Mass Media, which is described below */
		if(j != -1)
		{
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
			
				if((mysys->agent[j].zealot>random)&&(mysys->agent[i].feat[0] != mysys->agent[j].feat[0])) /*condition for zealot*/
			    	r = 0;    
				else
				{
			    		r = rand() % f;
				
	      	     			while(mysys->agent[i].feat[r] == mysys->agent[j].feat[r])
					    	r = (r+1)%f;
		   		}		

       	    			random = (((double)rand())/RAND_MAX);
        	
        			if((mysys->agent[i].zealot>random)&&(r==0))
        	    			continue;  /*If the agent i is a zealot, it does not change the first feature*/
        	    		Changes[i].x = r;
			
				/* Here we looks if f in one of metric features */
        	                if(r <  mysys->number_of_metric_feats)
				{
					/* Differences between Q values */
					diff_q = mysys->agent[i].feat[r] - mysys->agent[j].feat[r];
					diff_frac= (int)(diff_q*fraction);

					/* The new value is the actual value plus (less) a random value inside the difference */
					if(diff_q > 0)
						Changes[i].value = mysys->agent[j].feat[r] + (rand() % (diff_frac + 1));
					else
					{	
						/* Put the difference greater than zero */
						diff_frac = (-1 * diff_frac);	
						Changes[i].value = mysys->agent[j].feat[r] - (rand() % (diff_frac + 1));
					}
				}
				/* Else (if it is not metric) take the exact feature of j */
				else     		        
					Changes[i].value = mysys->agent[j].feat[r];
			}
	 	}
		/* The Mass Media case */
		else if (j == -1)
		{

			h_ab = homophily_mm(mysys->mass_media, mysys->agent[i]);

			random = (((double)rand())/RAND_MAX);
	   	
			/* If the interaction takes place */
		    	if((random < h_ab)&&(h_ab != 1.00))
			{
				/* It looks first if the first feature (edit section) is shared by the agent */
				if(mysys->agent[i].feat[mysys->mass_media.edit_secc] != mysys->mass_media.edit_line)
				{
					Changes[i].x = mysys->mass_media.edit_secc;
					/*Metric feature*/
					if(mysys->mass_media.edit_secc < mysys->number_of_metric_feats)
					{
						diff_q = mysys->agent[i].feat[mysys->mass_media.edit_secc] - mysys->mass_media.edit_line;
						diff_frac = (int)(diff_q * fraction);
						if(diff_q > 0)		
  							Changes[i].value = mysys->mass_media.edit_line + (rand() % (diff_frac + 1));
						else
						{
							diff_frac = (-1 * diff_frac);
       			   		                Changes[i].value = mysys->mass_media.edit_line - (rand() % (diff_frac + 1));
						}
					}
					else
						Changes[i].value = mysys->mass_media.edit_line;
				}
				/* If the first feature is already shared, the interaction goes on as usual */
				else
				{
					/* Take a random feature where the agents have a different value */
					f = mysys->agent[i].f;
					fraction = mysys->agent[i].fraction;	
					r = rand() % f;
				
			  	     	while(mysys->agent[i].feat[r] == mysys->mass_media.feat[r])
						r = (r+1)%f;

					Changes[i].x = r;
			
					/* Here we looks if f in one of metric features */
        	                	if(r <  mysys->number_of_metric_feats)
					{
						/* Differences between Q values */
						diff_q = mysys->agent[i].feat[r] - mysys->mass_media.feat[r];
						diff_frac= (int)(diff_q * fraction);

						/* The new value is the actual value plus (less) a random value inside the difference */
						if(diff_q > 0)
							Changes[i].value = mysys->mass_media.feat[r] + (rand() % (diff_frac + 1));
						else
						{	
							/* Put the difference greater than zero */
							diff_frac = (-1 * diff_frac);
							Changes[i].value = mysys->mass_media.feat[r] - (rand() % (diff_frac + 1));
						}
					}
					/* Else (if it is not metric) take the exact feature of j */
					else     		        
						Changes[i].value = mysys->mass_media.feat[r];
				}
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
