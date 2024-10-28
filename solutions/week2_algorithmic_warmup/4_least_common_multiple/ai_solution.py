def gcd(a: int, b: int) -> int:
    """
    Calculate the Greatest Common Divisor using Euclidean algorithm.
    This is an efficient method that works well with very large numbers.
    """
    while b:
        a, b = b, a % b
    return a


def lcm(a: int, b: int) -> int:
    """
    Calculate the Least Common Multiple using the formula: LCM(a,b) = |a * b| / GCD(a,b)
    Returns 0 if either input is 0.
    """
    if a == 0 or b == 0:
        return 0
    # print(f"a: {a}, b: {b}")
    # print(f"result: {abs(a * b) // gcd(a, b)}")
    return abs(a * b) // gcd(a, b)


if __name__ == "__main__":
    a, b = map(int, input().split())
    print(lcm(a, b))
