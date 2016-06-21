
#include "rewiring.h"

/* This function puts in "changes" the old and new neighbour for a given agent.
   The criteria of change a neighbour is that the homophily with the older is less 
   than with the new neighbour. But this only takes only opinion links */

void rewiring(axl_network *mysys, top_changes *changes, axl_network_alloc *mysys_alloc)
{
	int i, j, neigh_ind;
	int old, new, new_degree_plus, new_degree_less;
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
			for(j = 0; j < mysys.agent[i].degree; j++)
			{
				while(new == i || new == mysys.agent[i].neighbors[j])
				{
					new = rand() % mysys.nagents;
					j = -1;	
				}
			}
        	        /* Calculate and compare the homophily of the agents */
			h_old = homophily(mysys.agent[i], mysys.agent[old], mysys.opinion_included);
			h_new = homophily(mysys.agent[i], mysys.agent[new], mysys.opinion_included);

	                /* The change is not made if the links already exists */
			if(h_old < h_new)
			{
				changes[i].remove = old;
				changes[i].add = new;
			}	
			else
			{
				changes[i].remove = -1;
				changes[i].add = -1;
			}
		}
	}
	
	for(i = 0; i < n; i++)
	{
	    if(changes[i].remove != -1)
	    {
	        //Change old neighbour for the new in agent i
	        
	        old = changes[i].remove;
	        new = changes[i].add;
	        for(j = 0; j < mysys->agent[i].degree_opinion; j++)
	        {
	            if(mysys_alloc->agent_alloc[i].opinion_link_alloc[j] == old)
	            {
	                mysys_alloc->agent_alloc[i].opinion_link_alloc[j] = new;
	            }
	        }
	        
	        //Add new neighbour to the other (new) agent
	        new_degree_plus = mysys->agent[new].degree_opinion + 1;
	        realloc(mysys_alloc->agent[new].opinion_link,sizeof(int)*new_degree);
	        mysys_alloc->agent[new].opinion_link[new_degree] = i;
	        mysys->agent[new].degree_opinion = new_degree_plus;
	        
	        //Remove neighbour to the other (old) agent
	        new_degree_less = mysys->agent[old].degree_opinion - 1;
	        mysys_alloc->agent[old].opinion_link[new_degree] = i;
	    }
	}
	return;			
			
}	
