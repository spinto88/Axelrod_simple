
#include "is_neighbor.h"

int is_neighbor(axl_agent agent1, int ind_agent2, int opinion_links_included, int type_search)
{
/**
It sees if the index of the agent 2 is in the list of neighbors of agent 1.
*/
	int i;

	for(i = 0; i < agent1.contact_degree; i++)
	{
		if(ind_agent2 == agent1.contact_links[i])
			return 1;
	}

	if(opinion_links_included == 1, type_search != 1)
	{
	    for(i = 0; i < agent1.opinion_degree; i++)
   	    {
		if(ind_agent2 == agent1.opinion_links[i])
			return 1;
  	    }
	}

	return 0;
}

