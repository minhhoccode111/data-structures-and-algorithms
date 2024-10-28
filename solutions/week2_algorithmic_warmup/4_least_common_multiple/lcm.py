# Formula
#            |a * b|
# lcm(a,b) = --------
#            gcd(a,b)


def gcd(a, b):
    if b == 0:
        return a
    remainder = a % b
    return gcd(b, remainder)


def lcm(a, b):
    # cover edge cases
    if a == 0 or b == 0:
        return 0

    # print(f"a: {a}, b: {b}")
    # print(f"result: {abs(a * b) // gcd(a, b)}")
    # NOTE: have to use `//` instead of `/` because some how floating point make testcases fail
    return abs(a * b) // gcd(a, b)


if __name__ == "__main__":
    a, b = map(int, input().split())
    print(lcm(a, b))
