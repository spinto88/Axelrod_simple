
#include "is_neighbor.h"

int is_neighbor(axl_node node1, int ind_node2)
{
/**
It sees if the index of node 2 is in the list of neighbors of node 1
*/
	int i;

	for(i = 0; i < node1.degree; i++)
	{
		if(ind_node2 == node1.neighbors[i])
			return 1;
	}
	return 0;
}

