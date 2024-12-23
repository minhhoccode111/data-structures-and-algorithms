# python3

# find the maximum value of items that fits into the backpack

# to read input directly fromo standard input
from sys import stdin


def optimal_value(capacity, weights, values):
    # base case if nothing left
    if capacity == 0 or len(weights) == 0:
        return 0
    # the amount of the first item that can be taken
    # full backpack capacity vs full weight of first item
    amount = min(capacity, weights[0])
    # calculate the value will be add to total of the first item
    value = values[0] * amount / weights[0]
    # recursively calculate the value for the remaining capacity and items
    # and remove the first item from the weights and values list
    return value + optimal_value(capacity - amount, weights[1:], values[1:])


if __name__ == "__main__":
    # read input data and convert to int
    data = list(map(int, stdin.read().split()))
    # extract n and capacity
    n, capacity = data[0:2]
    # extract values
    values = data[2 : (2 * n + 2) : 2]
    # extract weights
    weights = data[3 : (2 * n + 2) : 2]
    # pair values and weights into tuples
    items = list(zip(values, weights))
    # sort items by value/weight ratio in descending order
    items.sort(key=lambda x: x[0] / x[1], reverse=True)
    # unzip back to values and weights
    values, weights = zip(*items)
    # convert back to list
    values = list(values)
    weights = list(weights)
    # print the right format of the calculated optimal value
    print("{:.4f}".format(optimal_value(capacity, weights, values)))
