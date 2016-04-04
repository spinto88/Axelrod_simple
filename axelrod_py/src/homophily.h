/*! \file homophily.h
    \brief Homophily functions.

    The homophily is the number of features that two axelrod
    agents share, divided by the total number of features.
*/

/*! \fn homophily(axl_agent a, axl_agent b)
    \brief Return the homophily between axelrod agent "a" and "b".
    \param a Axelrod agent.
    \param b Axelrod agent.
*/

/*! \fn homophily_mm(axl_mass_media mm, axl_agent a)
    \brief Equal to the homophily function, but between an axelrod mass media agent and an axelrod agent a.
    \param mm Axelrod mass media agent.
    \param a Axelrod agent.
*/

#ifndef HOMOPHILY_H
#define HOMOPHILY_H

#include "axelrod.h"

double homophily(axl_agent, axl_agent);

#endif
