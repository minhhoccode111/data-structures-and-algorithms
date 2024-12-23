# Formula

#            |a * b|
# lcm(a,b) = --------
#            gcd(a,b)


# NOTE: check out Greatest Common Divisor problem for GCD
def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


def lcm(a, b):
    return 0 if a == 0 or b == 0 else abs(a * b) // gcd(a, b)


if __name__ == "__main__":
    a, b = map(int, input().split())
    print(lcm(a, b))
