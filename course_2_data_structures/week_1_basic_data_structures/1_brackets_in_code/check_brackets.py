# python3

# implement a feature for a text editor to find errors in the usage of
# brackets in the code

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []

    for i, char in enumerate(text, 1):
        if char in "([{":
            opening_brackets_stack.append(Bracket(char, i))

        if char in ")]}":
            if not opening_brackets_stack:
                return i

            top = opening_brackets_stack.pop()
            if not are_matching(top.char, char):
                return i

    return opening_brackets_stack[0].position if opening_brackets_stack else "Success"


def main():
    text = input()
    result = find_mismatch(text)
    print(result)


if __name__ == "__main__":
    main()
