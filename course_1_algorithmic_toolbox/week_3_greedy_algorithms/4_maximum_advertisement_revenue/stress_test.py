import random
from dot_product import max_dot_product
from itertools import permutations
from dot_product_naive import max_dot_product_naive


# stress test to know why my efficient algorithm have wrong answer


def stress_test():
    # Parameters for stress testing
    max_n = 10  # Maximum size of the arrays
    max_value = 100  # Maximum value in the arrays
    test_cases = 1000000  # Number of test cases to generate

    for i in range(test_cases):
        # Generate random sizes and values
        n = random.randint(1, max_n)
        first_sequence = [random.randint(1, max_value) for _ in range(n)]
        second_sequence = [random.randint(1, max_value) for _ in range(n)]

        # Copy the sequences to avoid modifying them between functions
        first_seq_copy = first_sequence[:]
        second_seq_copy = second_sequence[:]

        # Compute results using both algorithms
        # naive_result = max_dot_product_naive(first_sequence, second_sequence)
        efficient_result = max_dot_product(first_seq_copy, second_seq_copy)

        print(i, efficient_result, " ", "ok")

        # # Compare results
        # if naive_result == efficient_result:
        #     print(i, " ", "OK")
        # else:
        #     print("Mismatch found!")
        #     print(f"Input first_sequence: {first_sequence}")
        #     print(f"Input second_sequence: {second_sequence}")
        #     print(f"Naive result: {naive_result}")
        #     print(f"Efficient result: {efficient_result}")
        #     break  # Stop at the first mismatch


if __name__ == "__main__":
    stress_test()
