#include "init_net.h"

void init_net(axl_network *mysys, int seed)
{
	int i, j, f, q;
        int n = mysys->nagents;

	srand(seed);

        for(i = 0; i < n; i++)
	{
		f = mysys->agent[i].f;
		q = mysys->agent[i].q;
         	for(j = 0; j < f; j++)
			mysys->agent[i].feat[j] = rand() % q;       	
	}
	return;
}
