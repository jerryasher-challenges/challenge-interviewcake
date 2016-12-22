#!python

from __future__ import print_function
from operator import itemgetter
import unittest

######################################################################
# this problem is from
# https://www.interviewcake.com/question/highest-product-of-3
# interviewcake 4
# https://www.interviewcake.com/question/python/merging-ranges

# Your company built an in-house calendar tool called HiCal. You want to
# add a feature to see the times in a day when everyone is available.
#
# To do this, you'll need to know when any team is having a meeting. In
# HiCal, a meeting is stored as tuples of integers (start_time,
# end_time). These integers represent the number of 30-minute blocks
# past 9:00am.
#
# For example:
#
# (2, 3) # meeting from 10:00 - 10:30 am
# (6, 9) # meeting from 12:00 - 1:30 pm
#
# Write a function merge_ranges() that takes a list of meeting time
# ranges and returns a list of condensed ranges.
#
# For example, given:
#
test1 = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
#
# your function would return:

soln1 = [(0, 1), (3, 8), (9, 12)]

# Do not assume the meetings are in order. The meeting times are coming
# from multiple teams.
#
# Write a solution that's efficient even when we can't put a nice upper
# bound on the numbers representing our time ranges. Here we've
# simplified our times down to the number of 30-minute slots past 9:00
# am. But we want the function to work even for very large numbers, like
# Unix timestamps. In any case, the spirit of the challenge is to merge
# meetings where start_time and end_time don't have an upper bound.

######################################################################

# Now my turn

# I seem to recall seeing this before solved by a first pass sort of
# the ranges then a second pass merging ranges using a push down list
# to push and pop new ranges, so let's try that...


def merge_ranges(meetings):
    if len(meetings) <= 1:
        return meetings

    meetings = sorted(meetings, key=itemgetter(0))
    pdl = [meetings[0]]
    meetings = meetings[1:]
    for (nstart, nend) in meetings:
        (start, end) = pdl[-1]
        if nstart <= end:
            if end <= nend:
                end = nend
            pdl[-1] = (start, end)
        else:
            pdl.append((nstart, nend))
    return pdl


class TestMergingRanges(unittest.TestCase):

    def test_givenexample(self):
        """test any examples from the problem"""
        print("")
        for soln, test in [
                [[(0, 1), (3, 8), (9, 12)],
                 [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]]]:
            print("merge_ranges %s" % test)
            print("  is %s (should be %s)" % (merge_ranges(test), soln))
            self.assertEqual(soln, merge_ranges(test))

    def test_others(self):
        """test other trials"""
        print("")
        for soln, test in [
                [[(-4, 8), (9, 12)],
                 [(3, 5), (-4, 8), (10, 12), (9, 10)]],
                [[(0, 3)],
                 [(0, 3), (1, 2)]]]:
            print("merge_ranges %s" % test)
            print("  is %s (should be %s)" % (merge_ranges(test), soln))
            self.assertEqual(soln, merge_ranges(test))


if __name__ == "__main__":
    # # unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMergingRanges)
    unittest.TextTestRunner(verbosity=2).run(suite)
