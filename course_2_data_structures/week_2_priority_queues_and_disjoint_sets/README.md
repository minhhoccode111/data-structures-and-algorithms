# Priority Queues and Disjoint Sets

## Heap

Note that assumming we use base 1 indexing

### Pseudo code

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

## HeapSort Pseudo code

```
HeapSort(A[1...n])
    BuildMaxHeap(A)
    for i = n to 1
        swap A[1] and A[i]
        n = n - 1
        Heapify(A, 1)

BuildMaxHeap(A[1...n])
    n = elements_in(A)
    for i = floor(n/2) to 1
        Heapify(A, i)

Heapify(A[1...n], i)
    left = 2i
    right = 2i + 1
    max = i
    if left <= n and A[left] > A[max]:
        max = left
    if right <= n and A[right] > A[max]:
        max = right
    if max != i:
        swap A[i] and A[max]
        Heapify(A, max)
```

## Disjoint Sets

Definition

A disjoint-set data structure is a data structure that supports the following operations:

- MakeSet(x) creates a singleton set {x}
- Find(x) returns ID of the set containing x:
  - if x and y lie in the same set, then Find(x) = Find(y)
  - otherwise, Find(x) != Find(y)
- Union(x, y) merges the sets containing x and y.

```
Preprocess(maze)
for each cell c in maze:
    MakeSet(c)
for each cell c in maze:
    for each neighbor n of c:
        Union(c, n)
```

```
IsReachable(A, B)
return Find(A) = Find(B)
```
