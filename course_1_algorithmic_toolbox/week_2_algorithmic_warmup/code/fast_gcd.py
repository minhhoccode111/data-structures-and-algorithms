# It then recursively calls itself with b and c as the new arguments. This step repeats until bb becomes zero, returning the GCD as the value of aa at that point.


def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


if __name__ == "__main__":
    a = int(input())
    b = int(input())
    print(gcd(a, b))
