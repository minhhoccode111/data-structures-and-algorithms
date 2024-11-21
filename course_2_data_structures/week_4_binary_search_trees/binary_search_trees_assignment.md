# Binary Search Trees Assignment

1. Your colleague proposed a different definition of a binary search tree: it is such binary tree with keys in the nodes that for each node the key of its left child (if exists) is less than its key, and the key of its right child (if exists) is bigger than its key. Is this a good definition for a binary search tree?

- No

We have to make sure it also greater than or less than the parent of current node too

2. Suppose we enforce the AVL tree condition only for the root of the tree, but not for all the nodes. Can such tree be unbalanced?

- Yes

Correct! Such tree could have height n/2 where nn is the number of nodes: two chains of length n/2 having root as the only common node form such a tree.

3. Can the Insert operation be implemented given only Split and Merge operations?

- Yes. First create a new tree with single key - the key to be inserted. Then split the current tree by this key. Then merge the left splitted part with the new tree. Then merge the result with the right splitted part.

4. Can the Delete operation be implemented given only Split and Merge operations?

- Yes. Suppose we are deleting key x. Split by the key twice: one split such that all the keys < x go to the left left and all the keys ≥ x go to the right. Then split the right part of the first split such that all the keys ≤ x go to the left and all the keys > x go to the right. Then merge the left part of the first split and the right part of the second split - thus leaving out the node with key x if there was such a node.
