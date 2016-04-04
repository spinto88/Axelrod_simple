#include "is_same_state.h"

// Criterio de mismo estado //
int is_same_state(axl_agent a, axl_agent b)
{
	// The criterion of same state is to have exactly the same cultural state

	double hab;
	
	hab = homophily(a, b);

	if(hab == 1.00)
		return 1;
	else
		return 0;
}
