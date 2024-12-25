# python3


# implement in-order, pre-order and post-order traversals of a binary tree


import sys, threading

sys.setrecursionlimit(10**6)
threading.stack_size(2**27)


class TreeOrders:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def inOrder(self):
        self.result = []

        def inOrderTraversal(index):
            if index == -1:
                return
            inOrderTraversal(self.left[index])
            self.result.append(self.key[index])
            inOrderTraversal(self.right[index])

        inOrderTraversal(0)
        return self.result

    def preOrder(self):
        self.result = []

        def preOrderTraversal(index):
            if index == -1:
                return
            self.result.append(self.key[index])
            preOrderTraversal(self.left[index])
            preOrderTraversal(self.right[index])

        preOrderTraversal(0)
        return self.result

    def postOrder(self):
        self.result = []

        def postOrderTraversal(index):
            if index == -1:
                return
            postOrderTraversal(self.left[index])
            postOrderTraversal(self.right[index])
            self.result.append(self.key[index])

        postOrderTraversal(0)
        return self.result


def main():
    tree = TreeOrders()
    tree.read()
    print(" ".join(str(x) for x in tree.inOrder()))
    print(" ".join(str(x) for x in tree.preOrder()))
    print(" ".join(str(x) for x in tree.postOrder()))


threading.Thread(target=main).start()
