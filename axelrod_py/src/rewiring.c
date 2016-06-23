
#include "rewiring.h"

/* This function puts in "changes" the old and new neighbour for a given agent.
   The criteria of change a neighbour is that the homophily with the older is less 
   than with the new neighbour. But this only takes only opinion links */

int rewiring(axl_network *mysys, axl_network_alloc *mysys_alloc)
{
	int i, j, neigh_ind;
	int old, new, new_degree_plus, new_degree_less, rewiring_on = 0;
	int n = mysys.nagents;
	top_changes *changes;
	double h_old, h_new;

	changes = (top_changes *)malloc(sizeof(top_changes) * n);
	for(i = 0; i < n; i++)
	{
		changes[i].add = (int *)malloc(sizeof(int));
		changes[i].remove = (int *)malloc(sizeof(int));
	}
		 
	for(i = 0; i < n; i++)
	{
		if(mysys->agent[i].degree_opinion != 0)
		{
	                /* The neighbour to be replace is chosen of the list of opinion links */
			neigh_ind = rand() % mysys->agent[i].degree_opinion;
			old = &mysys_alloc->agent_alloc[i].opinion_links_alloc[neigh_ind];

			/* The proposed agent is taken by random choice */
			new = rand() % mysys->nagents;
			for(j = 0; j < mysys->agent[i].degree; j++)
			{
				while(new == i || new == mysys_alloc->agent_alloc[i].neighbors_alloc[j])
				{
					new = rand() % mysys->nagents;
					j = -1;	
				}
			}
        	        /* Calculate and compare the homophily of the agents */
			h_old = homophily(mysys->agent[i], mysys->agent[old], mysys->opinion_included);
			h_new = homophily(mysys->agent[i], mysys->agent[new], mysys->opinion_included);

	                /* The change is not made if the links already exists */
			if(h_old < h_new)
			{
				changes[i].remove = old;
				changes[i].add = new;
				rewiring_on = 1;
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
	        
	        old = &changes[i].remove;
	        new = &changes[i].add;
	        for(j = 0; j < mysys->agent[i].degree_opinion; j++)
	        {
	            if(mysys_alloc->agent_alloc[i].opinion_links_alloc[j] == old)
	            {
	                mysys_alloc->agent_alloc[i].opinion_links_alloc[j] = new;
	            }
	        }
	        for(j = 0; j < mysys->agent[i].degree; j++)
	        {
	            if(mysys_alloc->agent_alloc[i].neighbors_alloc[j] == old)
	            {
	                mysys_alloc->agent_alloc[i].neighbors_alloc[j] = new;
	            }
	        }
	        
	        //Add new neighbour to the other (new) agent
	        new_degree_plus = mysys->agent[new].degree_opinion + 1;
	        mysys_alloc->agent_alloc[new].opinion_links_alloc = (int *)realloc(mysys_alloc->agent_alloc[new].opinion_links_alloc,sizeof(int) * new_degree_plus);
	        mysys_alloc->agent_alloc[new].opinion_links_alloc[new_degree_plus - 1] = i;
	        mysys->agent[new].degree_opinion = new_degree_plus;
	        
	        new_degree_plus = mysys->agent[new].degree + 1;
	        mysys_alloc->agent_alloc[new].neighbors_alloc = (int *)realloc(mysys_alloc->agent_alloc[new].neighbors_alloc,sizeof(int) * new_degree_plus);
	        mysys_alloc->agent_alloc[new].neighbors_alloc[new_degree_plus - 1] = i;
	        mysys->agent[new].degree = new_degree_plus;
	        
	        //Remove neighbour to the other (old) agent
	        new_degree_less = mysys->agent[old].degree_opinion - 1;
	        for(j = 0; j < mysys->agent[old].degree_opinion; j++)
	        {
	            if(mysys_alloc->agent_alloc[old].opinion_links_alloc[j] == i)
	            {
	                mysys_alloc->agent_alloc[old].opinion_links_alloc[j] = mysys_alloc->agent_alloc[old].opinion_links_alloc[mysys->agent[old].degree_opinion - 1];
	            }
	        }
	        mysys_alloc->agent_alloc[old].opinion_links_alloc = (int *)realloc(mysys_alloc->agent_alloc[old].opinion_links_alloc,sizeof(int) * new_degree_less);
	        mysys->agent[old].degree_opinion = new_degree_less;
	        
	        new_degree_less = mysys->agent[old].degree - 1;
	        for(j = 0; j < mysys->agent[old].degree; j++)
	        {
	            if(mysys_alloc->agent_alloc[old].neighbors_alloc[j] == i)
	            {
	                mysys_alloc->agent_alloc[old].neighbors_alloc[j] = mysys_alloc->agent_alloc[old].neighbors_alloc[mysys->agent[old].degree - 1];
	            }
	        }
	        mysys_alloc->agent_alloc[old].neighbors_alloc = (int *)realloc(mysys_alloc->agent_alloc[old].neighbors_alloc,sizeof(int) * new_degree_less);
	        mysys->agent[old].degree = new_degree_less;
	    }
	}
	free(changes);
	return rewiring_on;			
			
}	
