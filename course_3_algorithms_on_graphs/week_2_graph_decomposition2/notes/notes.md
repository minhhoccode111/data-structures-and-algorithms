# Directed Graphs

DAG: Directed Acyclic Graph
source: a vertex with no incoming edges
sink: a vertex with no outgoing edges

## Finding all nodes reachable from a particular node

```
explore(G,v)
input: G = (V,E) is a graph; v in V
output: visited(u) is set to true for all nodes u reachable from v

visited(v) = true
previsit(v)
for each edge (v, u) in E:
  if not visited(u):
    explore(G, u)
postvisit(v)
```

## Depth-first search

```
dfs(G)

for all v in V:
  visited(v) = false

for all v in V:
  if not visited(v):
    explore(G,v)
```

## Generate arrays `pre` and `post`

By define a simple counter `clock` init set to 1, which gets updated as follow

```
previsit(v)
pre[v] = clock
clock = clock + 1
```

```
postvisit(v)
post[v] = clock
clock = clock + 1
```

**Property**: For any nodes `u` and `v`, the two intervals [pre[u], post[u]] and [pre[v], post[v]] are either disjoint or one is contained within the other
