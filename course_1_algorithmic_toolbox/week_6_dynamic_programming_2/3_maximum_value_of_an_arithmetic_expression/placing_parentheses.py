def evaluate(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    else:
        assert False


def maximum_value(dataset):
    # extract numbers and operators
    numbers = []
    operators = []

    # parse the input string
    for i in range(len(dataset)):
        if i % 2 == 0:
            numbers.append(int(dataset[i]))
        else:
            operators.append(dataset[i])

    n = len(numbers)

    # initialize DP tables for max and min values
    max_dp = [[-float("inf")] * n for _ in range(n)]
    min_dp = [[float("inf")] * n for _ in range(n)]

    # initialize diagonal (single numbers)
    for i in range(n):
        max_dp[i][i] = numbers[i]
        min_dp[i][i] = numbers[i]

    # fill dp tables
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1

            for k in range(i, j):
                # get current operator
                op = operators[k]

                # calculate all possible combinations
                vals = [
                    evaluate(max_dp[i][k], max_dp[k + 1][j], op),
                    evaluate(max_dp[i][k], min_dp[k + 1][j], op),
                    evaluate(min_dp[i][k], max_dp[k + 1][j], op),
                    evaluate(min_dp[i][k], min_dp[k + 1][j], op),
                ]

                # update max and min values
                max_dp[i][j] = max(max_dp[i][j], max(vals))
                min_dp[i][j] = min(min_dp[i][j], min(vals))

    return max_dp[0][n - 1]


if __name__ == "__main__":
    print(maximum_value(input()))
