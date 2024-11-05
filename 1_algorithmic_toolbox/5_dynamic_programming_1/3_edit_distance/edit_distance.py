def edit_distance(s: str, t: str) -> int:
    n, m = len(s), len(t)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    # state transition: first row and first column
    for i in range(1, n + 1):
        dp[i][0] = i
    for j in range(1, m + 1):
        dp[0][j] = j
    # state transition: the rest of the rows and columns
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s[i - 1] == t[j - 1]:
                # if the two characters are equal, skip these two characters
                dp[i][j] = dp[i - 1][j - 1]
            else:
                # the minimum number of edits = the minimum number of edits
                # from three operations (insert, remove, replace) + 1
                dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
    # return the last position
    return dp[n][m]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
