# python3


# implement a stack that also supports the maximum value and to ensure that all
# operations still work in constant time


import sys


class StackWithMax:
    def __init__(self):
        self.__stack = []
        self.__maxStack = []

    def Push(self, value):
        self.__stack.append(value)
        if not self.__maxStack or value >= self.__maxStack[-1]:
            self.__maxStack.append(value)

    def Pop(self):
        assert len(self.__stack)
        value = self.__stack.pop()
        if value == self.__maxStack[-1]:
            self.__maxStack.pop()

    def Max(self):
        assert len(self.__stack)
        return self.__maxStack[-1]


if __name__ == "__main__":
    stack = StackWithMax()
    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()
        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert 0
