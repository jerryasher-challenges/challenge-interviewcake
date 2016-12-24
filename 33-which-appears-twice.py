#!python

from __future__ import print_function
import unittest

######################################################################
# this problem is from
# https://www.interviewcake.com/question/python/which-appears-twice
#

# I have a list where every number in the range 1...n appears once
# except for one number which appears twice.

# Write a function for finding the number that appears twice.

#
######################################################################

# Now my turn

# 1. first try, not seen, 1/2 a binary search until I realized list of
#    ints is not necessarily sorted.
# 2. 2nd try, in my head, can I xor them? Nah.

# 3. 3rd try, I recall the gaussian formula to add n consecutive
#    integers, and then realize I can quickly determine this number
#    as well as sum my entire list
#    and the difference will be the duplicated number


def which_twice(ints):
    """find the number in ints that appears twice"""

    n = len(ints)
    # n ints, so the list is
    # 1..(n-1) + some duplicated number
    # = ((n-1) * (1 + n - 1) / 2)
    # = ((n-1) * (n) / 2)
    # = ((n-1) * (n / 2.0)
    gauss = int((n - 1) * (n / 2.0))
    total = sum(ints)
    dupe = total - gauss
    return dupe


class TestTwice(unittest.TestCase):

    def test_examples(self):
        """test some examples"""
        tests = [
            [1, [1, 1, 2, 3]],
            [2, [1, 2, 2, 3]],
            [2, [1, 2, 2, 3]],
            [2, [1, 2, 2, 3]],
            [2, [1, 2, 2, 3]],
            [3, [3, 1, 2, 3]],
        ]

        for soln, ints in tests:
            print("")
            print("%s <- %s" % (soln, ints))
            ans = which_twice(ints)
            print("%s <= %s" % (ans, ints))
            self.assertEqual(soln, ans)


if __name__ == "__main__":
    # unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTwice)
    unittest.TextTestRunner(verbosity=2).run(suite)
