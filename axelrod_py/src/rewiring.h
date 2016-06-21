
#ifndef REWIRING_H
#define REWIRING_H

#include <stdlib.h>
#include "axelrod.h"
#include "homophily.h"

struct _top_changes
{
	int remove;
	int add;
};
typedef struct _top_changes top_changes;

void rewiring(axl_network *mysys, top_changes *, axl_network_alloc *mysys_alloc);

#endif
