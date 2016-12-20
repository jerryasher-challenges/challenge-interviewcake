#!python

from __future__ import print_function
import unittest

######################################################################
# this problem is from
# https://www.interviewcake.com/question/python/queue-two-stacks
#
# Implement a queue with two stacks

# Optimize for the time cost of m function calls on your queue. These
# can be any mix of enqueue and dequeue calls.

# Assume you already have a stack implementation and it gives O(1)O(1)
# time push and pop.

#
######################################################################

# Now my turn


class Stack():

    def __init__(self):
        self.stk = []

    def pop(self):
        """raises IndexError if you pop when it's empty"""
        return self.stk.pop()

    def push(self, elt):
        self.stk.append(elt)

    def is_empty(self):
        return len(self.stk) == 0

    def peek(self):
        if not self.stk.is_empty():
            return self.stk[-1]


class Queue():

    def __init__(self):
        self.q = Stack()  # the primary queue
        self.b = Stack()  # the reverse, opposite q (a joke: q vs b)
        self.front = None

    def is_empty(self):
        return self.q.is_empty()

    def peek(self):
        if self.q.is_empty():
            return None
        else:
            return self.front

    def enqueue(self, elt):
        self.front = elt
        self.q.push(elt)

    def dequeue(self):
        """raises IndexError if you dequeue from an empty queue"""
        while not self.q.is_empty() > 0:
            elt = self.q.pop()
            self.b.push(elt)
        val = self.b.pop()
        elt = None
        while not self.b.is_empty() > 0:
            elt = self.b.pop()
            self.q.push(elt)
        self.front = elt
        return val


# Now let's test


class TestQueueTwoStacks(unittest.TestCase):

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
