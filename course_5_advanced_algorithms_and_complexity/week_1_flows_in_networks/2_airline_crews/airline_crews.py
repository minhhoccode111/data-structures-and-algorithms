# python3


# apply an algorithm for finding maximum matching in a bipartite graph to assign
# airline crews to flights in the most efficient way


class MaxMatching:
    def read_data(self):
        n, m = map(int, input().split())
        adj_matrix = [list(map(int, input().split())) for _ in range(n)]
        return n, m, adj_matrix

    def write_response(self, matching):
        line = [str(-1 if x == -1 else x + 1) for x in matching]
        print(" ".join(line))

    def find_matching(self, n, m, adj_matrix):
        def dfs(flight, visited, match):
            for crew in range(m):
                if adj_matrix[flight][crew] and not visited[crew]:
                    visited[crew] = True
                    if match[crew] == -1 or dfs(match[crew], visited, match):
                        match[crew] = flight
                        return True
            return False

        match = [-1] * m
        for flight in range(n):
            visited = [False] * m
            dfs(flight, visited, match)

        matching = [-1] * n
        for crew in range(m):
            if match[crew] != -1:
                matching[match[crew]] = crew
        return matching

    def solve(self):
        n, m, adj_matrix = self.read_data()
        matching = self.find_matching(n, m, adj_matrix)
        self.write_response(matching)


if __name__ == "__main__":
    max_matching = MaxMatching()
    max_matching.solve()
