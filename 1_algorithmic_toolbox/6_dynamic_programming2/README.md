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
