
#ifndef REWIRING_H
#define REWIRING_H

#include <stdlib.h>
#include "axelrod.h"
#include "homophily.h"

struct _top_changes
{
	int *remove;
	int *add;
};
typedef struct _top_changes top_changes;

int rewiring(axl_network *mysys, axl_network_alloc *mysys_alloc);

#endif
