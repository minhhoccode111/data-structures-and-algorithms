import networkx as nx

grid = nx.MultiGraph(nx.grid_2d_graph(m=4, n=4))
grid = nx.eulerize(grid)
cycle = nx.eulerian_circuit(grid, source=(0, 0))
print("->".join(str(edge[0]) for edge in cycle))
