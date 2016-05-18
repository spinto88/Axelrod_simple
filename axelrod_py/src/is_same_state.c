#include "is_same_state.h"

int is_same_state(axl_agent agent1, axl_agent agent2, int clustering_radio)
{
	/* Criterion of same state */

	int diff_q;
	double hab;

	diff_q = abs(agent1.feat[0] - agent2.feat[0]);

        if(diff_q <= clustering_radio)
		return 1;
	else 
		return 0;
}
