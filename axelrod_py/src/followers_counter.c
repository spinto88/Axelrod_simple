
#include "followers_counter.h"

int followers_counter(axl_mass_media mm, axl_network mysys)
{
	int i;
	int n = mysys.nagents;
	int edit_secc = mm.edit_secc;
	int edit_line = mm.edit_line;
        int followers = 0;

	for(i = 0; i < n; i++)
	{
		if(mysys.agent[i].feat[edit_secc] == edit_line)
			followers++;
	}

	return followers;
}	
