import networkx as nx

# construct a graph
graph = nx.Graph([(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4), (3, 5), (4, 5)])
print(nx.eulerian_path(graph))
