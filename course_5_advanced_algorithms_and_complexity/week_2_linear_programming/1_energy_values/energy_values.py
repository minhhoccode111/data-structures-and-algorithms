# python3

# apply Gaussian Elimination to infer the energy values of ingredients given a
# restaurant menu with calorie counts and ingredient lists provided for each item

EPS = 1e-6
PRECISION = 20


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
    size = len(a)
    pivot_element = Position(0, 0)
    max_value = -1.0
    for row in range(size):
        if not used_rows[row]:
            for column in range(size):
                if not used_columns[column] and abs(a[row][column]) > max_value:
                    max_value = abs(a[row][column])
                    pivot_element.row = row
                    pivot_element.column = column
    return pivot_element


def SwapLines(a, b, used_rows, pivot_element):
    a[pivot_element.column], a[pivot_element.row] = (
        a[pivot_element.row],
        a[pivot_element.column],
    )
    b[pivot_element.column], b[pivot_element.row] = (
        b[pivot_element.row],
        b[pivot_element.column],
    )
    used_rows[pivot_element.column], used_rows[pivot_element.row] = (
        used_rows[pivot_element.row],
        used_rows[pivot_element.column],
    )
    pivot_element.row = pivot_element.column


def ProcessPivotElement(a, b, pivot_element):
    size = len(a)
    row = pivot_element.row
    col = pivot_element.column
    pivot_value = a[row][col]

    for i in range(size):
        a[row][i] /= pivot_value
    b[row] /= pivot_value

    for other_row in range(size):
        if other_row != row and abs(a[other_row][col]) > EPS:
            factor = a[other_row][col]
            for i in range(size):
                a[other_row][i] -= a[row][i] * factor
            b[other_row] -= b[row] * factor


def MarkPivotElementUsed(pivot_element, used_rows, used_columns):
    used_rows[pivot_element.row] = True
    used_columns[pivot_element.column] = True


def SolveEquation(equation):
    a = equation.a
    b = equation.b
    size = len(a)

    used_columns = [False] * size
    used_rows = [False] * size
    for step in range(size):
        pivot_element = SelectPivotElement(a, used_rows, used_columns)
        SwapLines(a, b, used_rows, pivot_element)
        ProcessPivotElement(a, b, pivot_element)
        MarkPivotElementUsed(pivot_element, used_rows, used_columns)

    return b


def PrintColumn(column):
    size = len(column)
    result = ""
    for row in range(size):
        result = result + "%.6lf" % column[row] + " "
    if size == 0:
        return
    print(result[: len(result) - 1])


if __name__ == "__main__":
    equation = ReadEquation()
    solution = SolveEquation(equation)
    PrintColumn(solution)
    exit(0)
