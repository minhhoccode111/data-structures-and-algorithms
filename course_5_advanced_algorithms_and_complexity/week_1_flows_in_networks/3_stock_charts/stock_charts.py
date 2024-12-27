# python3


# this problem is from the annual worldwide programming competition held by Google

# you will need to guess how to apply the algorithms from this module to find
# the most compact way of visualizing stock price data using charts


class StockCharts:
    def read_data(self):
        n, k = map(int, input().split())
        stock_data = [list(map(int, input().split())) for i in range(n)]
        return stock_data

    def write_response(self, result):
        print(result)

    def compare_stocks(self, stock1, stock2):
        return all(x < y for x, y in zip(stock1, stock2))

    def dfs(self, adj_matrix, u, visited, match):
        for v in range(len(adj_matrix[u])):
            if adj_matrix[u][v] and not visited[v]:
                visited[v] = True
                if match[v] == -1 or self.dfs(adj_matrix, match[v], visited, match):
                    match[v] = u
                    return True
        return False

    def max_bipartite_matching(self, adj_matrix):
        n = len(adj_matrix)
        match = [-1] * n
        result = 0

        for u in range(n):
            visited = [False] * n
            if self.dfs(adj_matrix, u, visited, match):
                result += 1

        return result

    def min_charts(self, stock_data):
        n = len(stock_data)
        adj_matrix = [[False] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if i != j and self.compare_stocks(stock_data[i], stock_data[j]):
                    adj_matrix[i][j] = True

        max_matching = self.max_bipartite_matching(adj_matrix)
        return n - max_matching

    def solve(self):
        stock_data = self.read_data()
        result = self.min_charts(stock_data)
        self.write_response(result)


if __name__ == "__main__":
    stock_charts = StockCharts()
    stock_charts.solve()
