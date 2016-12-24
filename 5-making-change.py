#!python

from __future__ import print_function
import unittest

######################################################################
# this problem is from
# interviewcake 5 Making Change
# https://www.interviewcake.com/question/python/coin

# Imagine you landed a new job as a cashier...
#
# Your quirky boss found out that you're a programmer and has a weird
# request about something they've been wondering for a long time.
#
# Write a function that, given:
#
# 1. an amount of money
# 2. a list of coin denominations
#
# computes the number of ways to make amount of money with coins of the
# available denominations.
#
# Example: for amount=4 (4c) and denominations=[1,2,3] (1c, 2c and 3c),
# your program would output 4 - the number of ways to make
# 4c with those denominations:
#
# 1c, 1c, 1c, 1c
# 1c, 1c, 2c
# 1c, 3c
# 2c, 2c

#
######################################################################

# Now my turn

###
# first try: recursion this is a recursive solution.  while this
# works, mostly, apparently this is a problem that can be solved with
# a dynamic programming solution (if you can recognize it)
# the change-making problem
# (https://en.wikipedia.org/wiki/Change-making_problem)

# but let's see first what recursion can do, then later, retry with
# some hints from interviewcake


def make_change1(amount, denominations):
    """return num ways to make change from denominations"""
    denominations.sort()
    denominations.reverse()

    # _make_change1 will return ALL the ways change can be made
    # this includes duplicates like (2, 1) being the same as (1, 2)
    patterns = _make_change1(amount, denominations)

    # so uniquify will eliminate the dupes
    uniques = uniquify(patterns)
    count = len(uniques)
    return count


def _make_change1(amount, denominations, level=0):
    """recursive procedure to find all ways combinations of demoniations sum to amount"""
    patterns = []
    for d in denominations:
        (quotient, remainder) = divmod(amount, d)
        if quotient > 0:
            if quotient == 1 and remainder == 0:
                patterns.append([d])
            else:
                sub_patterns \
                    = _make_change1(amount - d, denominations, level + 1)
                for pattern in sub_patterns:
                    pat = [d]
                    pat.extend(pattern)
                    patterns.append(pat)
    return patterns


def uniquify(patterns):
    """remove duplicates from a set of change making patterns"""
    s = set()
    # patterns is a list of lists
    # each pattern is a decomposition of the summands of the amount in terms
    # of the denominations
    # we sort the decomposition so that (2, 1) becomes (1, 2)
    # stringify it
    # toss it into a python set (to eliminate any dups)
    # and return the set
    for p in patterns:
        p.sort()
        strp = str(p)
        s.add(strp)
    elts = list(s)
    elts.sort()
    return elts


# trial 2, the dynamic solution canonically given as the soln to this problem
# is much faster and use far less space than the recursive method
# coming up with the dynamic solution on the other hand....


def make_change2(amount, denominations):
    """return num ways to make use change from denominations to add to amount (dynamic)"""

    ncointypes = len(denominations)

    # ways is an array, where from 0 cents to the target amount
    # ways holds a list of ways the given denominations can sum to the target
    # amount
    ways = [[0 for x in range(ncointypes)] for z in range(amount + 1)]

    # Using a dynamic solution, determine the ways for every postive
    # amount less than our target amount, building a table, a cache of
    # amounts that help us find the number of ways for the target
    # amount

    # for each amount from 0 up to our target amount
    for curr_amt in range(1, amount + 1):

        # find the number of ways of using all the coins to sum to the
        # current amount by looping over each coin

        for coin in range(ncointypes):

            # 1. find ways to get to the current amount minus our current coin

            sub_amount = curr_amt - denominations[coin]
            if sub_amount < 0:
                sub_amt_ways = 0
            elif sub_amount == 0:
                sub_amt_ways = 1  # 0 plus our current coin = curr amount
            else:
                sub_amt_ways = ways[sub_amount][coin]

            # 2. lookup the prior ways we found to get the current
            #    amount with the prior coins
            # here's where the dynamicism occurs:

            old_ways = ways[curr_amt][coin - 1]

            # the total ways is the sum of both ways
            ways[curr_amt][coin] = sub_amt_ways + old_ways

    count = ways[amount][ncointypes - 1]

    return count


# and now test


class TestMakeChange(unittest.TestCase):

    def change(self, text, fn, amount, denominations):
        """a helper fn"""
        count = fn(amount, denominations)
        print("%s: %s ways to make change for %s using %s" %
              (text, count, amount, denominations))
        return count

    def test_givenexample1(self):
        """test the given example"""
        amount = 4
        denominations = [1, 2, 3]
        count = self.change("dynamic", make_change2, amount, denominations)
        self.assertEqual(4, count)

    def test_21(self):
        """change for 1 cent"""
        amount = 1
        denominations = [1, 2, 3]
        count = self.change("dynamic", make_change2, amount, denominations)
        self.assertEqual(1, count)

    def test_22(self):
        """change for 2 cents"""
        amount = 2
        denominations = [1, 2, 3]
        count = self.change("dynamic", make_change2, amount, denominations)
        self.assertEqual(2, count)

    def test_23(self):
        """change for 3 cents"""
        amount = 3
        denominations = [1, 2, 3]
        count = self.change("dynamic", make_change2, amount, denominations)
        self.assertEqual(3, count)

    def test_24(self):
        """change for 4 cents"""
        amount = 4
        denominations = [1, 2, 3]
        count = self.change("dynamic", make_change2, amount, denominations)
        self.assertEqual(4, count)

    def test_more(self):
        """more tests that help determine if the recurse and dynamic approaches are both correct"""
        tests = [
            [1, 1, [1]],
            [0, 1, [2]],
            [0, 1, [3]],
            [1, 2, [1]],
            [2, 2, [1, 2]],
            [2, 2, [1, 2, 3]],
            [0, 2, [3]],
            [4, 4, [1, 2, 3]],
            [5, 10, [2, 5, 3, 6]],
            [85, 23, [1, 3, 5, 7, 8, 11]]]
        for soln, amount, denoms in tests:
            count = self.change("dynamic", make_change2, amount, denoms)
            self.assertEqual(soln, count)
        for soln, amount, denoms in tests:
            count = self.change("recursive", make_change1, amount, denoms)
            self.assertEqual(soln, count)

# conclusion, the dynamic solution is far far faster!

if __name__ == "__main__":
    # unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMakeChange)
    unittest.TextTestRunner(verbosity=2).run(suite)
