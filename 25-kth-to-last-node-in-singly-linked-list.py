#!python

from __future__ import print_function
import unittest

######################################################################
# this problem is from
# https://www.interviewcake.com/question/python/kth-to-last-node-in-singly-linked-list
#

# You have a linked list and want to find the kth to last node

# Write a function kth_to_last_node() that takes an integer k and the
# head_node of a singly linked list, and returns the kth to last node
# in the list.

# For example:


class LinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next = None

# a = LinkedListNode("Angel Food")
# b = LinkedListNode("Bundt")
# c = LinkedListNode("Cheese")
# d = LinkedListNode("Devil's Food")
# e = LinkedListNode("Eccles")

# a.next = b
# b.next = c
# c.next = d
# d.next = e

# kth_to_last_node(2, a)


#
######################################################################

# Now my turn


def kth_to_last_node(k, head):
    """return the kth to last node. 0th and 1th to last return the last"""

    # English is funny, because "second to the last" means "next to"
    # and there is no such thing as "first to the last"

    # so kth to the last has no meaning unless k > 1
    # since there is no meaning to it, may as well return head

    # in general then, to find the kth from last
    # let n be k - 1
    # then find the nth element from the last

    # do this with a ptr that walks n elements behind an advancing ptr

    i = 0
    kth = head
    while(head and head.next):
        head = head.next
        if i == k - 1:
            kth = kth.next
        else:
            i += 1
    return kth

# Now Test


class TestKthToLast(unittest.TestCase):

    def test_givenexample(self):
        """test the given example"""

        a = LinkedListNode("Angel Food")
        b = LinkedListNode("Bundt")
        c = LinkedListNode("Cheese")
        d = LinkedListNode("Devil's Food")
        e = LinkedListNode("Eccles")

        a.next = b
        b.next = c
        c.next = d
        d.next = e

        self.assertEqual("Devil's Food", kth_to_last_node(2, a).value)

    def test_KthToLast(self):
        """test the kth to last nodes for all ks"""

        # English is funny, because "second to the last" means "next to"
        # and there is no such thing as "first to the last"

        print("")
        for i in range(5):
            self.llist = LinkedListNode(0)

            last = self.llist
            for j in range(1, i + 1):
                last.next = LinkedListNode(j)
                last = last.next

            print("\n%s" % ll2list(self.llist))

            nl = ""
            for k in range(2, i + 2):
                value = kth_to_last_node(k, self.llist).value
                if k == i + 1:
                    nl = "\n"
                print("kth %s->%s  " % (k, value), end=nl)
                self.assertEqual(i - (k - 1), value)


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

if __name__ == "__main__":
    # unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestKthToLast)
    unittest.TextTestRunner(verbosity=2).run(suite)
