# python3


# find the minimum number of operations needed to get a positive integer n from
# 1 by using only three operations: add 1, multiply by 2, and multiply by 3


# using greedy algorithm
def compute_operations(n):
    return []


if __name__ == "__main__":
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)
