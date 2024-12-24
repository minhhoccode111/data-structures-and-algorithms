# python3

# compute the maximum length of a common subsequencec of two sequences


def lcs2(first_sequence, second_sequence):
    # Create a matrix with dimensions (n+1) x (m+1) initialized with zeros
    n, m = len(first_sequence), len(second_sequence)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Fill the dp matrix
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if first_sequence[i - 1] == second_sequence[j - 1]:
                # If characters match, add 1 to the diagonal value
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                # If characters don't match, take maximum of left and up cells
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Return the value in the bottom-right cell
    return dp[n][m]


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n
    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m
    print(lcs2(a, b))
