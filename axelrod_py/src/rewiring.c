
#include "rewiring.h"

/* This function puts in "changes" the old and new neighbour for a given agent.
   The criteria of change a neighbour is that the homophily with the older is less 
   than with the new neighbour. But this only takes only opinion links */

void rewiring(axl_network mysys, top_changes *changes)
{
	int i, j, neigh_ind;
	int old, new;
	int n = mysys.nagents;
	double h_old, h_new;

	for(i = 0; i < n; i++)
	{
		if(mysys.agent[i].degree_opinion != 0)
		{
	                /* The neighbour to be replace is chosen of the list of opinion links */
			neigh_ind = rand() % mysys.agent[i].degree_opinion;
			old = mysys.agent[i].opinion_links[neigh_ind];

			/* The proposed agent is taken by random choice */
			new = rand() % mysys.nagents;

        	        /* Calculate and compare the homophily of the agents */
			h_old = homophily(mysys.agent[i], mysys.agent[old]);
			h_new = homophily(mysys.agent[i], mysys.agent[new]);

	                /* The change is not made if the links already exists */
			if(h_old < h_new)
			{
				changes[i].remove = old;
				changes[i].add = new;
                	        for(j = 0; j < mysys.agent[i].degree; j++)
				{
					if(new == mysys.agent[i].neighbors[j])
					{
						changes[i].remove = -1;
						changes[i].add = -1;
					}
				}
				if(new == i)
				{	
					changes[i].remove = -1;
					changes[i].add = -1;
				}
			}	
			else
			{
				changes[i].remove = -1;
				changes[i].add = -1;
			}
		}
	}
	
	return;			
			
}	
