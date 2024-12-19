# Compute the greatest common divisor of two positive integers

# gcd(x, y) = gcd(x % y, y)
# proof: because any number that divides both x and y must also divide x % y

# because x % y always smaller than y, next recursive call will swap position of
# those digits


def gcd(x, y):
    return x if y == 0 else gcd(y, x % y)


if __name__ == "__main__":
    a, b = map(int, input().split())
    print(gcd(a, b))
