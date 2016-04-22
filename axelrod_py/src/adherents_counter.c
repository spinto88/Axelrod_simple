#include "adherents_counter.h"

int adherents_counter(axl_network mysys)
{
	int i;
	int n = mysys.nagents;
	int q_z;
	int adherents = 0;

	for(i = 0; i < n; i++)
	{
		if(mysys.agent[i].feat[0] == (mysys.agent[i].q_z - 1))
			adherents++;
	}

	return adherents;
}	
