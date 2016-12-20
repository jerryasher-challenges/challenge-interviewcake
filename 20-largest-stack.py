#!python

from __future__ import print_function
import unittest

######################################################################
# this problem is from
# https://www.interviewcake.com/question/python/largest-stack
#

# You want to be able to access the largest element in a stack.

# You've already implemented this Stack class.


class Stack:

    # initialize an empty list
    def __init__(self):
        self.items = []

    # push a new item to the last index
    def push(self, item):
        self.items.append(item)

    # remove the last item
    def pop(self):
        # if the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items:
            return None
        return self.items.pop()

    # see what the last item is
    def peek(self):
        if not self.items:
            return None
        return self.items[-1]

# Use your Stack class to implement a new class MaxStack with a function
# get_max() that returns the largest element in the stack. get_max()
# should not remove the item.

# Your stacks will contain only integers.

#
######################################################################

# Now my turn


class MaxStack(Stack):

    def get_max(self):
        if self.items.peek():
            return max(self.items)


# Now let's test


class TestMaxStack(unittest.TestCase):

    def setUp(self):
        self.q = Queue()

    def test_queuedequue(self):
        """queue up 5 integers, check they are in there, dequeue them, check for emptiness, perform other blackbox and whitebox tests"""
        self.assertTrue(self.q.is_empty())
        self.assertTrue(self.q.q.is_empty())
        self.assertTrue(self.q.b.is_empty())

        l = range(5)
        for i in l:
            self.q.enqueue(i)

        self.assertEqual(4, self.q.peek())
        self.assertEqual(l, self.q.q.stk)

        s = []
        l.reverse()
        for i in l:
            elt = self.q.dequeue()
            s.append(elt)

        self.assertTrue(self.q.is_empty())
        self.assertTrue(self.q.q.is_empty())
        self.assertTrue(self.q.b.is_empty())

        l.reverse()
        self.assertEqual(s, l)
        self.assertEqual([], self.q.b.stk)
        self.assertEqual([], self.q.q.stk)

if __name__ == "__main__":
    # unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestQueueTwoStacks)
    unittest.TextTestRunner(verbosity=2).run(suite)
