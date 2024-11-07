def maximum_gold(W, weights):
    n = len(weights)
    # need n + 1 because there's 1 row with 0s when n is 0
    K = [[0] * (W + 1) for _ in range(n + 1)]

    # the actual current capacity
    for w in range(1, W + 1):
        # the index of current gold weight
        for i in range(0, n):
            # if current gold weight is greater than current capacity
            if weights[i] > w:
                # then use the previous gold weight, in this same column capacity
                K[i][w] = K[i - 1][w]
            else:
                # else choose the maximum between previous weight and
                K[i][w] = max(K[i - 1][w], K[i - 1][w - weights[i]] + weights[i])

    # print(K)
    return K[n - 1][W]


if __name__ == "__main__":
    capacity, n = list(map(int, input().split()))
    weights = list(map(int, input().split()))
    assert len(weights) == n

    # print(capacity)
    # print(n)
    # print(weights)

    print(maximum_gold(capacity, weights))
