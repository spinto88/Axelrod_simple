#include "evolution.h"

void evolution(axl_network *mysys, int *neighbors, int seed)
{
	int i, j, f, r;	
        int n = mysys->nagents;
        double h_ab, random;

	struct Feature
	{
		int x;
		int value;
	} *Changes;

	Changes = (struct Feature *)malloc(sizeof(struct Feature)*n);

	srand(seed);

	for(i=0;i<n;i++)
	{
		Changes[i].x = -1;
		Changes[i].value = -1;
	}

	for(i=0;i<n;i++)
	{ 
       	        j = neighbors[i];

		h_ab = homophily(mysys->agent[i], mysys->agent[j]);

    		random = (((double)rand())/RAND_MAX);
   	
	    	if((random < h_ab)&&(h_ab != 1.00))
		{

			f = mysys->agent[i].f;
        		
			r = rand() % f;
				
	  	     	while(mysys->agent[i].feat[r] == mysys->agent[j].feat[r])
				r = (r+1)%f;
       		        
			Changes[i].x = r;
        	       	Changes[i].value = mysys->agent[j].feat[r];
	    	
	 	}

	}

	for(i=0;i<n;i++)
	{
		r = Changes[i].x;
		if(r!=-1)
			mysys->agent[i].feat[r] = Changes[i].value;
	}


        free(Changes);

	return;
}
