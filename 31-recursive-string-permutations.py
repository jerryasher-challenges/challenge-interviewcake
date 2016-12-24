#!python

from __future__ import print_function
import unittest

######################################################################
# this problem is from
# https://www.interviewcake.com/question/python/recursive-string-permutations
#

# Write a recursive function for generating all permutations of an input
# string. Return them as a set.

# Don't worry about time or space complexity -- if we wanted efficiency
# we'd write an iterative version.

# To start, assume every character in the input string is unique.

# Your function can have loops -- it just needs to also be recursive.

#
######################################################################

# Now my turn


def permute(string):
    """returns a list of all permutations of the input string"""

    if len(string) <= 1:
        return set([string])

    all_permutations = []

    for i in range(len(string)):
        first = string[i]
        rest = string[:i] + string[i + 1:]
        permutations = permute(rest)
        for permutation in permutations:
            all_permutations.append(first + permutation)

    return set(all_permutations)

# And now the tests


class TestStringPermutations(unittest.TestCase):

    def test_s(self):
        """some simple tests"""
        tests = [
            ["", [""]],
            ["a", ["a"]],
            ["ab", ["ab", "ba"]],
            ["abc", ["abc", "acb", "bac", "bca", "cab", "cba"]],
            ["abcd",
             [
                 'abcd', 'abdc', 'acbd', 'acdb', 'adbc', 'adcb',
                 'bacd', 'badc', 'bcad', 'bcda', 'bdac', 'bdca',
                 'cabd', 'cadb', 'cbad', 'cbda', 'cdab', 'cdba',
                 'dabc', 'dacb', 'dbac', 'dbca', 'dcab', 'dcba']]
        ]

        for string, soln in tests:
            soln_set = set(soln)
            permutation_set = permute(string)
            print("\npermutation of '%s' is %s" %
                  (string, permutation_set), end="")
            self.assertEqual(soln_set, permutation_set,
                             "permutations of '%s' should be %s but are %s" %
                             (string, soln_set, permutation_set))
        print("")


if __name__ == "__main__":
    # unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestStringPermutations)
    unittest.TextTestRunner(verbosity=2).run(suite)
