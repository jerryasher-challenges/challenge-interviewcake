#!python

from __future__ import print_function
import unittest

######################################################################
# this problem is from
# https://www.interviewcake.com/question/python/reverse-linked-list
#

# Hooray! It's opposite day. Linked lists go the opposite way today.
# Write a function for reversing a linked list. Do it in-place.

# Your function will have one input: the head of the list.
# Your function should return the new head of the list.

# Here's a sample linked list node class:


class LinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next = None

#
######################################################################

# Now my turn


def reverse_linked_list(head):
    """reverse a singly linked list in place"""
    if head:
        onebehind = None
        twobehind = None
        while head.next:
            twobehind = onebehind
            onebehind = head
            head = head.next
            onebehind.next = twobehind
        head.next = onebehind
    return head


def ll2list(head):
    """converts our linked list to a python list"""
    if head:
        list = [head.value]
        while head.next:
            head = head.next
            list.append(head.value)
        return list
    else:
        return None

# Now Test


class TestReverseLinkedList(unittest.TestCase):

    def setUp(self):
        self.a = LinkedListNode('A')
        self.b = LinkedListNode('B')
        self.c = LinkedListNode('C')
        self.d = LinkedListNode('D')

        self.a.next = self.b
        self.b.next = self.c
        self.c.next = self.d

    def test_0empty(self):
        """No linked list just None"""
        head = reverse_linked_list(None)
        self.assertEquals(None, head)

    def test_1node(self):
        """a linked list of one element"""
        self.a.next = None
        head = reverse_linked_list(self.a)
        self.assertEqual(self.a, head)

    def test_4banger(self):
        """no cycles"""

        l1 = ll2list(self.a)
        head = reverse_linked_list(self.a)
        l2 = ll2list(head)
        l2.reverse()
        self.assertEquals(l1, l2)

if __name__ == "__main__":
    # unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestReverseLinkedList)
    unittest.TextTestRunner(verbosity=2).run(suite)
