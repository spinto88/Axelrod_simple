#include "is_same_state.h"

int is_same_state(axl_network mysys, int node1, int node2, int clustering_radio)
{
	/* Criterion of same state */

	int diff_q;
	double hab;
	axl_agent a = mysys.agent[node1];
	axl_agent b = mysys.agent[node2];

	diff_q = abs(a.feat[0] - b.feat[0]);

        if(diff_q <= clustering_radio)
		return 1;
	else 
		return 0;
}
