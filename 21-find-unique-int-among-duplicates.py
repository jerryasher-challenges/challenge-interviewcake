#!python

from __future__ import print_function
import unittest
import operator

######################################################################
# this problem is from
# https://www.interviewcake.com/question/python/find-unique-int-among-duplicates
#

# Your company delivers breakfast via autonomous quadcopter drones. And
# something mysterious has happened.

# Each breakfast delivery is assigned a unique ID, a positive
# integer. When one of the company's 100 drones takes off with a
# delivery, the delivery's ID is added to a list,
# delivery_id_confirmations. When the drone comes back and lands, the ID
# is again added to the same list.

# After breakfast this morning there were only 99 drones on the
# tarmac. One of the drones never made it back from a delivery. We
# suspect a secret agent from Amazon placed an order and stole one of
# our patented drones. To track them down, we need to find their
# delivery ID.

# Given the list of IDs, which contains many duplicate integers and one
# unique integer, find the unique integer.

# The IDs are not guaranteed to be sorted or sequential. Orders aren't
# always fulfilled in the order they were received, and some deliveries
# get cancelled before takeoff.

#
######################################################################

# Now my turn

# My first thoughts are to use two hash tables. One collects unique
# ids, the other collects dup ids. Since hash insertion, deletion,
# lookup is a constant, this should be O(n) where n is length of id
# list.


def find_unique_int(ids):
    """find one unique id in a list of random, possibly duplicated, integers"""
    uids = {}
    dups = {}
    for id in ids:
        if id not in dups:
            if id in uids:
                del uids[id]
                dups[id] = True
            else:
                uids[id] = True
    for key in uids.keys():
        return key
    return None

# interviewcake first uses a solution that uses one hash table (but
# requires an n and n-1 scans), then suggests that given the problem
# statement: these are ints, and the list containts duplicates, where
# *duplicate* is a strict double entry, not a multiple entry, then we
# don't need a hash table, but can use a single integer and an
# XOR. Wow. Okay, that is true, but um, what a crazy arbitrary sort of
# problem


def find_unique_intxor(ids):
    """find one unique id in a list of random, possibly duplicated, integers"""
    unique = reduce(operator.xor, ids)
    return unique

# So this is a clever implementation, but comparing it to the prior
# find duplicates, it is much more brittle and works ONLY for this one
# specific problem where there is ONE unique and the rest are
# duplicate entries where duplicate means precisely TWO and never TWO
# OR MORE.

# Now Test


class TestFindUniqueInt(unittest.TestCase):

    def test_FindUniqueInt0Empty(self):
        self.assertEqual(None, find_unique_int([]))

    def test_FindUniqueInt0One(self):
        self.assertEqual(1, find_unique_int([1]))

    def test_FindUniqueInt0Two(self):
        self.assertEqual(None, find_unique_int([1, 1]))

    def test_FindUniqueInt1Many(self):
        self.assertEqual(1, find_unique_int(
            [1, 2, 3, 4, 4, 3, 2, 5, 6, 6, 5, 100, 101, 101, 100]))

    def test_FindUniqueIntXOR0EmptyRaisesError(self):
        self.assertRaises(TypeError, find_unique_intxor, [])

    def test_FindUniqueIntXOR0One(self):
        self.assertEqual(1, find_unique_intxor([1]))

    def test_FindUniqueIntXOR0Two(self):
        self.assertEqual(0, find_unique_intxor([1, 1]))

    def test_FindUniqueIntXOR1JustRight(self):
        self.assertEqual(1, find_unique_intxor(
            [1, 2, 3, 4, 4, 3, 2, 5, 6, 6, 5, 100, 101, 101, 100]))

    def test_FindUniqueIntXOR2Many(self):
        """too many uniques means the wrong answer is returned"""
        self.assertEqual(103, find_unique_intxor(
            [1, 2, 3, 4, 4, 3, 2, 5, 6, 6, 5, 100, 101, 101, 100, 102]))


if __name__ == "__main__":
    # unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFindUniqueInt)
    unittest.TextTestRunner(verbosity=2).run(suite)
