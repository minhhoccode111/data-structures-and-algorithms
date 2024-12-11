"""

diff <(python3 suffix_tree.py < test/1) <(cat test/1.a)
diff <(python3 suffix_tree.py < test/2) <(cat test/2.a)
diff <(python3 suffix_tree.py < test/3) <(cat test/3.a)

"""

# TODO: fix this problem


import sys


import sys


class SuffixTree:
    def __init__(self, text):
        self.text = text
        self.length = len(text)
        self.tree = [[] for _ in range(self.length // 10 + 1)]
        self.cnt = 1
        self.ROOT = 0

    class Node:
        def __init__(self, next_node, start, end):
            self.next = next_node
            self.start = start
            self.end = end

    def add_node(self, start, i):
        self.tree.append([])
        self.tree[i].append(self.Node(self.cnt, start, self.length))
        self.cnt += 1

    def add_nodes_branching(self, node, k, m):
        # this method is equivalent to the c++ version's logic
        if self.tree[node.next]:
            # create two new nodes and move existing subtree
            self.tree.append([])
            self.tree.append([])

            # move existing subtree
            self.tree[self.cnt] = self.tree[node.next].copy()

            # first new node with remaining part of original edge
            node_copy = self.Node(self.cnt, m, node.end)
            self.tree[node.next] = [node_copy]

            # second new node from the new splitting point
            node_new = self.Node(self.cnt + 1, k, self.length)
            self.tree[node.next].append(node_new)

            # update the original node's end
            node.end = m

            self.cnt += 2
        else:
            # if no subtree exists, simply add two new nodes
            self.add_node(m, node.next)
            self.add_node(k, node.next)
            node.end = m

    def build_tree(self):
        for j in range(self.length):
            cur = self.ROOT
            k = j
            while True:
                # find an edge starting with the current symbol
                symbol = self.text[k]
                matching_edges = [
                    node for node in self.tree[cur] if self.text[node.start] == symbol
                ]

                if not matching_edges:
                    # no matching edge, add a new node and break
                    self.add_node(k, cur)
                    break

                node = matching_edges[0]
                m = node.start

                # compare characters along the edge
                while k < self.length and m < node.end:
                    if self.text[k] != self.text[m]:
                        # splitting point found
                        self.add_nodes_branching(node, k, m)
                        break
                    k += 1
                    m += 1

                # if we've fully traversed this edge
                if m == node.end:
                    if k == self.length:
                        # reached end of input
                        break

                    if not self.tree[node.next]:
                        # no further edges, add a new node
                        self.add_node(k, node.next)
                        break

                    # move to next node
                    cur = node.next
                    continue

                # partial match or other cases
                if k == self.length:
                    # input fully processed
                    break

                if not self.tree[node.next]:
                    # no subtree, add a new node at the remaining point
                    self.add_node(m, node.next)
                    node.end = m
                    break

                # create a new intermediate node
                self.tree.append([])
                self.tree[self.cnt].append(self.Node(node.next, m, node.end))
                node.next = self.cnt
                node.end = m
                break

    def print_tree_edges(self):
        result = []
        for edges in self.tree:
            for e in edges:
                result.append(self.text[e.start : e.end])
        # sort the results to ensure consistent ordering
        return sorted(set(result))


def build_suffix_tree(text):
    """
    Build a suffix tree of the string text and return a list
    with all of the labels of its edges (the corresponding
    substrings of the text) in any order.
    """
    suffix_tree = SuffixTree(text)
    suffix_tree.build_tree()
    return suffix_tree.print_tree_edges()


if __name__ == "__main__":
    text = sys.stdin.readline().strip()
    result = build_suffix_tree(text)
    print("\n".join(result))
