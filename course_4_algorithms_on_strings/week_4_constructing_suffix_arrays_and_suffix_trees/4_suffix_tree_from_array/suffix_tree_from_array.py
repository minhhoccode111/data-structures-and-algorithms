# python3


# construct a suffix tree from the suffix array and LSP array of a string


import sys
from collections import deque


class SuffixTreeNode:
    def __init__(self, parent, string_depth, edge_start, edge_end):
        self.parent = parent
        self.string_depth = string_depth
        self.edge_start = edge_start
        self.edge_end = edge_end
        self.children = dict()
        self.node_id = None


class SuffixTree:
    def __init__(self, text, suffix_arr, lcp, alphabet):
        self.text = text
        self.suffix_arr = suffix_arr
        self.lcp = lcp
        self.alphabet = sorted(alphabet)
        self.root = self._construct_tree(self.text, self.suffix_arr, self.lcp)
        self.edges = self._construct_edges(self.root)

    def _construct_edges(self, root):
        edges = dict()
        root.node_id = 0
        cur_id = 1
        q = deque([root])
        while q:
            cur = q.popleft()

            if cur.children:
                edges[cur.node_id] = []
                for char in self.alphabet:
                    if char in cur.children:
                        child = cur.children[char]
                        child.node_id = cur_id
                        cur_id += 1
                        edges[cur.node_id].append(
                            (child.node_id, child.edge_start, child.edge_end)
                        )
                        q.append(child)

        return edges

    def print_edges(self, edges):
        for node in edges:
            s = "Node {} / edges ".format(node)
            edges_s = ""
            for edge in edges[node]:
                edges_s += "#{}-{} ".format(edge[0], self.text[edge[1] : (edge[2] + 1)])
            s += edges_s
            print(s)

    def _construct_tree(self, text, suffix_arr, lcp):
        root = SuffixTreeNode(
            parent=None,
            string_depth=0,
            edge_start=-1,
            edge_end=-1,
        )

        lcp_prev = 0
        cur_node = root

        for i in range(len(text)):
            suffix = suffix_arr[i]

            while cur_node.string_depth > lcp_prev:
                cur_node = cur_node.parent

            if cur_node.string_depth == lcp_prev:
                cur_node = self._create_new_leaf(cur_node, text, suffix)
            else:
                edge_start = suffix_arr[i - 1] + cur_node.string_depth
                offset = lcp_prev - cur_node.string_depth
                mid_node = self._break_edge(cur_node, text, edge_start, offset)
                cur_node = self._create_new_leaf(mid_node, text, suffix)

            if i < len(text) - 1:
                lcp_prev = lcp[i]

        return root

    @staticmethod
    def _create_new_leaf(node, text, suffix):
        leaf = SuffixTreeNode(
            parent=node,
            string_depth=len(text) - suffix,
            edge_start=node.string_depth + suffix,
            edge_end=len(text) - 1,
        )
        node.children[text[leaf.edge_start]] = leaf
        return leaf

    @staticmethod
    def _break_edge(node, text, start, offset):
        start_char = text[start]
        mid_char = text[start + offset]
        mid_node = SuffixTreeNode(
            parent=node,
            string_depth=node.string_depth + offset,
            edge_start=start,
            edge_end=start + offset - 1,
        )
        mid_node.children[mid_char] = node.children[start_char]
        node.children[start_char].parent = mid_node
        node.children[start_char].edge_start += offset
        node.children[start_char] = mid_node
        return mid_node

    def output_tree(self):
        stack = [(0, 0)]
        while stack:
            node, edge_index = stack.pop()
            if node not in self.edges:
                continue
            edges = self.edges[node]
            if edge_index + 1 < len(edges):
                stack.append((node, edge_index + 1))
            print("%d %d" % (edges[edge_index][1], edges[edge_index][2] + 1))
            stack.append((edges[edge_index][0], 0))


def main():
    alphabet = "ACGT$"
    text = sys.stdin.readline().strip()
    suffix_array = list(map(int, sys.stdin.readline().strip().split()))
    lcp = list(map(int, sys.stdin.readline().strip().split()))
    print(text)
    tree = SuffixTree(text, suffix_array, lcp, alphabet)
    tree.output_tree()


if __name__ == "__main__":
    main()
