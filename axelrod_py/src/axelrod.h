
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
	int q_z;
	double fraction; /*Change a feature A with metric to a value in a fraction of the distance between A and B, from neighbour B. fraction = 0 normal axelrod */
	int *feat; /*!< Cutural vector with f components.*/
	double zealot;
	int vaccine;
	int degree; /* Degree of the node */
	int label; /* Label useful for the fragment identifier */
	int *neighbors; /* List of neighbors */
	int degree_contact; /* Degree of the list of contact neighbors */
	int *contact_links; /* List of neighbors which are contact links */
	int degree_opinion; /* Degree of the list of only opinion neighbors */
	int *opinion_links; /* List of neighbors which are opinion links */
};
typedef struct _axl_agent axl_agent; /*!< struct _axl_agent redefined as axl_agent. */
#endif

#ifndef AXL_MASS_MEDIA
#define AXL_MASS_MEDIA
/* Axelrod Mass Media
*/
struct _axl_mass_media
{
	int f; // Number of features
	int q; // Number of traits per feature
	int *feat; // Cultural vector
	double b; // Strengh of the media
	int strategy; // Strategy of adaptation
	int edit_secc; // Editorial section: feature which doesn't change
	int edit_line; // Trait of the editorial section
};
typedef struct _axl_mass_media axl_mass_media;
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
        int number_of_metric_feats; /* This is the number of features which are metric. If it's larger than f, it means that all features are metric */
        axl_mass_media mass_media;
        double b;
        int mode_mf; /*1 active, 0 inactive*/
};
typedef struct _axl_network axl_network;
#endif



