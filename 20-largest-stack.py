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

    def get_max_bad_bad_bad(self):
        """simple, but works by peeking into super's internal data"""
        # a more sophisticated design might keep track of the max
        # value separately and not requiring spying into the super's
        # abstraction.

        # that would be better oop, less likely to break in the
        # future, but likely slower to run, harder to implement and
        # test,

        # it's easy to keep track of the max separately by writing our
        # own push and pop that reference super, IF all values in the
        # stack are unique. otherwise duplicate entries of the max
        # value makes the actual max value harder to maintain

        if self.peek():
            return max(self.items)


# Now let's test


class TestMaxStack(unittest.TestCase):

    def test_MaxStack0Empty(self):
        """test an empty stack"""
        ms = MaxStack()
        self.assertEqual(None, ms.get_max_bad_bad_bad())

    def test_MaxStack1Filled(self):
        """test a stack with a bunch of nums"""
        ms = MaxStack()
        for i in range(4):
            ms.push(i)
        ms.push(100)
        for i in range(5, 10):
            ms.push(i)

        self.assertEqual(100, ms.get_max_bad_bad_bad())

    def test_MaxStack2MultipleMaxes(self):
        """test a stack with a multiple occurrences of the same max num"""
        ms = MaxStack()
        for i in range(4):
            ms.push(i)
        ms.push(100)
        for i in range(5, 10):
            ms.push(i)
        ms.push(110)
        ms.push(100)

        self.assertEqual(110, ms.get_max_bad_bad_bad())
        ms.pop()
        self.assertEqual(110, ms.get_max_bad_bad_bad())
        ms.pop()
        self.assertEqual(100, ms.get_max_bad_bad_bad())
        ms.pop()
        ms.pop()
        ms.pop()
        ms.pop()
        ms.pop()
        self.assertEqual(100, ms.get_max_bad_bad_bad())
        ms.pop()
        self.assertEqual(3, ms.get_max_bad_bad_bad())

if __name__ == "__main__":
    # unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMaxStack)
    unittest.TextTestRunner(verbosity=2).run(suite)
