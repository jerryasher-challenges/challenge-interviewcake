#!python

from __future__ import print_function
import random
import unittest

######################################################################
# this problem is from
# https://www.interviewcake.com/question/python/simulate-7-sided-die
#

# You have a function rand5() that generates a random integer from 1 to
# 5. Use it to write a function rand7() that generates a random integer
# from 1 to 7.

# rand5() returns each integer with equal probability. rand7() must also
# return each integer with equal probability.

######################################################################

# now my turn


def rand5():
    """return a random integer from 1 to 5"""
    return random.randrange(1, 6)

# first try:


# implementation of the canonical rejection sampling algorithm (found
# by googling)

def rand7():
    """return a random integer from 1 to 7"""
    while True:
        r1 = 5 * (rand5() - 1)
        r2 = rand5()
        r = r1 + r2
        if r <= 21:
            return r % 7 + 1


def rand7natural():
    """return a random integer from 1 to 7"""
    return random.randrange(1, 8)


# now test


class Test5SidedDie(unittest.TestCase):

    def test_rand5(self):
        """test the uniformity of the solution, by computing std deviation
        after many trials, showing it converges to a small number"""
        for fn in [rand7, rand7natural]:
            print("\n%s" % fn.__name__)
            for trials in [100, 1000, 10000, 100000]:
                freq = [0] * 7
                for i in range(trials):
                    r = fn()
                    i = r - 1
                    freq[i] += 1

                total = sum(freq)
                mean = total / (7.0 * trials)
                averages = [freq[j] / float(trials) for j in range(7)]
                diffs = [(averages[j] - mean) for j in range(7)]
                sq_diffs = [diffs[j] ** 2 for j in range(7)]
                variance = sum(sq_diffs) / 7.0
                stddev = variance**0.5

                print("\n%s trials" % trials)
                print("7 sided die rolls %s" % freq)
                print("averages %s" % averages)
                print("mean %5.4s  variance %5.4s  stddev %8.6s" %
                      (mean, variance, stddev))

                self.assertAlmostEqual(stddev, 0, delta=0.05)


if __name__ == "__main__":
    # unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(Test5SidedDie)
    unittest.TextTestRunner(verbosity=2).run(suite)
