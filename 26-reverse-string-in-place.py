#!python

from __future__ import print_function
import unittest

######################################################################
# this problem is from
# https://www.interviewcake.com/question/python/reverse-string-in-place
#

# Write a function to reverse a string in-place(*).

# (*) Since strings in Python are immutable, first convert the string into a
# list of characters, do the in-place reversal on that list, and re-join
# that list into a string before returning it. This isn't technically
# "in-place" and the list of characters will cost O(n)O(n) additional
# space, but it's a reasonable way to stay within the spirit of the
# challenge. If you're comfortable coding in a language with mutable
# strings, that'd be even better!

#
######################################################################

# Now my turn


def reverse_bytes_in_place(l):
    """reverse the list in place"""

    n = len(l)
    for i in range(n / 2):
        (l[i], l[n - i - 1]) = (l[n - i - 1], l[i])

    # I like my solution that uses these in place, no need for a
    # temp val swap but at hacker news, someone says the "correct"
    # way is, and I think they are right, to use extended slices
    # as:

    # return l[::-1]

    return l


def string_reverse(string):
    """reverse a string 'in place' in place"""

    # raise TypeError # (actual correct Python answer)

    b = bytearray(string)
    b = reverse_bytes_in_place(b)

    return str(b)


# Now Test


class TestReverseStringInPlace(unittest.TestCase):

    def test_string_reverse_in_place(self):
        """test string reversal"""
        self.assertEqual("", string_reverse(""))
        self.assertEqual("e", string_reverse("e"))
        self.assertEqual("abcd", string_reverse("dcba"))
        self.assertEqual("abcde", string_reverse("edcba"))
        self.assertEqual("jihgfedcba", string_reverse("abcdefghij"))

if __name__ == "__main__":
    # unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestReverseStringInPlace)
    unittest.TextTestRunner(verbosity=2).run(suite)
