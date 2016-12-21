#!python

from __future__ import print_function
import unittest
import operator

######################################################################
# this problem is from
# https://www.interviewcake.com/question/python/delete-node
#

# Delete a node from a singly-linked list , given only a variable
# pointing to that node.

# The input could, for example, be the variable b below:


class LinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next = None


def example():
    a = LinkedListNode('A')
    b = LinkedListNode('B')
    c = LinkedListNode('C')

    a.next = b
    b.next = c

    delete_node(b)


#
######################################################################

# Now my turn

# obvious attack: overwrite and shift up

# what this really does is overwriting our current node with data from
# the following node. That next node will be garbage collected if
# nothing else points to it.  This seemingly fails when you are handed
# the last node. Sure you can mark it's data as invalid, but still the
# prior node's next will still point to this ghost of a node.

def delete_node(node):
    """deletes a node from the middle of a linked list"""

    ptr = node.next
    if ptr:
        node.next = ptr.next
        node.value = ptr.value

    else:
        # tail end node, what to do?
        # seemingly only thing to do is raise an Exception
        raise ValueError("Bad input! Can't delete tail node.")

# Now Test


class TestDeleteNode(unittest.TestCase):

    def setUp(self):
        self.a = LinkedListNode('A')
        self.b = LinkedListNode('B')
        self.c = LinkedListNode('C')
        self.a.next = self.b
        self.b.next = self.c

    def test_DeleteNode(self):
        """delete a node from middle of list"""
        delete_node(self.b)
        self.assertEqual('C', self.a.next.value)
        self.assertEqual(self.b, self.a.next)

    def test_DeleteTailNode(self):
        """delete a tail end and raise an Exception"""
        self.assertRaises(ValueError, delete_node, self.c)


if __name__ == "__main__":
    # unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestDeleteNode)
    unittest.TextTestRunner(verbosity=2).run(suite)
