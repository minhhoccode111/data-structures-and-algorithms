# python3


# construct a suffix tree of a string


import sys


class SuffixTreeNode:
    def __init__(self, start, end=None):
        self.children = {}
        self.start = start
        self.end = end


class SuffixTree:
    def __init__(self, text):
        self.text = text
        self.root = SuffixTreeNode(-1, -1)
        self.build()

    def build(self):
        n = len(self.text)
        for i in range(n):
            current = self.root
            j = i
            while j < n:
                char = self.text[j]
                if char in current.children:
                    child = current.children[char]
                    k = child.start
                    while k < child.end and j < n and self.text[k] == self.text[j]:
                        k += 1
                        j += 1
                    if k == child.end:
                        current = child
                    else:
                        split_node = SuffixTreeNode(child.start, k)
                        current.children[char] = split_node
                        split_node.children[self.text[k]] = child
                        child.start = k
                        split_node.children[self.text[j]] = SuffixTreeNode(j, n)
                        break
                else:
                    current.children[char] = SuffixTreeNode(j, n)
                    break

    def collect_edges(self):
        edges = []
        stack = [self.root]
        while stack:
            node = stack.pop()
            for child in node.children.values():
                edges.append(self.text[child.start : child.end])
                stack.append(child)
        return edges


def build_suffix_tree(text):
    tree = SuffixTree(text)
    return tree.collect_edges()


if __name__ == "__main__":
    text = sys.stdin.readline().strip()
    result = build_suffix_tree(text)
    print("\n".join(result))
