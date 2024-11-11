# gcd: greatest common divisor


def gcd(a, b):
    best = 0
    d = 1
    for d in range(1, a + b):
        if a % d == 0 and b % d == 0:
            best = d
    return best


if __name__ == "__main__":
    a = int(input())
    b = int(input())
    print(gcd(a, b))
