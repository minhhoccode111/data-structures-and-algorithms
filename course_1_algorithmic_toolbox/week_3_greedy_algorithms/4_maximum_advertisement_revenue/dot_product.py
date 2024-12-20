# python3

# find the maximum dot product of two sequences of numbers


from itertools import permutations


def max_dot_product(first_sequence, second_sequence):
    # Sort both sequences in descending order
    first_sequence.sort(reverse=True)
    second_sequence.sort(reverse=True)
    # Compute the dot product
    return sum(p * c for p, c in zip(first_sequence, second_sequence))


if __name__ == "__main__":
    n = int(input())
    prices = list(map(int, input().split()))
    clicks = list(map(int, input().split()))
    assert len(prices) == len(clicks) == n
    print(max_dot_product(prices, clicks))
