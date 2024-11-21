# Splay Trees Assignment

1. What is going to happen if you forget to splay the last accessed vertex in the implementation of FindFind in case the key was not found in the splay tree?

- The tree will work too slow on some sequences of operations

2. What will happen if you splay the node with the smallest key in a splay tree?

- The root of the new tree won't have left child

The node with the smallest key will become the root after splaying, and it cannot have a left child, because the key of the left child must be smaller than the key of its parent

3. What will happen if you select a node NN, splay its predecessor PP (the node with the largest key smaller than the key of NN), then splay the node NN itself?

- N will be the root, P will be the left child of the root, P won't have a right child

Correct! After the first splay, P will become the root. After the second splay, N will become the root, and P will become its child, and it will be on the left, because its key is smaller. P won't have a right child, because a right child of P must have key bigger than the key of P, and also it must have key smaller than the key of N (because it is now in the left subtree of N), but it can't happen, because P is the predecessor of N, so there are no keys between the key of P and the key of N
