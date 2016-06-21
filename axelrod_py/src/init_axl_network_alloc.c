
#include "init_axl_network_alloc.h"

void init_axl_network_alloc(axl_network *mysys, axl_network_alloc *mysys_alloc)
{
    int i, j;
    int n;
    
    n = mysys->nagents;
    
    mysys_alloc->agent_alloc = (axl_agent_alloc *)malloc(sizeof(axl_agent_alloc) * n);
    
    for(i = 0; i < n; i++)
    {
        mysys_alloc->agent_alloc[i].neighbors_alloc = (int *)malloc(sizeof(int)*mysys->agent[i].degree);
        
        for(j = 0; j < mysys->agent[i].degree; j++)
        {
            mysys_alloc->agent_alloc[i].neighbors_alloc[j] = mysys->agent[i].neighbors[j];
        }
        
        mysys_alloc->agent_alloc[i].contact_links_alloc = (int *)malloc(sizeof(int)*mysys->agent[i].degree_contact);     
        
        for(j = 0; j < mysys->agent[i].degree_contact; j++)
        {
            mysys_alloc->agent_alloc[i].contact_links_alloc[j] = mysys->agent[i].contact_links[j];
        }
        
        mysys_alloc->agent_alloc[i].opinion_links_alloc = (int *)malloc(sizeof(int)*mysys->agent[i].degree_opinion); 
        
        for(j = 0; j < mysys->agent[i].degree_opinion; j++)
        {
            mysys_alloc->agent_alloc[i].opinion_links_alloc[j] = mysys->agent[i].opinion_links[j];
        }
        
    }
    
    

}
