# Dynamic Programming 2

## Knapsack with repetition

```
K(0) = 0
for w = 1 to W:
    K(w) = max{K(w - w<i>) + v<i> : w<i> <= w}
return K(W)
```

Example

```
W = 10
Item Weight Value
1    2      $3
2    3      $7
3    5      $10

    (W) 0  1  2  3  4  5  6  7  8  9  10
(n)(w,v)
0       0  0  0  0  0  0  0  0  0  0  0
1(2,3)  0  0  3  3  6  10 10 13 17 17 20
2(3,7)  0  0  0  7  7  10 14 14 17 21 21
3(5,10) 0  0  0  0  0  10 10 13 17 17 20
max     0  0  3  7  7  10 14 14 17 21 21

So the answer is: 21
```

## Knapsack without repetition

```
Initialize all K(0, j) = 0 and all K(w, 0) = 0
for j = 1 to n:
    for w = 1 to W:
        if w<j> > w: K(w, j) = K(w, j - 1)
        else: K(w, j) = max{K(w, j-1), K(w - w<j>, j - 1) + v<j>}
return K(W,n)
```

```
W = 10
Item Weight Value
1     2     $3
2     3     $7
3     5    $10


       (W) 0  1  2  3  4  5  6  7  8  9 10
  (n)(w,v)
  0        0  0  0  0  0  0  0  0  0  0  0
1(2,3)     0  0  3  3  3  3  3  3  3  3  3
2(3,7)     0  0  3  7  7 10 10 10 10 10 10
3(5,10)    0  0  3  7  7 10 10 13 17 17 20
max        0  0  3  7  7 10 10 13 17 17 20

So the answer is: 20
```

## Placing Parentheses (Or maximum value of an arithmetic expression)

M: for storing the max values
m: for storing the min values

```
MinAndMax(i,j)
min <- +Inf
max <- -Inf
for k from i to j - 1:
    a <- M(i,k) op<k> M(k + 1, j)
    b <- M(i,k) op<k> m(k + 1, j)
    c <- m(i,k) op<k> M(k + 1, j)
    d <- m(i,k) op<k> m(k + 1, j)
    min <- min(min, a, b, c, d)
    max <- max(max, a, b, c, d)
return (min,max)
```

```
Parentheses(d<1>op<1>d<2>op<2>...d<n>)
for i from 1 to n:
    m(i, i) <- d<i>, M(i, i) <- d<i>
for s from 1 to n - 1:
    for i from 1 to n -s:
        j <- i + s
        m(i, j), M(i, j) <- MinAndMax(i, j)
return M(1,n)
```
