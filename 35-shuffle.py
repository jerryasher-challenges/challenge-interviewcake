#!python

from __future__ import print_function
import random
import unittest

######################################################################
# this problem is from
# https://www.interviewcake.com/question/python/shuffle
#

# Write a function for doing an in-place shuffle of a list.

# The shuffle must be "uniform," meaning each item in the original list
# must have the same probability of ending up in each spot in the final
# list.

# Assume that you have a function get_random(floor, ceiling) for getting
# a random integer that is >= floor and <= ceiling.
#
######################################################################

# Now my turn

# I'll implement the canonical shuffle in place algorithm then test it
# to make sure it fits the statistical definition of a uniform random
# shuffle

random.seed()


def get_random(floor, ceiling):
    """return a random number in the closed interval (floor, ceiling)"""
    return random.randint(floor, ceiling)  # randint does this already


# this is interviewcake's non-uniform naive shuffle
# stripped of comments, it differs from the in_place_uniform_shuffle
# by 1 character. (A critical 1 character difference!)

# using statistics in the unit tests, it can be seen that the naive
# shuffle never converges on a uniform shuffling, empirically, the
# variance can at times be seen to increase even with increasing
# repetitions.

def naive_shuffle(the_list):
    # for each index in the list

    n = len(the_list)

    for i in xrange(0, n - 1):

        # grab a random other index
        j = get_random(0, n - 1)

        # and swap the values
        the_list[i], the_list[j] = the_list[j], the_list[i]


# the canonical shuffle in place algorithm


def in_place_uniform_shuffle(the_list):
    """in place shuffle of a the_list"""

    n = len(the_list)

    # sweep each position in turn marching up the the_list
    # (do not bother with the nth element, which would swap with itself)
    for i in xrange(0, n - 1):
        # at each position of the_list put an element chosen from
        # remainder of the the_list
        j = get_random(i, n - 1)
        # print("%s <--> %s" % (i, j))
        the_list[i], the_list[j] = the_list[j], the_list[i]


class TestShuffle(unittest.TestCase):

    def test_demo(self):
        """demonstrate random shuffles"""
        for i in xrange(4, 7):
            for shuffle in [in_place_uniform_shuffle]:
                print("")
                print(shuffle.__name__)
                the_list = [element for element in xrange(i)]
                print("the_list was %s" % the_list)
                shuffle(the_list)
                print("     now %s" % the_list)
                print("")
        self.assertTrue(True)

    def test_uniformity(self):
        """test to make sure this is a uniform shuffle"""

        # if this is a uniform shuffle, then after some bignum
        # repetitions, we should see every element appear in every
        # position of the the_list, uniformly.

        # the average of 0..9 is 4.5
        # if the elements are uniformly shuffled, over bignum repetitions
        # at every position in the the_list, the average of all elements
        # shuffled into that position should be 4.5

        for shuffle in [naive_shuffle, in_place_uniform_shuffle]:

            print("\n\n%s\n" % shuffle.__name__)

            n = 10
            for trials in [1, 5, 10, 100, 1000, 10000]:
                count = [0 for i in range(n)]
                for trial in range(trials):
                    the_list = [i for i in range(n)]
                    shuffle(the_list)
                    for i in range(n):
                        count[i] += the_list[i]

                print("%s shuffles" % trials)
                print("      counts % s" % count)
                average = [count[i] / float(trials) for i in range(n)]
                print("    averages %s" % average)

                total = sum(average)
                mean = total / float(n)
                sq_diffs = [(average[i] - mean) ** 2 for i in range(n)]
                variance = sum(sq_diffs) / n
                stddev = variance**0.5

                print("        mean %s   variance %.6s   standard deviation %.6s"
                      % (mean, variance, stddev))

        # leaving the above loop, the last trial was of 10000 shuffles
        # using the in place uniform shuffle

        # the test of uniformity has shuffled the the_list 10000 times
        # and computes the averages of all the elements shuffled into
        # each position, and ensures standard deviation of the
        # averages is close to zero

        self.assertAlmostEqual(stddev, 0, delta=0.1)


if __name__ == "__main__":
    # unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestShuffle)
    unittest.TextTestRunner(verbosity=2).run(suite)
