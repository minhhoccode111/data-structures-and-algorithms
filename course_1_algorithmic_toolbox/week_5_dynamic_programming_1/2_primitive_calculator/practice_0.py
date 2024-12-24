# python3


# find the minimum number of operations needed to get a positive integer n from
# 1 by using only three operations: add 1, multiply by 2, and multiply by 3


# using greedy algorithm
def compute_operations(n):
    num_ops = 0
    curr_num = 1
    num_steps = [1]

    while curr_num < n:
        if n >= curr_num * 3:
            curr_num *= 3
        elif n >= curr_num * 2:
            curr_num *= 2
        else:
            curr_num += 1
        num_ops += 1
        num_steps.append(curr_num)

    return num_steps


if __name__ == "__main__":
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)
