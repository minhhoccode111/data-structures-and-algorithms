# python3

# a company needs to allocate its advertising budget across different
# subdepartments. each subdepartment has proposed a campaign plan, and the
# company has budget constraints and policies. determine if it's possible to
# allocate the budget to satisfy all the constraints

from itertools import starmap
from operator import mul
from sys import stdin


class IntToSAT:
    sol1 = (
        (0,),
        (1,),
    )
    sol2 = (
        (0, 0),
        (0, 1),
        (1, 0),
        (1, 1),
    )
    sol3 = (
        (0, 0, 0),
        (0, 0, 1),
        (0, 1, 0),
        (0, 1, 1),
        (1, 0, 0),
        (1, 0, 1),
        (1, 1, 0),
        (1, 1, 1),
    )

    def __init__(self, A, b):
        self.A = A
        self.b = b

    def _inequality_to_sat(self, row, value):
        nonzero_ids, nonzero_elems = [], []
        for i, a in enumerate(row):
            if a != 0:
                nonzero_ids.append(i + 1)
                nonzero_elems.append(a)
                if len(nonzero_elems) == 3:
                    break
        num_nonzero_elems = len(nonzero_elems)
        sat = []
        if num_nonzero_elems == 0:
            return sat
        if num_nonzero_elems == 1:
            sol = self.sol1
        elif num_nonzero_elems == 2:
            sol = self.sol2
        else:
            sol = self.sol3
        for s in sol:
            res = sum(starmap(mul, zip(nonzero_elems, s)))
            if res > value:
                signs = [1 if x == 0 else -1 for x in s]
                clause = tuple(starmap(mul, zip(signs, nonzero_ids)))
                sat.append(clause)
        return sat

    def convert(self):
        sat = []
        for i in range(len(self.A)):
            row = self.A[i]
            value = self.b[i]
            sat_row = self._inequality_to_sat(row, value)
            if sat_row:
                sat.extend(sat_row)
        if not sat:
            sat.append((1, -1))
        return sat


def main():
    line = stdin.readline()
    if not line:
        return
    num_inequalities, num_variables = map(int, line.split())
    A = []
    for _ in range(num_inequalities):
        line = stdin.readline()
        if not line:
            return
        A += [list(map(int, line.split()))]
    line = stdin.readline()
    if not line:
        return
    b = list(map(int, line.split()))

    ilp_to_sat = IntToSAT(A, b)
    sat = ilp_to_sat.convert()
    print(len(sat), num_variables)
    for clause in sat:
        s = " ".join(map(str, clause))
        s += " 0"
        print(s)


if __name__ == "__main__":
    main()
