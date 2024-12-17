# python3


"""

diff <(python3 evacuation.py < tests/01) <(cat tests/01.a)
diff <(python3 evacuation.py < tests/02) <(cat tests/02.a)
diff <(python3 evacuation.py < tests/03) <(cat tests/03.a)
diff <(python3 evacuation.py < tests/04) <(cat tests/04.a)
diff <(python3 evacuation.py < tests/05) <(cat tests/05.a)
diff <(python3 evacuation.py < tests/06) <(cat tests/06.a)
diff <(python3 evacuation.py < tests/07) <(cat tests/07.a)
diff <(python3 evacuation.py < tests/08) <(cat tests/08.a)
diff <(python3 evacuation.py < tests/09) <(cat tests/09.a)
diff <(python3 evacuation.py < tests/10) <(cat tests/10.a)
diff <(python3 evacuation.py < tests/11) <(cat tests/11.a)
diff <(python3 evacuation.py < tests/12) <(cat tests/12.a)
diff <(python3 evacuation.py < tests/13) <(cat tests/13.a)
diff <(python3 evacuation.py < tests/14) <(cat tests/14.a)
diff <(python3 evacuation.py < tests/15) <(cat tests/15.a)
diff <(python3 evacuation.py < tests/16) <(cat tests/16.a)
diff <(python3 evacuation.py < tests/17) <(cat tests/17.a)
diff <(python3 evacuation.py < tests/18) <(cat tests/18.a)
diff <(python3 evacuation.py < tests/19) <(cat tests/19.a)
diff <(python3 evacuation.py < tests/20) <(cat tests/20.a)
diff <(python3 evacuation.py < tests/21) <(cat tests/21.a)
diff <(python3 evacuation.py < tests/22) <(cat tests/22.a)
diff <(python3 evacuation.py < tests/23) <(cat tests/23.a)
diff <(python3 evacuation.py < tests/24) <(cat tests/24.a)
diff <(python3 evacuation.py < tests/25) <(cat tests/25.a)
diff <(python3 evacuation.py < tests/26) <(cat tests/26.a)
diff <(python3 evacuation.py < tests/27) <(cat tests/27.a)
diff <(python3 evacuation.py < tests/28) <(cat tests/28.a)
diff <(python3 evacuation.py < tests/29) <(cat tests/29.a)
diff <(python3 evacuation.py < tests/30) <(cat tests/30.a)
diff <(python3 evacuation.py < tests/31) <(cat tests/31.a)
diff <(python3 evacuation.py < tests/32) <(cat tests/32.a)
diff <(python3 evacuation.py < tests/33) <(cat tests/33.a)
diff <(python3 evacuation.py < tests/34) <(cat tests/34.a)
diff <(python3 evacuation.py < tests/35) <(cat tests/35.a)
diff <(python3 evacuation.py < tests/36) <(cat tests/36.a)

"""


from collections import deque


class Edge:

    def __init__(self, u, v, capacity):
        self.u = u
        self.v = v
        self.capacity = capacity
        self.flow = 0


# This class implements a bit unusual scheme for storing edges of the graph,
# in order to retrieve the backward edge for a given edge quickly.
class FlowGraph:

    def __init__(self, n):
        # List of all - forward and backward - edges
        self.edges = []
        # These adjacency lists store only indices of edges in the edges list
        self.graph = [[] for _ in range(n)]

    def add_edge(self, from_, to, capacity):
        # Note that we first append a forward edge and then a backward edge,
        # so all forward edges are stored at even indices (starting from 0),
        # whereas backward edges are stored at odd indices.
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
        # To get a backward edge for a true forward edge (i.e id is even), we
        # should get id + 1 due to the described above scheme. On the other
        # hand when we have to get a "backward" edge for a backward edge (i.e.
        # get a forward edge for backward - id is odd), id - 1 should be taken

        # It turns out that id ^ 1 works for both cases. Think this through!
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
    """
    Perform a BFS to find an augmenting path.
    Returns True if there is a path from `from_` to `to`.
    """
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


# NOTE: code go here
def max_flow(graph, from_, to):
    flow = 0

    parent = [-1] * graph.size()

    # While there exists an augmenting path
    while bfs(graph, from_, to, parent):
        # Find the maximum flow we can push through the found path
        path_flow = float("Inf")
        current = to

        while current != from_:
            edge_id = parent[current]
            edge = graph.get_edge(edge_id)
            path_flow = min(path_flow, edge.capacity - edge.flow)
            current = edge.u

        # Update the flow values along the path
        current = to
        while current != from_:
            edge_id = parent[current]
            graph.add_flow(edge_id, path_flow)
            current = graph.get_edge(edge_id).u

        # Add path flow to the total flow
        flow += path_flow

    return flow


if __name__ == "__main__":
    graph = read_data()
    print(max_flow(graph, 0, graph.size() - 1))
