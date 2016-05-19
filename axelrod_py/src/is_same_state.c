#include "is_same_state.h"

int is_same_state(axl_network mysys, int node1, int node2, int clustering_radio, int type_serch)
{
	/* Criterion of same state */

	int diff_q;
	double hab;
	axl_agent a = mysys.agent[node1];
	axl_agent b = mysys.agent[node2];

        if(type_serch == 0)
        {
		diff_q = abs(a.feat[0] - b.feat[0]);

        	if(diff_q <= clustering_radio)
			return 1;
		else 
			return 0;
        }
        else 
        {
		if(a.vaccine == b.vaccine)
			return 1;
		else 
			return 0;
        }
}
