
#include "fragment_identifier.h"

void fragment_identifier(axl_network mysys, axl_node *node_info, int clustering_radio)
{

	/* =================================================
	Fragment identifier:
        It takes as argument an axelrod network, and puts into vector 
        labels an identifier of each agent. If two agents share an equal label
        it means that they belong from the same cluster.
        Degree[i] is the degree of the node i.
        Neighbors[i] are the neighbors of node i, from 0 to degree[i].
	==================================================*/

	int i, j, k;
        int node1, node2;
	int *ordering;
        int n = mysys.nagents;
	
	ordering = (int *)malloc( n * sizeof(int));

	// Initilization of the vector labels and ordering
        // Ordering vector puts the nodes with the same label together
	for(i = 0; i < n; i++)
	{
		node_info[i].label = i;
		ordering[i] = i;
	}

	j = 0;
	for(i = 0; i < n; i++)
	{

		// Node 1 is the node in the i'th place of ordering
		node1 = ordering[i]; 

		if(j == i)
			j += 1;
                // j is the place where we are in the ordering vector, allways a step after i

                // k is the index which we use to go over the vector ordering. It allways starts from the j'th place
                k = j;
		while(k < n)
		{
			// Node 2 is the node which we compare with node 1
  			node2 = ordering[k];

			if(((is_neighbor(node_info[node1], node2)) == 1) && (is_same_state(mysys, node1, node2, clustering_radio) == 1))
			// It means: if node2 is a neighbor of node1 and they have the same state, so... 			
			{					
                                                // Label of node 2 becomes the same as the node 1's label
						node_info[node2].label = node_info[node1].label;	
                                                // We put the node 2 in the j'th place
						swap(ordering + k, ordering + j);
                                                // The new place in the ordering vector is the following
						j++;		
			}
		k++;

		}
	}
	
	free(ordering);

	return;
}
