## General Problem: 
NYC’s public transportation system (subway + bus) largely functions using a hub and spoke model, centralized in central / lower Manhattan (see GRAPH A).
While this system made sense when jobs & people were concentrated in central / lower Manhattan (below 59th st.), as jobs and people both have moved to the outer-boroughs, it makes less sense. 
When we look at the demographics of WHO lives in the outer-boroughs and what types of jobs are moving, there is some story there about the public transportation disproportionately affecting lower income residents of color...
How can we use networks to model this reality? 

## (1)
We can ask: **do buses address the lack of connectivity observed in the subway system?** 
First and foremost, there are barely any inter-borough buses which is a problem in and of itself. Moreover, the select bus service (which is supposed to address issues of speed and connectivity) doesn't have a single cross-borough line...
We can build two graphs, one where bus routes are included and one where they aren't, for each neighborhood. This can then be scaled up for all of NYC. 
For each graph, we can use the following measure and see how it changes as the network "grows" (meaning, as the bus routes are added).

vertices: stations
edges: whether or not these two stations are connected by a line
(1) Measure the degree of connectivity relative to how much the network could be connected if all stations were connected
y = e / e_max = e / 2v - 4 (for networks that have 2 or more lines in some vertices)

## (2)
or (and this question is more interconnected with social science / public policy research) we can ask: **does the transportation system effectively get outer-borough residents to and from work?**
While the MTA collects data on who enters a station (turnstile data), it has no collection process for where people go or where they get off. Thus, we can't really quantiatively build a model that depicts what routes are most common. 
However, several reports have used interviews to try and figure out where people need to be going, and with the development of real time GPS feeds, maybe this data becomes available

Regardless, if there is a set of "routes" with origin and destination points for the vertices, and the edges are the possible paths (the subway or bus routes) to get from some origin to some destination, it could result in a really cool & socially relevant network. 
The edges can then be weighted with the following attributes:
1. Average ride time 
2. Variance of ride time

We could then see how certain "routes" are significantly more efficient or just easier to do than others. This type of network makes sense only if the assumptions made at the outset, about which routes are relevant and what "sample" routes could represent a larger population, are sound. 

