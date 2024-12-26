# python3

# Compute the last digit of the n-th Fibonacci number

# Use matrix exponentiation
# See: Exercises 0.4 - p.18 - Algorithms 1st Edition


def fib_huge(n):
    if n <= 1:
        return n

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
        result = [[1, 0], [0, 1]]
        while power > 0:
            if power % 2 == 1:
                result = multiply_matrices(result, matrix)
            matrix = multiply_matrices(matrix, matrix)
            power //= 2
        return result

    fib_matrix = [[1, 1], [1, 0]]
    result_matrix = matrix_power(fib_matrix, n - 1)

    return result_matrix[0][0]


if __name__ == "__main__":
    n = int(input())
    print(fib_huge(n) % 10)
