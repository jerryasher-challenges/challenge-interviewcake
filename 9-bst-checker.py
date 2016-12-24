#!python

######################################################################
# this problem is from
# https://www.interviewcake.com/question/bst-checker

# ------------------------------

# Write a function to see if a binary tree is a valid binary search tree

# A binary tree is a tree where every node has two or fewer
# children. The children are usually called left and right.

# ----------- review -----------
#
# A * perfect * binary tree has no gaps, and the leaf nodes are all at the
# bottom of the tree.

# Property 1:
#     the number of total nodes on each "level" doubles as we
# move down the tree.

# Property 2:
#     the number of nodes on the last level is equal to the sum
# of the number of nodes on all other levels(plus 1). In other words,
# about half of our nodes are on the last level.

# Let's call the number of nodes n, and the height of the tree as h,
# where h starts at 1. h can also be thought of as the "number of
# levels."

# If a perfect binary tree has height h, how many nodes does it have?

# n = 2 ^ h - 1

# Let's call the number of nodes n, and the height of the tree h. h can
# also be thought of as the "number of levels."

# If we had h, how could we calculate n?

# n = 2 ^ h - 1
# n + 1 = 2 ^ h
# ln(n + 2) = h * ln(2)
# h = ln(n + 2) / ln(2)

# A binary search tree is a binary tree in which, for each node:

# The node's value is greater than all values in the left subtree.

# The node's value is less than all values in the right subtree.

# BSTs are useful for quick lookups. If the tree is balanced, we can
# search for a given value in the tree in O(\lg{n})O(lgn) time.

######################################################################

# Now my turn

import unittest

# ------------------------------

# Here's a sample binary tree node class:


class BinaryTreeNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert_left(self, value):
        self.left = value
        return self.left

    def insert_right(self, value):
        self.right = value
        return self.right

    # ------------------------------

    def __str__(self):
        s = "<" + str(self.value) + ", " + str(self.left) + \
            ", " + str(self.right) + ">"
        return s

    # A function to check a binary tree is a valid binary search tree

    # A binary search tree is a binary tree in which, for each node:
    #   The node's value is greater than all values in the left subtree.
    #   The node's value is less than all values in the right subtree.
    #   The above two conditions imply a valid bst has unique elements

    def is_bst(self, depth=0):
        depth += 1

        inf = float('inf')
        lmin = rmin = inf
        lmax = rmax = -inf

        if self.left:
            (lvalid, lmin, lmax) = self.left.is_bst(depth)

            if not lvalid:
                return False, None, None
            if self.value <= lmax:
                print("{:{width}}left: {} is not > {}!".format(
                    "", self.value, lmax, width=depth))
                return False, None, None

        if self.right:
            (rvalid, rmin, rmax) = self.right.is_bst(depth)

            if not rvalid:
                return False, None, None
            if self.value >= rmin:
                print("{:{width}}right: {} is not < {}!".format(
                    "", self.value, rmin, width=depth))
                return False, None, None

        nmin = min([lmin, rmin, self.value])
        nmax = max([lmax, rmax, self.value])

        print("{:{width}}min:{} < value:{} < max:{}".format(
            "", lmax, self.value, rmin, width=depth))
        return self.value, nmin, nmax

# now test


class TestBinaryTreeNodes(unittest.TestCase):

    def setUp(self):
        # [valid_bst, list_tree]
        self.cases = [
            [True, [1]],
            [False, [1, 2, None]],
            [True, [2, 1, 3]],
            [False, [2, 1, 2]],
            [False, [2, 1, 1]],
            [False, [3, 2, 1]],
            [True, [12, [10, 8, 11], [15, 14, 16]]],
            [False, [12, [10, 8, 13], [15, 10, 16]]],
            [False, [12, [10, 8, 11], [11, 12, 16]]],
            [False, [12, [10, 8, 11], [13, 14, 16]]],
        ]
        print("setup: %s cases" % len(self.cases))

    def test_bst(self):
        caseno = 0
        for (designed_bst, case) in self.cases:
            print("\ncase %2s: %s" % (caseno, case))
            bt = list_tree_to_BinaryTree(case)
            (valid, min, max) = bt.is_bst()

            by_design = ""
            if not designed_bst and not valid:
                by_design = "(by design)"
            if designed_bst and not valid:
                by_design = "!!! ERROR!"
            if not designed_bst and valid:
                by_design = "!!! ERROR!"

            if valid:
                print("{:{width}} {} <= {} <= {} => valid bst {}"
                      .format('',
                              min, valid, max,
                              by_design, width=6))
            else:
                print("{:{width}} not a valid bst {}"
                      .format('',
                              by_design, width=6))

            self.assertNotEqual(by_design, "!!! ERROR!")

            caseno += 1

# Coming from lisp, I like to see trees implemented in pure list
# structures, [1 [2 21 22] [3 31 32]] if only because they are easy to
# visualize and to create as tests. I refer to such trees here as a
# list_tree

# however, interviewcake prefers a more java/c traditional
# [node, ptr_left, ptr_right] structure so I have added a routine
# that lets me create testcases using lisplike trees and then
# converting them to ptrful trees.

# a helper fn to convert from my preferred lisp list_tree format
# to nodey binary trees


def list_tree_to_BinaryTree(list_tree):

    # this just helps with short hand "trees"
    # of forms 1, or [1] changing it into [1, None, None]
    # then truncating
    if type(list_tree) is not list:
        list_tree = [list_tree, None, None]
    list_tree = list_tree + [None, None, None]
    list_tree = list_tree[0:3]

    (value, left, right) = list_tree

    node = BinaryTreeNode(value)

    if left:
        node.insert_left(list_tree_to_BinaryTree(left))

    if right:
        node.insert_right(list_tree_to_BinaryTree(right))

    return node


if __name__ == "__main__":
    # unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestBinaryTreeNodes)
    unittest.TextTestRunner(verbosity=2).run(suite)
