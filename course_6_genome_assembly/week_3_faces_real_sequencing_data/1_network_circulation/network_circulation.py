# python3


# Given a directed graph with lower and upper bounds on edge capacities,
# determine if a valid flow (circulation) exists that satisfies these bounds
# and flow conservation at each vertex, outputting "YES" and the flow values if
# it does, or "NO" otherwise

from collections import deque
from random import randint, choice


class NetworkEdge:
    def __init__(self, vertex_from, vertex_to, capacity):
        self.source = vertex_from
        self.target = vertex_to
        self.max_capacity = capacity
        self.current_flow = 0

    def __str__(self):
        return "NetworkEdge(source={}, target={}, max_capacity={}, current_flow={})".format(
            self.source + 1, self.target + 1, self.max_capacity, self.current_flow
        )

    def __repr__(self):
        return "\nNetworkEdge(source={}, target={}, max_capacity={}, current_flow={})".format(
            self.source + 1, self.target + 1, self.max_capacity, self.current_flow
        )


class ResidualNetwork:
    MAX_FLOW = 10**6

    def __init__(self, vertex_count):
        self.vertices = vertex_count
        self.edge_list = []
        self.adjacency = [[] for _ in range(vertex_count)]

    def insert_edge(self, vertex_from, vertex_to, capacity):
        forward = NetworkEdge(vertex_from, vertex_to, capacity)
        backward = NetworkEdge(vertex_to, vertex_from, 0)
        self.adjacency[vertex_from].append(len(self.edge_list))
        self.edge_list.append(forward)
        self.adjacency[vertex_to].append(len(self.edge_list))
        self.edge_list.append(backward)

    def discover_path(self, vertex_from, vertex_to):
        edge_trace = [None] * self.vertices
        visited = [False] * self.vertices
        visited[vertex_from] = True
        queue = deque([vertex_from])

        while queue:
            current = queue.popleft()
            if current == vertex_to:
                break

            for edge_idx in self.adjacency[current]:
                edge = self.edge_list[edge_idx]
                if (not visited[edge.target]) and (
                    edge.current_flow < edge.max_capacity
                ):
                    queue.append(edge.target)
                    edge_trace[edge.target] = edge_idx
                    visited[edge.target] = True

        result = None
        if edge_trace[vertex_to] is not None:
            result = []
            vertex = vertex_to
            while vertex != vertex_from:
                edge_idx = edge_trace[vertex]
                result.append(edge_idx)
                vertex = self.edge_list[edge_idx].source
            result = result[::-1]
        return result

    def compute_max_flow(self, source, sink):
        while True:
            path = self.discover_path(source, sink)
            if path is None:
                break

            bottleneck = ResidualNetwork.MAX_FLOW
            for edge_idx in path:
                edge = self.edge_list[edge_idx]
                bottleneck = min(bottleneck, edge.max_capacity - edge.current_flow)

            for edge_idx in path:
                if edge_idx % 2 == 0:
                    self.edge_list[edge_idx].max_capacity -= bottleneck
                    self.edge_list[edge_idx + 1].max_capacity += bottleneck
                else:
                    self.edge_list[edge_idx - 1].max_capacity += bottleneck
                    self.edge_list[edge_idx].max_capacity -= bottleneck

        for i in range(len(self.edge_list) // 2):
            self.edge_list[i * 2].current_flow = self.edge_list[i * 2 + 1].max_capacity
            self.edge_list[i * 2].max_capacity += self.edge_list[i * 2 + 1].max_capacity


class CirculationEdge:
    def __init__(self, vertex_from, vertex_to, min_flow, max_flow):
        self.source = vertex_from
        self.target = vertex_to
        self.min_flow = min_flow
        self.max_flow = max_flow
        self.current_flow = 0


class CirculationSolver:
    def __init__(self, vertex_count, edges):
        self.vertex_count = vertex_count
        self.edges = edges
        self.edge_count = len(edges)

    def validate_flow(self, vertex_count, edges):
        inbound = [[] for _ in range(vertex_count)]
        outbound = [[] for _ in range(vertex_count)]
        for idx, edge in enumerate(edges):
            inbound[edge.target].append(idx)
            outbound[edge.source].append(idx)

        for vertex in range(vertex_count):
            incoming = sum(edges[i].current_flow for i in inbound[vertex])
            outgoing = sum(edges[i].current_flow for i in outbound[vertex])
            if incoming != outgoing:
                return False

        for edge in edges:
            if not (edge.min_flow <= edge.current_flow <= edge.max_flow):
                return False
        return True

    def check_trivial(self):
        saved_flows = []
        for edge in self.edges:
            saved_flows.append(edge.current_flow)
            edge.current_flow = edge.min_flow

        result = self.validate_flow(self.vertex_count, self.edges)

        for idx, edge in enumerate(self.edges):
            edge.current_flow = saved_flows[idx]
        return result

    def solve(self):
        if self.check_trivial():
            solution = []
            for edge in self.edges:
                edge.current_flow = edge.min_flow
                solution.append(edge.current_flow)
            return solution

        network = ResidualNetwork(self.vertex_count + 2)
        for edge in self.edges:
            network.insert_edge(edge.source, edge.target, edge.max_flow - edge.min_flow)

        inbound = [[] for _ in range(self.vertex_count)]
        outbound = [[] for _ in range(self.vertex_count)]
        for idx, edge in enumerate(self.edges):
            inbound[edge.target].append(idx)
            outbound[edge.source].append(idx)

        vertex_balance = [0] * self.vertex_count
        for vertex in range(self.vertex_count):
            vertex_balance[vertex] -= sum(
                self.edges[i].min_flow for i in inbound[vertex]
            )
            vertex_balance[vertex] += sum(
                self.edges[i].min_flow for i in outbound[vertex]
            )

        super_source = self.vertex_count
        super_sink = self.vertex_count + 1

        for vertex in range(self.vertex_count):
            balance = vertex_balance[vertex]
            if balance < 0:
                network.insert_edge(super_source, vertex, abs(balance))
            elif balance > 0:
                network.insert_edge(vertex, super_sink, balance)

        network.compute_max_flow(super_source, super_sink)

        for edge in network.edge_list:
            if (
                edge.source == super_source or edge.target == super_sink
            ) and edge.current_flow != edge.max_capacity:
                return None

        solution = []
        for idx, edge in enumerate(self.edges):
            edge.current_flow = edge.min_flow + network.edge_list[idx * 2].current_flow
            solution.append(edge.current_flow)
        return solution


def main():
    vertex_count, edge_count = map(int, input().split())
    edges = []
    for _ in range(edge_count):
        v1, v2, low, cap = map(int, input().split())
        edges.append(CirculationEdge(v1 - 1, v2 - 1, low, cap))

    solution = CirculationSolver(vertex_count, edges).solve()
    if solution is not None:
        print("YES")
        for flow in solution:
            print(flow)
    else:
        print("NO")


if __name__ == "__main__":
    main()
