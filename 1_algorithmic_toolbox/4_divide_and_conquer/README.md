# Divide and Conquer

- Break into non-overlapping subproblems of the same type
- Solve subproblems
- Combine results

## Linear Search

- Create a recursive solution
- Define a corresponding recurrence relation, T
- Determine T(n): worst-case runtime
- Optionally, create iterative solution

## Polynomial Multiplication

Uses of multiplying polynomials

- Error-correcting codes
- Large-integer multiplication
- Generating functions
- Convolution in signal processing

Naive solution O(n^2)

```
MultPoly(A, B, n)

product <- Array[2n - 1]
for i from 0 to 2n - 2:
    product[i] <- 0
for i from 0 to n - 1:
    for j from 0 to n - 1:
        product[i + j] <- product[i + j] + A[i] * B[j]
return product
```

Naive Divide and Conquer Algorithm solution O(n^2)

```
MultPoly2(A, b, n, a1, b1)
R = array[0..2n - 1]
if n = 1:
    R[0] = A[a1] * B[B1]; return R
R[0..n - 2] = MultPoly2(A, B, n/2, a1, b1)
R[n..2n - 2] = MultPoly2(A, B, n/2, a1 + n/2, b1 + n/2)
D0E1 = MultPoly2(A, B, n/2, a1, b1 + n/2)
D1E0 = MultPoly2(A, B, n/2, a1 + n/2, b1)
R[n/2...n + n/2 - 2] += D1E0 + D0E1
return R
```

Faster Divide and Conquer Algorithm solution

## Master theorem

## Sorting problem

- Make searching faster

## Selection Sort

Example

- Find a minimum by scanning the array
- Swap it with the first element
- Repeat with the remaining part of the array

Pseudo code

```
SelectionSort(A[1...n])
for i from 1 to n:
    minIndex <- 1
    for j from i + 1 to n:
        if A[j] < A[minIndex]:
            minIndex <- j
    {A[minIndex] = min A[i...n]}
    swap(A[i], A[minIndex])
    {A[1...i] is in final position}
```

Lemma

The running time of SelectSort(A[1...n]) is O(n^2)

Proof

n iterations of outer loop, at most n interations of inner loop

## Merge sort

Pseudo code

```
MergeSort(A[1...n])
if n = 1:
    return A
m <- n / 2
B <- MergeSort(A[1...m])
C <- MergeSort(A[m + 1...n])
A' <- MergeSort(B, C)
return A'
```

```
Merge(B[1...p], C[1...q])
{B and C are sorted}
D <- empty array of size p + q
while B and C are both non-empty:
    b <- the first element of B
    c <- the first element of C
    if b <= c:
        move b from B to the end of D
    else:
        move c from C to the end of D
move the rest of B and C to the end of D
return D
```

Estimating Tree Depth

- The number of leaves `l` in the tree must be at least `n!` (the total number of premutations)
- The worst-case running time of the algorithm (the number of comparisons made) is at least the depth `d`

## Count Sort

```
CountSort(A[1...n])
Count[1...M] <- [0,...,0]
for i from i to n:
    Count[A[i]] <- Count[A[i]] + 1
{k appears Count[k] times in A}
Pos[1...M] <- [0,...,0]
Pos[1] <- 1
for j from 2 to M:
    Pos[j] <- Pos[j - 1] + Count[j - 1]
{k will occupy range [Pos[k]...Pos[[k + 1] - 1]]}
for i from 1 to n:
    A'[Pos[A[i]]] <- A[i]
    Pos[A[i]] <- Pos[A[i]] + 1
```

## Quick sort

Pseudo code

```
QuickSort(A, l, r)
if l >= r:
    return
m <- Partition(A, l, r)
{A[m] is in the final position}
QuickSort(A, l, m - 1)
QuickSort(A, m + 1, r)
```
