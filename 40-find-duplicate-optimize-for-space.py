#!python

from __future__ import print_function
import random
import unittest

######################################################################
# this problem is from
# https://www.interviewcake.com/question/python/find-duplicate-optimize-for-space
#

# Find a duplicate, Space Edition.

# We have a list of integers, where:

# + The integers are in the range 1..n
# + The list has a length of n+1

# It follows that our list has at least one integer which appears at
# least twice. But it may have several duplicates, and each duplicate
# may appear more than twice.

# Write a function which finds an integer that appears more than once in
# our list. (If there are multiple duplicates, you only need to find one
# of them.)

# We're going to run this function on our new, super-hip Macbook Pro
# With Retina Display. Thing is, the damn thing came with the RAM
# soldered right to the motherboard, so we can't upgrade our RAM. So we
# need to optimize for space!

# Gotchas

# We can do this in O(1) space.
# We can do this in less than O(n^2) time, while keeping O(1) space.
# We can do this in O(n log n) time and O(1) space.
# We can do this without destroying the input.

#
######################################################################

# Now my turn well almost...

######################################################################
# Interviewcake goes on to says
# https://www.interviewcake.com/question/python/find-duplicate-optimize-for-space-beast-mode

#  We can find a duplicate integer in O(n) time while keeping our space
#  cost at O(1)

# This is a tricky one to derive (unless you have a strong background in
# graph theory), so we'll get you started:

# Imagine each item in the list as a node in a linked list. In any
# linked list , each node has a value and a "next" pointer. In this
# case:

# The value is the integer from the list.

# The "next" pointer points to the value-eth node in the list (numbered
# starting from 1). For example, if our value was 3, the "next" node
# would be the third node.

# list        [2, 3, 1, 3]
# position     1  2  3  4
# linked list  2->3->1<-3
######################################################################

# Now my turn...

# so the hint from interviewcake, the bonus "beast" mode make me think
# of how one would find a cycle in a linked list, and we did that
# earlier in interviewcake problem 23, linked-list-cycles.

# and we did that by starting at a tail, and using "floyd's algorithm".
# and we could do that here as well, if we only had a tail...

# but as explained here:
# http://aperiodic.net/phil/archives/Geekery/find-duplicate-elements.html

# we do know a tail...

# since the numbers are:
# + The integers are in the range 1..n
# + The list has a length of n+1

# then we know nothing in the list from 1..n can point to list[n+1],
# so we can start floyd walking at n+1, follow the graph till we hit
# the cycle, and determine the start of the cycle (according to floyd)
# and that will be a duplicate.


def find_duplicate(list):
    """find a duplicate of 1..n in a list n+1 elements long"""

    n = len(list)
    i = n
    j = n
    while True:
        print("looking for cycle: i %s j %s" % (i, j))
        i = list[i - 1]  # tortoise
        j = list[j - 1]  # hare
        j = list[j - 1]  # hare
        if i == j:
            print("cycle found at %s" % i)
            break

    # we found a cycle
    # now restart j
    # and loop until j meets i again
    # and that's the start of the cycle (or the dup)

    j = n
    while True:
        print("looking for dup: i %s j %s" % (i, j))
        i = list[i - 1]
        j = list[j - 1]
        if i == j:
            print("dup found at %s" % i)
            break

    print("dup is %s" % i)
    return i


# Now Test


class TestFindDuplicate(unittest.TestCase):

    def test_given(self):
        print("")
        dup = find_duplicate([2, 3, 1, 3])
        self.assertEqual(3, dup)

    def test_more(self):
        print("")
        for i in range(20):
            n = random.randrange(4, 7)
            l = range(1, n + 1)
            dup = random.randrange(1, n + 1)
            l.append(dup)
            random.shuffle(l)
            print("l is %s" % l)
            found_dup = find_duplicate(l)
            self.assertEqual(dup, found_dup)

if __name__ == "__main__":
    # unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFindDuplicate)
    unittest.TextTestRunner(verbosity=2).run(suite)
