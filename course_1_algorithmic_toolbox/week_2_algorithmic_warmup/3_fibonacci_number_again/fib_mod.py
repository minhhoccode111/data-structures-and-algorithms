# python3

# Huge fibonacci number problem
# Compute the n-th Fibonacci number modulo m using Pisano Period


# Calculate and return Pisano Period
# the length of a Pisano Period for a
# given m ranges from 3 to m * m
def pisanoPeriod(m):
    previous, current = 0, 1
    for i in range(0, m * m):
        previous, current = current, (previous + current) % m

        # a Pisano Period starts with 01
        if previous == 0 and current == 1:
            return i + 1


# calculate F<n> mod m
def fib_mod(n, m):
    # getting the period
    pisano_period = pisanoPeriod(m)
    # taking mod of N with period length
    n = n % pisano_period
    previous, current = 0, 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    for i in range(n - 1):
        previous, current = current, previous + current
    return current % m


if __name__ == "__main__":
    n, m = map(int, input().split())
    print(fib_mod(n, m))
