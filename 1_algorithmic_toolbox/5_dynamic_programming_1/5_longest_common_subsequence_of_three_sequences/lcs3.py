import numpy


def LCS3(s1, s2, s3, n1, n2, n3):
    Matrix = numpy.zeros((n1 + 1, n2 + 1, n3 + 1))
    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            for k in range(1, n3 + 1):
                if s1[i - 1] == s2[j - 1] == s3[k - 1]:
                    Matrix[i][j][k] = Matrix[i - 1][j - 1][k - 1] + 1
                else:
                    Matrix[i][j][k] = max(
                        Matrix[i - 1][j][k], Matrix[i][j - 1][k], Matrix[i][j][k - 1]
                    )
    return (int(Matrix[-1][-1][-1]), Matrix)


def printSubsequence(Matrix, s1, s2, s3, i, j, k, seq):
    if i == 0 or j == 0 or k == 0:
        if seq == []:
            return None
        else:
            return "".join(seq[::-1])
    if s1[i - 1] == s2[j - 1] == s3[k - 1]:
        seq.append(s1[i - 1])
        return printSubsequence(Matrix, s1, s2, s3, i - 1, j - 1, k - 1, seq)
    if Matrix[i - 1][j][k] > Matrix[i][j - 1][k]:
        if Matrix[i - 1][j][k] > Matrix[i][j][k - 1]:
            return printSubsequence(Matrix, s1, s2, s3, i - 1, j, k, seq)
        else:
            return printSubsequence(Matrix, s1, s2, s3, i, j, k - 1, seq)
    else:
        if Matrix[i][j - 1][k] > Matrix[i][j][k - 1]:
            return printSubsequence(Matrix, s1, s2, s3, i, j - 1, k, seq)
        else:
            return printSubsequence(Matrix, s1, s2, s3, i, j, k - 1, seq)


if __name__ == "__main__":
    n1, s1, n2, s2, n3, s3 = (
        int(input()),
        input(),
        int(input()),
        input(),
        int(input()),
        input(),
    )
    LCS_length, Matrix = LCS3(s1, s2, s3, n1, n2, n3)
    print("Length of LCS:", LCS_length)
    sequence = printSubsequence(Matrix, s1, s2, s3, n1, n2, n3, [])
    print("LCS:", sequence)
