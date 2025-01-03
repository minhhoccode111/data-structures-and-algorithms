# python3


# apply an algorithm for finding maximum flow in a network to dedtermine how
# fast people can be evacuated from the given city


from collections import deque


class Edge:
    def __init__(self, u, v, capacity):
        self.u = u
        self.v = v
        self.capacity = capacity
        self.flow = 0


class FlowGraph:
    def __init__(self, n):
        self.edges = []
        self.graph = [[] for _ in range(n)]

    def add_edge(self, from_, to, capacity):
        forward_edge = Edge(from_, to, capacity)
        backward_edge = Edge(to, from_, 0)
        self.graph[from_].append(len(self.edges))
        self.edges.append(forward_edge)
        self.graph[to].append(len(self.edges))
        self.edges.append(backward_edge)

    def size(self):
        return len(self.graph)

    def get_ids(self, from_):
        return self.graph[from_]

    def get_edge(self, id):
        return self.edges[id]

    def add_flow(self, id, flow):
        self.edges[id].flow += flow
        self.edges[id ^ 1].flow -= flow


def read_data():
    vertex_count, edge_count = map(int, input().split())
    graph = FlowGraph(vertex_count)
    for _ in range(edge_count):
        u, v, capacity = map(int, input().split())
        graph.add_edge(u - 1, v - 1, capacity)
    return graph


def bfs(graph, from_, to, parent):
    visited = [False] * graph.size()
    queue = deque([from_])
    visited[from_] = True

    while queue:
        current = queue.popleft()

        for edge_id in graph.get_ids(current):
            edge = graph.get_edge(edge_id)

            if not visited[edge.v] and edge.capacity > edge.flow:
                queue.append(edge.v)
                visited[edge.v] = True
                parent[edge.v] = edge_id

                if edge.v == to:
                    return True

    return False


def max_flow(graph, from_, to):
    flow = 0

    parent = [-1] * graph.size()

    while bfs(graph, from_, to, parent):

        path_flow = float("Inf")
        current = to

        while current != from_:
            edge_id = parent[current]
            edge = graph.get_edge(edge_id)
            path_flow = min(path_flow, edge.capacity - edge.flow)
            current = edge.u

        current = to
        while current != from_:
            edge_id = parent[current]
            graph.add_flow(edge_id, path_flow)
            current = graph.get_edge(edge_id).u

        flow += path_flow

    return flow


if __name__ == "__main__":
    graph = read_data()
    print(max_flow(graph, 0, graph.size() - 1))
