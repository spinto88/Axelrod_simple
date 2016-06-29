
#include "init_network.h"

void distant_neighbors(axl_network *, int, int *);

void init_network(axl_network *mysys)
{
	int i, j, r;
	int n = mysys->nagents;
	int list_of_neighbors[8];

	for(i = 0; i < n; i++)
	{
		distant_neighbors(mysys, i, list_of_neighbors);
		for(j = 0; j < 8; j++)
			mysys->agent[i].opinion_links[j] = list_of_neighbors[j];
		for(j = 8; j < MAXIMUM_DEGREE; j++)
			mysys->agent[i].opinion_links[j] = -1;
	}

	return;
}

void distant_neighbors(axl_network *mysys, int agent, int *list_of_neighbors)
{
	int n2 = mysys->nagents;
	int n = (int)sqrt(n2);

	int x = agent % n;
	int y = agent / n;

	list_of_neighbors[0] = ((x + 2) + n) % n + ((y + n) % n) * n;
	list_of_neighbors[1] = ((x + 2) + n) % n + (((y + 2) + n) % n) * n;
	list_of_neighbors[2] = ((x + 2) + n) % n + (((y - 2) + n) % n) * n;
	list_of_neighbors[3] = ((x - 2) + n) % n + ((y + n) % n) * n;
	list_of_neighbors[4] = ((x - 2) + n) % n + (((y + 2) + n) % n) * n;
	list_of_neighbors[5] = ((x - 2) + n) % n + (((y - 2) + n) % n) * n;
	list_of_neighbors[6] = (x + n) % n + (((y + 2) + n) % n) * n;
	list_of_neighbors[7] = (x + n) % n + (((y - 2) + n) % n) * n;

	return;
}
