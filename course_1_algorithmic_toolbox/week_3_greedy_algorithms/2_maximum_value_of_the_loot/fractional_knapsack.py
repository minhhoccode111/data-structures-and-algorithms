from sys import stdin


# already sorted the most expensive item in values list
def optimal_value(capacity, weights, values):
    # if capacity = 0 or weights list is empty
    if capacity == 0 or len(weights) == 0:
        return 0

    # the mount we will stole, either full capacity or full weight of current item
    amount = min(capacity, weights[0])
    value = values[0] * amount / weights[0]

    # slice from the second element to the end of both weights and values lists
    return value + optimal_value(capacity - amount, weights[1:], values[1:])


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2 : (2 * n + 2) : 2]
    weights = data[3 : (2 * n + 2) : 2]
    # pair up values and weights
    items = list(zip(values, weights))
    # sort by price per pound (value/weight) in desc order
    items.sort(key=lambda x: x[0] / x[1], reverse=True)
    # unzip the sorted items back into values and weights
    values, weights = zip(*items)
    # convert back to lists
    values = list(values)
    weights = list(weights)
    opt_value = optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
