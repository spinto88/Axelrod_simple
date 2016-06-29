
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
        int ff; /* Fix features */
	int q; /*!< Number of traits per feature.*/
	int q_z; /* Maximmun value of the opinion */
	int opinion; /* Opinion about vaccinated */
	int *feat; /*!< Cutural vector with f components.*/
	double zealot; /* Probability to be zealot */
	int vaccine; /* To vaccine or not to vaccine, that is the cuestion...*/
	int label; /* Label useful for the fragment identifier */
	int contact_degree; /* Degree of the list of contact neighbors */
	int *contact_links; /* List of neighbors which are contact links */
	int opinion_degree; /* Degree of the list of only opinion neighbors */
	int *opinion_links; /* List of neighbors which are opinion links */
};
typedef struct _axl_agent axl_agent; /*!< struct _axl_agent redefined as axl_agent. */
#endif

#ifndef AXL_NETWORK
#define AXL_NETWORK
/** 
Axelrod network with n agents
*/

struct _axl_network
{
	int nagents; /* Number of axelrod agents in the network */
	axl_agent *agent; /* Vector of axelrod agents */
        double noise; /* Rate of noise */
        double phi;
	int evol_opinion;
	int opinion_included;
	int rewiring;
};
typedef struct _axl_network axl_network;
#endif
