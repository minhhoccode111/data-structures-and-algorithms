# python3


# implement an algorithm for solving linear programming with only a few
# inequalities and apply it to determine the optimal diet


from sys import stdin
import itertools
import copy


class Equation:
    def __init__(self, a, b):
        self.a = a
        self.b = b


class Position:
    def __init__(self, column, row):
        self.column = column
        self.row = row


def ReadEquation():
    size = int(input())
    a = []
    b = []
    for row in range(size):
        line = list(map(float, input().split()))
        a.append(line[:size])
        b.append(line[size])
    return Equation(a, b)


def SelectPivotElement(a, used_rows, used_columns):
    pivot_element = Position(0, 0)
    while used_rows[pivot_element.row]:
        pivot_element.row += 1
    while used_columns[pivot_element.column]:
        pivot_element.column += 1
    if a[pivot_element.row][pivot_element.column] == 0:
        global flagSwap
        global flagExit
        flagSwap = True
        s = pivot_element.row
        while a[pivot_element.row][pivot_element.column] == 0:
            pivot_element.row += 1
            if pivot_element.row > len(a) - 1:
                pivot_element.column += 1
                pivot_element.row = s
                if pivot_element.column > len(a[0]) - 1:
                    flagExit = True
                    break
    return pivot_element


def SwapLines(a, b, used_rows, pivot_element):
    used_rows_num = 0
    while used_rows[used_rows_num]:
        used_rows_num += 1
    a[pivot_element.row], a[used_rows_num] = a[used_rows_num], a[pivot_element.row]
    b[pivot_element.row], b[used_rows_num] = b[used_rows_num], b[pivot_element.row]
    pivot_element.row = used_rows_num
    global flagSwap
    flagSwap = False


def ProcessPivotElement(a, b, pivot_element):
    num = a[pivot_element.row][pivot_element.column]
    for i in range(len(a[pivot_element.row])):
        a[pivot_element.row][i] /= num
    if b[pivot_element.row] != 0:
        b[pivot_element.row] /= num
    for i in range(len(a)):
        h = a[i]
        if i == pivot_element.row:
            continue
        if h[pivot_element.column] != 0:
            numrow = h[pivot_element.column]
            for j in range(len(h)):
                h[j] -= a[pivot_element.row][j] * numrow
            b[i] -= b[pivot_element.row] * numrow
    pass


def MarkPivotElementUsed(pivot_element, used_rows, used_columns):
    used_rows[pivot_element.row] = True
    used_columns[pivot_element.column] = True


def SolveEquation(equation):
    a = copy.deepcopy(equation.a)
    b = copy.deepcopy(equation.b)
    size = len(a)
    global flagSwap
    global flagExit
    flagExit = False
    used_columns = [False] * (size)
    used_rows = [False] * (size)
    for step in range(size):
        pivot_element = SelectPivotElement(a, used_rows, used_columns)
        if flagExit:
            return [-1 for i in range(m)]
        if flagSwap:
            SwapLines(a, b, used_rows, pivot_element)
        ProcessPivotElement(a, b, pivot_element)
        MarkPivotElementUsed(pivot_element, used_rows, used_columns)

    return b


def test(solution, A, b):
    for i in range(len(A)):
        sum = 0
        for j in range(len(A[i])):
            sum += A[i][j] * solution[j]
        if sum - b[i] > 1e-4:
            return False
    return True


def solve_diet_problem(n, m, A, b, c):
    set_interseption = itertools.combinations([i for i in range(n + m + 1)], m)
    maximum = -(10**9)
    bestSolution = []
    for i in set_interseption:
        Aevac = []
        bEvac = []
        for j in i:
            Aevac.append(A[j])
            bEvac.append(b[j])
        equation = Equation(Aevac, bEvac)
        solution = SolveEquation(equation)
        ans = 0
        for s in range(m):
            ans += c[s] * solution[s]
        if test(solution, A, b):
            if ans >= maximum:
                maximum = ans
                bestSolution = solution
                infTest = i
    if bestSolution == []:
        return -1, []
    elif n in infTest:
        return 1, []
    else:
        return 0, bestSolution


flagSwap = False
flagExit = False
n, m = list(map(int, stdin.readline().split()))
A = []
for i in range(n):
    A += [list(map(int, stdin.readline().split()))]
b = list(map(int, stdin.readline().split()))
c = list(map(int, stdin.readline().split()))
A.append([1 for i in range(m)])
b.append(10**9)
for i in range(m):
    s = [0 for i in range(m)]
    s[i] = -1
    A.append(s)
    b.append(0)


anst, ansx = solve_diet_problem(n, m, A, b, c)


if anst == -1:
    print("No solution")
if anst == 0:
    print("Bounded solution")
    print(" ".join(list(map(lambda x: "%.18f" % x, ansx))))
if anst == 1:
    print("Infinity")
