#!python

from __future__ import print_function
import unittest

######################################################################
# this problem is from
# https://www.interviewcake.com/question/python/merge-sorted-arrays
#

# In order to win the prize for most cookies sold, my friend Alice and I
# are going to merge our Girl Scout Cookies orders and enter as one
# unit.

# Each order is represented by an "order id" (an integer).

# We have our lists of orders sorted numerically already, in
# lists. Write a function to merge our lists of orders into one sorted
# list.

# For example:

my_list = [3, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14, 19]

# print merge_lists(my_list, alices_list)

#
######################################################################

# Now my turn...


def merge_lists(listi, listj):
    """merge these two sorted lists"""

    sortd = []
    i = 0
    j = 0
    leni = len(listi)
    lenj = len(listj)
    while i < leni or j < lenj:
        ith = listi[i] if i < leni else float('inf')
        jth = listj[j] if j < lenj else float('inf')
        if ith < jth:
            i += 1
            sortd.append(ith)
        else:
            j += 1
            sortd.append(jth)
    return sortd

# Now Test


class TestMergeSortedArrays(unittest.TestCase):

    def test_given(self):
        print(merge_lists(my_list, alices_list))


if __name__ == "__main__":
    # unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMergeSortedArrays)
    unittest.TextTestRunner(verbosity=2).run(suite)
