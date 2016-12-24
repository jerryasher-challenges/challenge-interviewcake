#!python

######################################################################
# this problem is from
# https://www.interviewcake.com/question/python/balanced-binary-tree

# Write a function to see if a binary tree is "superbalanced" (a new
# tree property we just made up).

# A tree is "superbalanced" if the difference between the depths of any
# two leaf nodes is no greater than one.

######################################################################

# Now my turn

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

    # recursively walk the binary tree top down
    # note the depth at each descent
    # and keep a list of the various leaf node depths
    # as soon as imsuperbalance is discovered
    # return false
    def is_superbalanced(self, leaf_depths=None, depth=0):
        if leaf_depths is None:
            leaf_depths = []
        depth = depth + 1

        # print("{:{width}}is_superbalanced: {} {} ({})"
        #       .format(' ', depth, leaf_depths, self.value, width=depth))

        # a leaf node has no children
        if self.left is None and self.right is None:

            # two ways we might now have an unbalanced tree:
            #   1) more than 2 different leaf depths
            #   2) Two leaf depths that are more than 1 apart

            if depth not in leaf_depths:
                # print("{} : {}".format(depth, self.value))
                leaf_depths.append(depth)

            if len(leaf_depths) > 2:
                return False

            if (max(leaf_depths) - min(leaf_depths)) > 1:
                return False

            return True

        if self.left:
            check = self.left.is_superbalanced(leaf_depths, depth)
            if not check:
                return False

        if self.right:
            check = self.right.is_superbalanced(leaf_depths, depth)
            if not check:
                return False

        return True


class TestBinaryTreeNodes(unittest.TestCase):

    def setUp(self):
        # [caseno, superbalanced, list_tree]
        self.cases = [
            [0, True, [1]],
            [1, True, [1, None, None]],
            [2, True, [1, 2, None]],
            [3, True, [1, 2, 3]],
            [4, True, [1, [2, None, None], None]],
            [5, True, [1,
                       ['2l',
                        '3ll',
                        '3lr'],
                       None]],
            [6, True, [1,
                       ['2l', ['3ll', '4lll', '4llr'], '3lr'],
                       ['2r', ['3rl', '4rll', '4rlr'], '3rr']]],
            [7, True, [5, [10, 20, 25], [15, 30, 35]]],
            [8, False, [
                5, [10, 20, [25, 40, None]], [15, None, None]]],
            [9, False, [5,
                        [10, None, None],
                        [15,
                         None,
                         [20,
                          [25,
                           [30, 40]]]]]],
            [10, False, [5,
                         10,
                         [15, None, [20, [25, [30, 40]]]]]],
            [11, True, [5,
                        [10, [20, 40, 45], [25, 50, 55]],
                        [15, [30, 60, 65], [35, 70, 75]]]],
            [12, True, [5,
                        [10,
                         [20,
                          [40, 80, 90],
                          [45, 95, 100]],
                         [25,
                          [50, 105, 110],
                          [55, 115, 120]]],
                        [15,
                         [30,
                          [60, 125, 130],
                          [65, 135, 140]],
                         [35,
                          [70, 145, 150],
                          [75, 155, 160]]]]],
            [13, False, [5,
                         [10,
                          [20,
                           [40, 80, 90],
                           [45, 95, 100]],
                          25],
                         [15,
                          [30,
                           [60, 125, 130],
                           [65, 135, 140]],
                          [35,
                           [70, 145, 150],
                           [75, 155, 160]]]]],
            [14, False, [5,
                         [10,
                          [20,
                           [40, 80],
                           [45, 95, 100]],
                          [25,
                           [50],
                           [55, 115, 120]]],
                         [15,
                          [30,
                           [60, 125, [130, 165]],
                           [65, 135, 140]],
                          [35,
                           [70, 145, 150],
                           [75, 155, 160]]]]],
            [15, True, [5,
                        [10,
                         [20,
                          [40, 80]]]]],
        ]
        print("setup: %s cases" % len(self.cases))

    def test_4balance(self):
        for (caseno, designed_superbalanced, case) in self.cases:
            print("\ncase %2s: %s" % (caseno, case))
            bt = list_tree_to_BinaryTree(case)
            computed_superbalanced = bt.is_superbalanced()
            by_design = ""
            if not designed_superbalanced and not computed_superbalanced:
                by_design = "(by design)"
            if designed_superbalanced and not computed_superbalanced:
                by_design = "!!! ERROR!"

            print("{:{width}}{}superbalanced {}"
                  .format('', '' if computed_superbalanced else "not ",
                          by_design, width=6))

            if designed_superbalanced and not computed_superbalanced:
                self.fail()


# Coming from lisp, I like to see trees implemented in pure list
# structures, [1 [2 21 22] [3 31 32]] if only because they are easy to
# visualize and to create as tests. I refer to such trees here as a
# list_tree

# however, interviewcake prefers a more java/c traditional
# [node, ptr_left, ptr_right] structure so I have added a routine
# that let me create testcases using lisplike trees and then
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
    unittest.main()
