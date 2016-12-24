#!python

######################################################################
# this problem is from
# https://www.interviewcake.com/question/second-largest-item-in-bst

# Write a function to find the 2nd largest element in a binary search tree

# Here are two implementations:
# 1: the "obvious" that sorts the tree and pulls out penultimate
# 2: and one that exploits knowledge of structure of a binary search tree
#    to find the two possible locations the penultimate might be at
######################################################################

import unittest

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

    # sort a binary tree with in-order traversal
    def uniq_sort(self, nodes=None, depth=0):
        if nodes is None:
            nodes = []
        depth = depth + 1
        if self.left:
            self.left.uniq_sort(nodes, depth)

        if len(nodes) > 0:
            if nodes[-1] != self.value:
                nodes.append(self.value)
        else:
            nodes.append(self.value)

        if self.right:
            self.right.uniq_sort(nodes, depth)
        return nodes

    # Find the 2nd largest element in a binary search tree
    # assumes it has been given a valid bst
    # this version requires a sort
    def second_largest(self):
        sort = self.uniq_sort()
        if len(sort) > 1:
            return sort[-2]
        else:
            return None

    # Find the 2nd largest element in a binary search tree
    # assumes it has been given a valid bst
    # this version avoids sorting the tree
    # by exploiting a bit of knowledge about binary search trees
    # and quite frankly is inspired by a google search of the question
    # this is one reason why "how would you do this..." interview
    # questions should be answered "I would think about and I would
    # google it".

    def second_largest2(self):
        """a sol'n that uses knowledge of binary trees to avoid sort"""
        n = 0
        pptr = self
        rptr = self.right
        # we want the second to last rightmost node
        # which we find with two following ptrs
        # when the first ptr falls off the tree
        # the ppptr points to the second to last node
        while rptr:
            n += 1
            ppptr = pptr
            pptr = rptr
            rptr = rptr.right
        if self.right:
            if n >= 1:
                return ppptr.value
            else:
                return None

        n = 0
        pptr = self
        rptr = self.left
        # now we want the last rightmost node
        # which we find with a following ptr
        # when the first ptr falls off the tree
        # the pptr points to the last node
        while rptr:
            n += 1
            pptr = rptr
            rptr = rptr.right
        if self.left:
            if n >= 1:
                return pptr.value
            else:
                return None
        return None

# now test


class TestBinaryTreeNodes(unittest.TestCase):

    def setUp(self):
        # [second_largest, list_tree]
        self.cases = [
            [None, [1]],
            [2, [2, 1, 3]],
            [15, [12, [10, 8, 11], [15, 14, 16]]],
            [11, [12, [10, 8, 11]]],
            [10, [12, [10, 8]]]
        ]
        print("setup: %s cases" % len(self.cases))

    def test_bst(self):
        caseno = 0
        for (soln, case) in self.cases:
            print("\ncase %2s: %s" % (caseno, case))
            bt = list_tree_to_BinaryTree(case)

            # test the sorting soln
            second = bt.second_largest()
            print("  second_largest is %s" % second)
            self.assertEqual(
                soln, second,
                "expected soln {} is not {}".format(soln, second))

            # now test the quicker soln
            second2 = bt.second_largest2()
            print("  second_largest2 is %s" % second2)
            self.assertEqual(
                soln, second2,
                "expected soln {} is not {}".format(soln, second2))

            caseno += 1

# a helper fn to convert from my preferred lisp list_tree format
# to nodey binary trees

# Coming from lisp, I like to see trees implemented in pure list
# structures, [1 [2 21 22] [3 31 32]] if only because they are easy to
# visualize and to create as tests. I refer to such trees here as a
# list_tree

# however, interviewcake prefers a more java/c traditional
# [node, ptr_left, ptr_right] structure so I have added a few routines
# that let me create testcases using lisplike trees and then
# converting them to ptrful trees.


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
