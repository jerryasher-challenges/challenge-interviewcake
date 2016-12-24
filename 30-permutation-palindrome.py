#!python

from __future__ import print_function
import unittest

######################################################################
# this problem is from
# https://www.interviewcake.com/question/python/permutation-palindrome
#

# Write an efficient function that checks whether any permutation of an
# input string is a palindrome

# Examples:

#  "civic" should return True
#  "ivicc" should return True
#  "civil" should return False
#  "livci" should return False

#
######################################################################

# Now my turn

# so at first it seems like we need an efficent way to come up with
# all permutations of an input string. But I think if we consider what
# we know about palindromes...

# A palindrome will have either have every letter in it occurring a
# multiple of 2 times, or will have one letter appearing an odd number
# of times, and the rest appearing a multiple of 2 times.

# so if we just maintain a count of each letter's number of
# occurrences and test at the end that there are only zero or one odd
# letters then we should know if we have a palindrome possibility.

# we will assume case sensitivity
# we not strip out any non alphabetical characters


def could_be_a_palindrome(string):
    """returns True if any permutation of the string might be a palindrome"""

    # we will assume case sensitivity
    # we not strip out any non alphabetical characters

    freq = {}

    for ch in string:
        if ch in freq:
            del freq[ch]
        else:
            freq[ch] = True

    return len(freq) <= 1

    # And now the tests


class TestPermutationPalindrome(unittest.TestCase):

    def test_0givenexample(self):
        """test the given example"""

        tests = [
            [True, "civic"],
            [True,  "ivicc"],
            [False,  "civil"],
            [False,  "livci"]]

        for valid, string in tests:
            self.assertEqual(valid, could_be_a_palindrome(string),
                             "%s should be %s" % (string, valid))

    def test_1simpletons(self):
        """some more simple tests"""
        tests = [
            [False, "canal"],
            [True, "a man a plan a canal panama"],
            [True, "amanaplanacanalpanama"],
            [False, "panama"],
            [True, "kayak"],
            [True, "madam"],
            [True, "racecar"],
            [True, "tattarrattat"],
            [False, "tattarrattatxes"]]

        for valid, string in tests:
            self.assertEqual(valid, could_be_a_palindrome(string),
                             "%s should be %s" % (string, valid))


if __name__ == "__main__":
    # unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPermutationPalindrome)
    unittest.TextTestRunner(verbosity=2).run(suite)
