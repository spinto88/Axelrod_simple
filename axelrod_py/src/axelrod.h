
#ifndef AXL_AGENT
#define AXL_AGENT
/*!
  Axelrod agent:
  An axelrod agent is caracterized by 
  a cultural vector with f components
  with represent the cultural features.
  Each feature can adopt q integer values,
  which represent the traits of a feature.
*/
struct _axl_agent
{
	int f; /*!< Number of features.*/
	int q; /*!< Number of traits per feature.*/
	int *feat; /*!< Cutural vector with f components.*/
};
typedef struct _axl_agent axl_agent; /*!< struct _axl_agent redefined as axl_agent. */
#endif


#ifndef AXL_NODE
#define AXL_NODE
/**
Axelrod node: it has information
about the degree of the node 
and the list of neighbors
*/
struct _axl_node
{
	int degree;
        int label;
	int *neighbors;
};
typedef struct _axl_node axl_node;
#endif


#ifndef AXL_NETWORK
#define AXL_NETWORK
/** 
Axelrod network with n agents
*/

struct _axl_network
{
	int nagents;
	axl_agent *agent;
        double noise;
};
typedef struct _axl_network axl_network;
#endif
