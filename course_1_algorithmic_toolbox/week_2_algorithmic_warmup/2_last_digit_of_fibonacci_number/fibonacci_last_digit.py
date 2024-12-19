# python3

# Compute the last digit of the n-th Fibonacci number

# Use matrix exponentiation
# See: Exercises 0.4 - p.18 - Algorithms 1st Edition


def fib_huge(n):
    # base case
    if n <= 1:
        return n

    # multiply two 2×2 matrices a and b
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

    # efficiently computes matrix^power using exponentiation by squaring
    def matrix_power(matrix, power):
        # start with identity matrix
        # any matrix multiplied by identity matrix remains unchanged
        result = [[1, 0], [0, 1]]
        while power > 0:
            # if power is odd
            if power % 2 == 1:
                # multiply the result matrix by current matrix
                result = multiply_matrices(result, matrix)
            # square the matrix (multiply it by itself) to reduce the number of
            # multiplications needed
            matrix = multiply_matrices(matrix, matrix)
            # halve the power
            power //= 2
        # this reduce the time complexity to O(log n), making the algorithm
        # efficient
        return result

    # matrix representation of Fibonacci numbers
    fib_matrix = [[1, 1], [1, 0]]
    """
    the property of this matrix is:

    M^n = [F<n+1>, F<n>  ]
          [F<n>  , F<n-1>]

    the (0, 0)- element of M^(n-1) gives F<n>, the n-th Fibonacci number
    """
    result_matrix = matrix_power(fib_matrix, n - 1)

    return result_matrix[0][0]


if __name__ == "__main__":
    n = int(input())
    # mod 10 to get the last digit
    print(fib_huge(n) % 10)
