#!/bin/env python3


"""

diff <(python fibonacci.py < test/1) <(cat test/1.a)
diff <(python fibonacci.py < test/2) <(cat test/2.a)
diff <(python fibonacci.py < test/3) <(cat test/3.a)
diff <(python fibonacci.py < test/4) <(cat test/4.a)
diff <(python fibonacci.py < test/5) <(cat test/5.a)

"""


def fibonacci_number(n):
    if n <= 1:
        return n

    a = 0
    b = 1
    i = n - 2

    while i > 0:
        i -= 1
        c = a + b
        a = b
        b = c

    return a + b


# prevent the main function from running when module is imported
if __name__ == "__main__":
    input_n = int(input())
    print(fibonacci_number(input_n))
