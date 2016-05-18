
#include "is_neighbor.h"

int is_neighbor(axl_agent agent1, int ind_agent2)
{
/**
It sees if the index of the agent 2 is in the list of neighbors of agent 1.
*/
	int i;

	for(i = 0; i < agent1.degree; i++)
	{
		if(ind_agent2 == agent1.neighbors[i])
			return 1;
	}
	return 0;
}

