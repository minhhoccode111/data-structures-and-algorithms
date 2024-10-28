# It then recursively calls itself with b and c as the new arguments. This step repeats until bb becomes zero, returning the GCD as the value of aa at that point.


def gcd(a, b):
    if b == 0:
        return a
    remainder = a % b
    return gcd(b, remainder)


if __name__ == "__main__":
    a = int(input())
    b = int(input())
    print(gcd(a, b))
