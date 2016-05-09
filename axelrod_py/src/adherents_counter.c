#include "adherents_counter.h"

// Counts the number of agents that have the value q in the first feature
 
int adherents_counter(axl_network mysys, int q)
{
	int i;
	int n = mysys.nagents;
	int adherents = 0;

	for(i = 0; i < n; i++)
	{
		if(mysys.agent[i].feat[0] == q)
			adherents++;
	}

	return adherents;
}	
