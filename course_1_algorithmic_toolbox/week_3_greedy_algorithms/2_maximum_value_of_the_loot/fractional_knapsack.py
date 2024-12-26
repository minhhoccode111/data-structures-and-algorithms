# python3

# find the maximum value of items that fits into the backpack

from sys import stdin


def optimal_value(capacity, weights, values):
    if capacity == 0 or len(weights) == 0:
        return 0
    amount = min(capacity, weights[0])
    value = values[0] * amount / weights[0]
    return value + optimal_value(capacity - amount, weights[1:], values[1:])


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2 : (2 * n + 2) : 2]
    weights = data[3 : (2 * n + 2) : 2]
    items = list(zip(values, weights))
    items.sort(key=lambda x: x[0] / x[1], reverse=True)
    values, weights = zip(*items)
    values = list(values)
    weights = list(weights)
    print("{:.4f}".format(optimal_value(capacity, weights, values)))
