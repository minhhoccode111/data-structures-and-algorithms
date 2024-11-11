def knapsack_with_repetition(capacity, items):
    # items: (weight, value)
    k = [0] * (capacity + 1)
    k[0] = 0
    for w in range(1, capacity + 1):
        for weight, value in items:
            if weight <= w:
                k[w] = max(k[w], k[w - weight] + value)

    return k[capacity]


print(knapsack_with_repetition(10, [(4, 5), (6, 8)]))  # 13
print(knapsack_with_repetition(15, [(2, 3), (3, 7), (5, 10)]))  # 35
print(knapsack_with_repetition(7, [(1, 2), (3, 4), (4, 5)]))  # 14
print(knapsack_with_repetition(20, [(5, 10), (10, 15), (12, 20)]))  # 40
print(knapsack_with_repetition(5, [(1, 2), (2, 3), (3, 5)]))  # 10
