
#include "homophily.h"

double homophily(axl_agent a, axl_agent b)
{
	int i;
	int f = a.f; /* Number of features.*/
	double hab = 0.00; /* Homophily.*/

	/* Go over all features. */
	for(i = 0; i < f; i++)
	{
 		/* If a given feature is shared, the homophily increases. */
		if(a.feat[i] == b.feat[i])
			hab += 1.00;
	}
	/* Return the normalized (respect to f) homophily. */
	return (hab / f);
}

double homophily_mm(axl_mass_media mm, axl_agent a)
{
	/* Equal function but with a mass media as argument */
	int i;
        int f = mm.f;
        double hma = 0.00;
 
        for(i = 0; i < f; i++)
	{
		if(mm.feat[i] == a.feat[i])
			hma += 1.00;
	}

	return (hma / f);
}

