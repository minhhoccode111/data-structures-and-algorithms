# python3

# given a set of gold bars of various weights and a backpack that can hold at
# most W pounds, place as much gold as possible into the backpack


def maximum_gold(W, weights):
    n = len(weights)
    K = [[0] * (W + 1) for _ in range(n + 1)]

    for w in range(1, W + 1):
        for i in range(0, n):
            if weights[i] > w:
                K[i][w] = K[i - 1][w]
            else:
                K[i][w] = max(K[i - 1][w], K[i - 1][w - weights[i]] + weights[i])

    return K[n - 1][W]


if __name__ == "__main__":
    capacity, n = list(map(int, input().split()))
    weights = list(map(int, input().split()))
    assert len(weights) == n

    print(maximum_gold(capacity, weights))
