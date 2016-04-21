
#include "mean_homophily_mm.h"

double mean_homophily_mm(axl_mass_media mm, axl_network mysys)
{
	/* Compute the mean value of the homophily among the followers
	of the mass media:
	It adds the homophily of all followers and the Media, normalized
	by the number of followers */

	int i;
	int n = mysys.nagents;
        int followers = 0;
        int edit_secc = mm.edit_secc;
        int edit_line = mm.edit_line;
	double hmm = 0.00;

	for(i = 0; i < n; i++)
        {
		if(mysys.agent[i].feat[edit_secc] == edit_line)
                {
	 		hmm += homophily_mm(mm, mysys.agent[i]);
                        followers++;
		}
	}

        if (followers != 0)
  		return (hmm / followers);
        else
        	return hmm;          
}		
