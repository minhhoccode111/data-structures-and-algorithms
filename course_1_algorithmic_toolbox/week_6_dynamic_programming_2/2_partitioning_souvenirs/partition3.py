from sys import stdin


def partition3(values):
    if not values or len(values) < 3:
        return 0

    total_sum = sum(values)
    if total_sum % 3 != 0:
        return 0

    target = total_sum // 3
    n = len(values)

    dp = [[[False] * (target + 1) for _ in range(target + 1)] for _ in range(n + 1)]

    dp[0][0][0] = True

    for i in range(1, n + 1):
        curr = values[i - 1]
        for s1 in range(target + 1):
            for s2 in range(target + 1):
                dp[i][s1][s2] = dp[i - 1][s1][s2]

                if s1 >= curr:
                    dp[i][s1][s2] |= dp[i - 1][s1 - curr][s2]

                if s2 >= curr:
                    dp[i][s1][s2] |= dp[i - 1][s1][s2 - curr]

                s3 = total_sum - s1 - s2
                if s3 >= curr:
                    dp[i][s1][s2] |= dp[i - 1][s1][s2]

    return 1 if dp[n][target][target] else 0


if __name__ == "__main__":
    input_n, *input_values = list(map(int, stdin.read().split()))
    assert input_n == len(input_values)
    print(partition3(input_values))
