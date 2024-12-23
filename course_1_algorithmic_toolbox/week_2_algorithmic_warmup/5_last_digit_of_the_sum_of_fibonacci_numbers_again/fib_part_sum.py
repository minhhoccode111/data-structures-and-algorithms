# python3


# NOTE: This is a subproblem of the Fibonacci partial sum problem.
# Related problem: "Last digit of the sum of Fibonacci numbers again."


def fib_part_sum(m, n):
    # Initialize the sum of Fibonacci numbers in the range.
    sum = 0

    # Use the property of the Pisano period for modulo 10, which has a period of 60.
    # Reduce m and n modulo 60 to simplify computation.
    m = m % 60
    n = n % 60

    # Handle cases where n < m after modulo, adjust n to include numbers from m to n.
    if n < m:
        n += 60

    # Initialize the first two Fibonacci numbers.
    current = 0
    next = 1

    # Loop through Fibonacci numbers up to the nth index.
    for i in range(n + 1):
        # Add the current Fibonacci number to the sum if the index is within the range [m, n].
        if i >= m:
            sum += current

        # Compute the next Fibonacci number in the sequence.
        new_current = next
        next = next + current
        current = new_current

    # Return the last digit of the computed sum.
    return sum % 10


if __name__ == "__main__":
    m, n = map(int, input().split())
    print(fib_part_sum(m, n))
