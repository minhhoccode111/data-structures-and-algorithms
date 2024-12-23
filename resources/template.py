#!/usr/bin/env python3
# The platform need this line to specify which version of python to use


"""

diff: Command to differentiate the solution output (write to stdout use `print`)
with the test output (write to stdout use `cat`)
<(command): run sub command before the main command (diff)

# Dirrectoties
test/: not git ignored, sample test cases
tests/: git ignored, store the test files provided by the platform

# Files
solution.py: solution file
1: input file
1.a: output file

# Commands
diff <(python solution.py < test/1) <(cat test/1.a)
diff <(python solution.py < tests/2) <(cat tests/2.a)

"""


def solution(n):
    # TODO: implement solution here

    return n


# this syntax prevent the main function from running when module is imported
# it's better than define the `main()` function directly
if __name__ == "__main__":
    input_n = int(input())
    print(solution(input_n))
