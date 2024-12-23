# python3


# NOTE: This is a subproblem of the Fibonacci partial sum problem.
# Related problem: "Last digit of the sum of Fibonacci numbers again."


def fib_part_sum(m, n):
    sum = 0

    m = m % 60
    n = n % 60

    if n < m:
        n += 60

    current = 0
    next = 1

    for i in range(n + 1):
        if i >= m:
            sum += current

        new_current = next
        next = next + current
        current = new_current

    return sum % 10


if __name__ == "__main__":
    n = int(input())

    print(fib_part_sum(0, n))
