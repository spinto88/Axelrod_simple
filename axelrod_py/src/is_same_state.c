#include "is_same_state.h"

int is_same_state(axl_agent agent1, axl_agent agent2, int clustering_radio, int type_search)
{
	/* Criterion of same state */

	int diff_q;
	double hab;

        if(type_search == 0)
	{
		diff_q = abs(agent1.feat[0] - agent2.feat[0]);

        	if(diff_q <= clustering_radio)
			return 1;
		else 
			return 0;
        }
        else 
        {
		if(agent1.vaccine == agent2.vaccine)
			return 1;
		else 
			return 0;
        }
}
