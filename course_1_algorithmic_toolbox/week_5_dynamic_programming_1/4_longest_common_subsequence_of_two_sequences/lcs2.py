import numpy


def LCS2(s1, s2, n1, n2):
    Matrix = numpy.zeros((n1 + 1, n2 + 1))
    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            if s1[i - 1] == s2[j - 1]:
                Matrix[i][j] = Matrix[i - 1][j - 1] + 1
            if s1[i - 1] != s2[j - 1]:
                Matrix[i][j] = max(Matrix[i][j - 1], Matrix[i - 1][j])
    return (int(Matrix[n1][n2]), Matrix)


def printSubsequence(Matrix, s1, s2, i, j, seq):
    if i == 0 or j == 0:
        if seq == []:
            return None
        return "".join(seq[::-1])
    if s1[i - 1] == s2[j - 1]:
        seq.append(s1[i - 1])
        return printSubsequence(Matrix, s1, s2, i - 1, j - 1, seq)
    if Matrix[i - 1][j] > Matrix[i][j - 1]:
        return printSubsequence(Matrix, s1, s2, i - 1, j, seq)
    else:
        return printSubsequence(Matrix, s1, s2, i, j - 1, seq)


if __name__ == "__main__":
    n1, s1, n2, s2 = int(input()), input(), int(input()), input()
    LCS_length, Matrix = LCS2(s1, s2, n1, n2)
    sequence = printSubsequence(Matrix, s1, s2, n1, n2, [])
    print("Length of LCS:", LCS_length)
    print("LCS:", sequence)
