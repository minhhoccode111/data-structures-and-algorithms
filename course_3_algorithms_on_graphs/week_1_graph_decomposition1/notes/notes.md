# Graph Decomposition 1

## Formal Description

```
Reachability
input: Graph G and vertex s
output: The collection of vertices v of G so that there is a path from s to v
```

## Pseudocode

```
Components(s)
DiscoveredNodes = {s}
while there is an edge e leaving
DiscoveredNodes that has not been explored:
    add vertex at other end of e to DiscoveredNodes
return DiscoveredNodes
```

```
Explore(v)
visited(v) = true
for (v,w) in E:
    if not visited(w):
        Explore(w)
```

## Proof

- Onlye explores things reachable from v
- w not marked as visited unless explored
- if w explored, all neighbors explored
- u reachable from v by path
- Assume w furthest along path explored
- Must explore next item

## Runtime

Number of calls to explore:

- Each explored vertex is marked visited
- No vertex is explored after visited once
- Each vertex is explored at most once

## Connected Components

```
Theorem
The vertices of a graph G can be partitioned into connected components so that v is reachable from w iff they are in the same connected component
```

## Modification of Explore

```
Explore(v)
visited(v) = true
CCnum(v) = cc
for (v,w) in E:
  if not visted(w):
    Explore(w)
```

## Modification of DFS

```
DFS(G)
for all v in V mark v unvisited
cc = 1
for v in V:
  if not visited(v):
    Explore(v)
      cc++
```

Previsit and Postvisit functions

```
Explore(v)
visited(v) = true
previsit(v)
for (v,w) in E:
  if not visited(w):
    Explore(w)
postvisit(v)
```

## Clock

- Keep trach of order of visit
- Clock ticks at each pre-/post- visit
- Records previsit and postvisit times for each v

## Computing Pre- and Post- numbers

```
previsit(v)
clock = 1
pre(v) = clock
clock = clock + 1
```

```
postvisit(v)
clock = 1
post(v) = clock
clock = clock + 1
```
