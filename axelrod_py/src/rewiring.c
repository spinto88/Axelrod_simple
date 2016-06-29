
#include "rewiring.h"

/* The criteria of change a neighbour is that the homophily with the older is less 
   than with the new neighbour. But this only takes only opinion links */

int agent_in_list(axl_network *, int, int);

void rewiring(axl_network *mysys, int seed)
{
	int i, j;
	int ind_old;
	int new, old;
	int agent;
	int n = mysys->nagents;
	double h_new, h_old;

	int *list_agents;

	srand(seed);

	list_agents = (int *)malloc(sizeof(int) * n);

	for(i = 0; i < n; i++)
		list_agents[i] = i;

	for(i = 0; i < n; i++)
	{
		j = rand() % n;
		swap(list_agents + i, list_agents + j);
	}

	for(i = 0; i < n; i++)
	{
		agent = list_agents[i];

		if(mysys->agent[agent].opinion_degree > 0)
		{

			ind_old = rand() % mysys->agent[agent].opinion_degree;
			old = mysys->agent[agent].opinion_links[ind_old];	
			
			new = rand() % n;
			while(agent_in_list(mysys, agent, new) == 1)
				new = rand() % n;

			h_old = homophily(mysys->agent[agent], mysys->agent[old], mysys->opinion_included);
			h_new = homophily(mysys->agent[agent], mysys->agent[new], mysys->opinion_included);	

			if(h_new > h_old)
			{
				for(j = 0; j < mysys->agent[old].opinion_degree; j++)
				{
					if(mysys->agent[old].opinion_links[j] == agent)
					{

						swap(&mysys->agent[old].opinion_links[j], &mysys->agent[old].opinion_links[mysys->agent[old].opinion_degree - 1]);
						mysys->agent[old].opinion_links[mysys->agent[old].opinion_degree - 1] = -1;
						mysys->agent[old].opinion_degree -= 1;

				                mysys->agent[agent].opinion_links[ind_old] = new;

          				        mysys->agent[new].opinion_links[mysys->agent[new].opinion_degree] = agent;
      				                mysys->agent[new].opinion_degree += 1;
						break;
					}
				}
			}
		}

	}

	free(list_agents);

	return;
}


int agent_in_list(axl_network *mysys, int agent, int new)
{
	int i;

	for(i = 0; i < mysys->agent[agent].contact_degree; i++)
	{
		if(new == mysys->agent[agent].contact_links[i])
			return 1;
	}

	for(i = 0; i < mysys->agent[agent].opinion_degree; i++)
	{
		if(new == mysys->agent[agent].opinion_links[i])
			return 1;
	}

	if(agent == new)
		return 1;

	return 0;
}
