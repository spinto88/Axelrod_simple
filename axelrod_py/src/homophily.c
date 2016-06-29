
#include "homophily.h"

double homophily(axl_agent a, axl_agent b, int opinion_included)
{
	int i;
	int f = a.f; /* Number of features.*/
	double hab = 0.00; /* Homophily.*/

	if(f == 0)
		return 1.00;
    
	/* Go over all features. */
	for(i = 0; i < f; i++)
	{
 		/* If a given feature is shared, the homophily increases. */
		if(a.feat[i] == b.feat[i])
			hab += 1.00;
	}

	if(opinion_included == 1)
	{
		if(a.opinion == b.opinion)
			hab += 1.00;
		return (hab / (f + 1));
	}
	else
	/* Return the normalized (respect to f) homophily. */
		return (hab / f);
}
