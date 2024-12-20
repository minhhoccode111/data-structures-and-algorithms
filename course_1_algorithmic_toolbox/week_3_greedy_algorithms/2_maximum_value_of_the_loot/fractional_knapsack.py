# python3

# find the maximum value of items that fits into the backpack

from sys import stdin  # Import stdin to read input directly from standard input


def optimal_value(capacity, weights, values):
    # Base case: if no capacity or no items left, return 0
    if capacity == 0 or len(weights) == 0:
        return 0
    # Calculate the amount of the first item's weight that can be taken
    amount = min(capacity, weights[0])
    # Calculate the value derived from the taken portion of the first item
    value = values[0] * amount / weights[0]
    # Recursively calculate the value for the remaining capacity and items
    return value + optimal_value(capacity - amount, weights[1:], values[1:])


if __name__ == "__main__":
    # Read input data and convert it to integers
    data = list(map(int, stdin.read().split()))
    # Extract the number of items and backpack capacity
    n, capacity = data[0:2]
    # Extract the values of the items
    values = data[2 : (2 * n + 2) : 2]
    # Extract the weights of the items
    weights = data[3 : (2 * n + 2) : 2]
    # Pair values and weights into tuples
    items = list(zip(values, weights))
    # Sort items by value-to-weight ratio in descending order for a greedy approach
    items.sort(key=lambda x: x[0] / x[1], reverse=True)
    # Unzip sorted items into separate lists for values and weights
    values, weights = zip(*items)
    # Convert the tuples to lists for further processing
    values = list(values)
    weights = list(weights)
    # Calculate the optimal value of items that can fit into the backpack
    opt_value = optimal_value(capacity, weights, values)
    # Print the optimal value formatted to four decimal places
    print("{:.4f}".format(opt_value))
