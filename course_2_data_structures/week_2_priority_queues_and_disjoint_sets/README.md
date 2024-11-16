# Priority Queues and Disjoint Sets

## Pseudocode

```
Parent(i)
return [i/2]
```

```
LeftChild(i)
return 2i
```

```
RightChild(i)
return 2i + 1
```

```
SiftUp(i)
while i > 1 and H[Parent(i)] < H[1]:
    swap H[Parent(i)] and H[i]
    i <- Parent(i)
```

```
SiftDown(i)
maxIndex <- i
l <- LeftChild(i)
if l <= size and H[l] > H[maxIndex]:
    maxIndex <- l
r <- RightChild(i)
if r <= size and H[r] > H[maxIndex]:
    maxIndex <- r
if i != maxIndex:
    swap H[i] and H[maxIndex]
    SiftDown(maxIndex)
```

```
Insert(p)
if size = maxSize:
    return ERROR
size <- size + 1
H[size] <- p
SiftUp(size)
```

```
ExtractMax()
result <- H[1]
H[1] <- H[size]
size <- size - 1
SiftDown(1)
return result
```

```
Remove(i)
H[i] <- Infinity
SiftUp(i)
ExtractMax()
```

```
ChangePriority(i, p)
oldp <- H[i]
H[i] <- p
if p > oldp:
    SiftUp(i)
else:
    SiftDown(i)
```

## HeapSort

```
HeapSort(A[1...n])
create an empty priority queue
for i from 1 to n:
    Insert(A[i])
for i from n downto 1:
    A[i] <- ExtractMax()
```
