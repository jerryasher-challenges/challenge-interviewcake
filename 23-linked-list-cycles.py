#!python

from __future__ import print_function
import unittest

######################################################################
# this problem is from
# https://www.interviewcake.com/question/python/linked-list-cycles
#

# You have a singly-linked list and want to check if it contains a cycle.

# A singly-linked list is built with nodes, where each node has:

# node.next -- the next node in the list.

# node.value -- the data held in the node. For example, if our linked
# list stores people in line at the movies, node.value might be the
# person's name.

# For example:


class LinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next = None

# A cycle occurs when a node's next points back to a previous node in
# the list. The linked list is no longer linear with a beginning and
# end -- instead, it cycles through a loop of nodes.

# Write a function contains_cycle() that takes the first node in a
# singly-linked list and returns a boolean indicating whether the list
# contains a cycle.


#
######################################################################

# Now my turn


def contains_cycle(node):
    """detect a cycle in a singly linked list"""

    # I seem to recall some sort of algorithm which uses two ptrs, one
    # advances quickly, the other advances slowly. If there is no
    # cycle, it comes to an end in n time. If there is a cycle,
    # eventually the fast ptr catches up to the slow ptr and we found a
    # cycle, again proportional to n time.

    slow = node
    while node.next and node.next.next:
        # print("%s: %s->%s" % (n, node.value, node.next))
        slow = slow.next
        node = node.next.next
        if node is slow:
            return True
    return False

# Now Test


class TestDetectCycle(unittest.TestCase):

    def setUp(self):
        self.a = LinkedListNode('A')
        self.b = LinkedListNode('B')
        self.c = LinkedListNode('C')
        self.d = LinkedListNode('D')
        self.e = LinkedListNode('E')
        self.f = LinkedListNode('F')
        self.g = LinkedListNode('G')
        self.h = LinkedListNode('H')
        self.i = LinkedListNode('I')
        self.j = LinkedListNode('J')

        self.a.next = self.b
        self.b.next = self.c
        self.c.next = self.d
        self.d.next = self.e
        self.e.next = self.f
        self.f.next = self.g
        self.g.next = self.h
        self.h.next = self.i
        self.i.next = self.j

    def test_detect0(self):
        """no cycles"""
        # print("")
        # for node in [self.a,
        #              self.b,
        #              self.c,
        #              self.d,
        #              self.e,
        #              self.f,
        #              self.g,
        #              self.h,
        #              self.i,
        #              self.j]:
        #     print("%s -> %s" % (node.value, node.next))

        self.assertFalse(contains_cycle(self.a))

    def test_detect1acycle(self):
        """a cycle"""
        self.j.next = self.a

        self.assertTrue(contains_cycle(self.a))

    def test_detect1alatecycle(self):
        """a cycle"""
        self.j.next = self.h

        self.assertTrue(contains_cycle(self.a))

    def test_detect1asmallcycle(self):
        """a cycle"""
        self.j.next = self.j

        self.assertTrue(contains_cycle(self.a))

if __name__ == "__main__":
    # unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestDetectCycle)
    unittest.TextTestRunner(verbosity=2).run(suite)
