
#include "mean_homophily_followers.h"

double mean_homophily_followers(axl_mass_media mm, axl_network mysys)
{
	/* It adds the homophily between all the followers' agents normalized
	the number of pairs of followers that can be formed.
	It measures the similarity degree between followers. */

	int i, j;
	int n = mysys.nagents;
        int edit_secc = mm.edit_secc;
        int edit_line = mm.edit_line;
        int pairs = 0;
        double hab = 0.00;

	for(i = 0; i < n; i++)
	{
		if(mysys.agent[i].feat[edit_secc] == edit_line)
		{
			for(j = i; j < n; j++)
			{
				if(mysys.agent[j].feat[edit_secc] == edit_line)
				{
					hab += homophily(mysys.agent[i], mysys.agent[j]);
					pairs++;
				}
			}
		}
	}

        if(pairs != 0)
		return (hab / pairs);
        else
                return (hab);
}		
