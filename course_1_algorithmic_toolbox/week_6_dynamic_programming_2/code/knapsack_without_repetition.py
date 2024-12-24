def knapsack_without_repetition(capacity, items):
    n = len(items)
    # Initialize a 2-D array to store maximum value for each capacity and number of items
    K = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Build the table K[][] in a bottom-up manner
    for j in range(1, n + 1):
        weight, value = items[j - 1]
        for w in range(capacity + 1):
            if weight > w:
                K[j][w] = K[j - 1][w]
            else:
                K[j][w] = max(K[j - 1][w], K[j - 1][w - weight] + value)

    return K[n][capacity]


# Example usage
print(knapsack_without_repetition(10, [(4, 5), (6, 8)]))  # Output: 13
print(knapsack_without_repetition(15, [(2, 3), (3, 7), (5, 10)]))  # Output: 20
print(knapsack_without_repetition(7, [(1, 2), (3, 4), (4, 5)]))  # Output: 9
print(knapsack_without_repetition(20, [(5, 10), (10, 15), (12, 20)]))  # Output: 30
print(knapsack_without_repetition(5, [(1, 2), (2, 3), (3, 5)]))  # Output: 8
