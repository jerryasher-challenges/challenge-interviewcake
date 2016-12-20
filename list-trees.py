#!python

# A tree can be expressed in Python has nested lists.
# Walk such a tree in BFS
# Then walk the tree in DFS, pre-order, in-order, post-order

import unittest


def _printNode(node, **kwargs):
    print(node)


def breadth_first_walk(tree, fn=None, **kwargs):
    """
    http://algorithms.tutorialhorizon.com/breadth-first-searchtraversal-in-a-binary-tree
    """
    if fn is None:
        fn = _printNode
    q = [tree]
    while len(q) > 0:
        node = q.pop()
        if type(node) is not list:
            node = [node, None, None]
        node.extend([None, None, None])
        node = node[0:3]
        (value, left, right) = node
        if value:
            fn(value, **kwargs)
        if left:
            q.insert(0, left)
        if right:
            q.insert(0, right)


def depth_first_walk(tree, depth=0, fn=None, **kwargs):
    if fn is None:
        fn = _printNode

    # this nonsense just helps with short hand "trees"
    # of forms 1, or [1] changing it into [1, None, None]
    # then truncating
    if type(tree) is not list:
        tree = [tree, None, None]
    tree.extend([None, None, None])
    tree = tree[0:3]

    (value, left, right) = tree
    if value:
        fn(value, **kwargs)
    if left:
        depth_first_walk(left, depth + 1, fn, **kwargs)
    if right:
        depth_first_walk(right, depth + 1, fn, **kwargs)


class TestListTrees(unittest.TestCase):

    cases = []

    def setUp(self):
        Tree1Level1 = [1]
        Tree1Level2 = [1, None, None]
        Tree2Level1 = [1, 2, None]
        Tree2Level2 = [1, 2, 3]
        Tree2Level3 = [1, [2, None, None], None]
        Tree3Level1 = [1, ['2l', '3ll', '3lr'], None]
        Tree4Level1 = [1, ['2l', ['3ll', '4lll', '4llr'], '3lr'],
                       ['2r', ['3rl', '4rll', '4rlr'], '3rr']]
        Tree9Level0 = [5, [10, 20, 25], [15, 30, 35]]
        TestListTrees.cases = [
            Tree1Level1,
            Tree1Level2,
            Tree2Level1,
            Tree2Level2,
            Tree2Level3,
            Tree3Level1,
            Tree4Level1,
            Tree9Level0
        ]
        print("setup: %s cases" % len(TestListTrees.cases))

    def test_0bf(self):
        print("test_0bf: breadth_first_walk")
        n = 0
        for case in TestListTrees.cases:
            n += 1
            print("\ncase %s: %s" % (n, case))
            breadth_first_walk(case)
        self.assertTrue(True)

    def test_0df(self):
        print("test_0df: depth_first_walk")
        n = 0
        for case in TestListTrees.cases:
            n += 1
            print("\ncase %s: %s" % (n, case))
            depth_first_walk(case)
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
