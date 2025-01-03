# python3

# implement a data structure to store a set of integers and quickly compute
# range sums

from sys import stdin


class Vertex:
    def __init__(self, key, sum, left, right, parent):
        (self.key, self.sum, self.left, self.right, self.parent) = (
            key,
            sum,
            left,
            right,
            parent,
        )


def update(v):
    if v == None:
        return
    v.sum = (
        v.key
        + (v.left.sum if v.left != None else 0)
        + (v.right.sum if v.right != None else 0)
    )
    if v.left != None:
        v.left.parent = v
    if v.right != None:
        v.right.parent = v


def smallRotation(v):
    parent = v.parent
    if parent == None:
        return
    grandparent = v.parent.parent
    if parent.left == v:
        m = v.right
        v.right = parent
        parent.left = m
    else:
        m = v.left
        v.left = parent
        parent.right = m
    update(parent)
    update(v)
    v.parent = grandparent
    if grandparent != None:
        if grandparent.left == parent:
            grandparent.left = v
        else:
            grandparent.right = v


def bigRotation(v):
    if v.parent.left == v and v.parent.parent.left == v.parent:
        smallRotation(v.parent)
        smallRotation(v)
    elif v.parent.right == v and v.parent.parent.right == v.parent:
        smallRotation(v.parent)
        smallRotation(v)
    else:
        smallRotation(v)
        smallRotation(v)


def splay(v):
    if v == None:
        return None
    while v.parent != None:
        if v.parent.parent == None:
            smallRotation(v)
            break
        bigRotation(v)
    return v


def find(root, key):
    v = root
    last = root
    next = None
    while v != None:
        if v.key >= key and (next == None or v.key < next.key):
            next = v
        last = v
        if v.key == key:
            break
        if v.key < key:
            v = v.right
        else:
            v = v.left
    root = splay(last)
    return (next, root)


def split(root, key):
    (result, root) = find(root, key)
    if result == None:
        return (root, None)
    right = splay(result)
    left = right.left
    right.left = None
    if left != None:
        left.parent = None
    update(left)
    update(right)
    return (left, right)


def merge(left, right):
    if left == None:
        return right
    if right == None:
        return left
    while right.left != None:
        right = right.left
    right = splay(right)
    right.left = left
    update(right)
    return right


root = None


def insert(x):
    global root
    (left, right) = split(root, x)
    new_vertex = None
    if right == None or right.key != x:
        new_vertex = Vertex(x, x, None, None, None)
    root = merge(merge(left, new_vertex), right)


def erase(x):
    global root
    if not search(x):
        return
    (left, right) = split(root, x + 1)
    (left, middle) = split(left, x)
    root = merge(left, right)


def search(x):
    global root
    result, root = find(root, x)
    if result is None or result.key != x:
        return False
    root = splay(result)
    return True


def sum(fr, to):
    global root
    (left, middle) = split(root, fr)
    (middle, right) = split(middle, to + 1)
    ans = middle.sum if middle else 0
    root = merge(merge(left, middle), right)
    return ans


MODULO = 1000000001
n = int(stdin.readline())
last_sum_result = 0
for i in range(n):
    line = stdin.readline().split()
    if line[0] == "+":
        x = int(line[1])
        insert((x + last_sum_result) % MODULO)
    elif line[0] == "-":
        x = int(line[1])
        erase((x + last_sum_result) % MODULO)
    elif line[0] == "?":
        x = int(line[1])
        print("Found" if search((x + last_sum_result) % MODULO) else "Not found")
    elif line[0] == "s":
        l = int(line[1])
        r = int(line[2])
        res = sum((l + last_sum_result) % MODULO, (r + last_sum_result) % MODULO)
        print(res)
        last_sum_result = res % MODULO
