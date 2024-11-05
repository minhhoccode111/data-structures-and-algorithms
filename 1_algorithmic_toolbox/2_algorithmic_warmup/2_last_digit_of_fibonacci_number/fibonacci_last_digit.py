# def fibonacci_last_digit(n):
#     if n <= 1:
#         return n
#
#     # first 2 numbers in fibonacci sequence
#     a = 0
#     b = 1
#     # use i to count backward
#     i = n - 2
#
#     while i > 0:
#         i -= 1
#         # c: next sum of 2 previous number
#         c = a + b
#         # update a
#         a = b
#         # update b
#         b = c
#
#     return (a + b) % 10

# import sys

# sys.set_int_max_str_digits(999999999)


def fibonacci_last_digit(n):
    if n <= 1:
        return n

    # Define the transformation matrix
    def multiply_matrices(a, b):
        return [
            [
                a[0][0] * b[0][0] + a[0][1] * b[1][0],
                a[0][0] * b[0][1] + a[0][1] * b[1][1],
            ],
            [
                a[1][0] * b[0][0] + a[1][1] * b[1][0],
                a[1][0] * b[0][1] + a[1][1] * b[1][1],
            ],
        ]

    def matrix_power(matrix, power):
        result = [[1, 0], [0, 1]]  # Identity matrix
        while power > 0:
            if power % 2 == 1:
                result = multiply_matrices(result, matrix)
            matrix = multiply_matrices(matrix, matrix)
            power //= 2
        return result

    # Fibonacci transformation matrix
    fib_matrix = [[1, 1], [1, 0]]
    result_matrix = matrix_power(fib_matrix, n - 1)

    # print(f"n is: {n}")
    # print(f"result is: {result_matrix[0][0]}")
    # The nth Fibonacci number is in the [0][0] position of the result matrix
    return result_matrix[0][0] % 10


if __name__ == "__main__":
    n = int(input())
    print(fibonacci_last_digit(n))
