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


def in_place_uniform_shuffle(deck):
    """in place shuffle of a deck"""

    n = len(deck)

    # sweep each position in turn marching up the deck
    # (do not bother with the nth card, which would swap with itself)
    for i in xrange(0, n - 1):
        # at each position put a card chosen from remainder of the deck
        j = get_random(i, n - 1)
        # print("%s <--> %s" % (i, j))
        deck[i], deck[j] = deck[j], deck[i]


class TestShuffle(unittest.TestCase):

    def test_demo(self):
        """demonstrate random shuffles"""
        for i in xrange(4, 7):
            for shuffle in [in_place_uniform_shuffle]:
                print("")
                print(shuffle.__name__)
                deck = [card for card in xrange(i)]
                print("deck was %s" % deck)
                shuffle(deck)
                print("     now %s" % deck)
                print("")
        self.assertTrue(True)

    def test_uniformity(self):
        """test to make sure this is a uniform shuffle"""

        # if this is a uniform shuffle, then after some bignum
        # repetitions, we should see every card appear in every
        # position of the deck, uniformly.

        # the average of 0..9 is 4.5
        # if the cards are uniformly shuffled, over bignum repetitions
        # at every position in the deck, the average of all cards
        # shuffled into that position should be 4.5

        print("")

        ncards = 10
        for i in [1, 5, 10, 100, 1000, 10000]:
            count = [0 for card in range(ncards)]
            for trial in range(i):
                deck = [card for card in range(ncards)]
                in_place_uniform_shuffle(deck)
                for index in range(ncards):
                    count[index] += deck[index]

            print("% i shuffles" % i)
            print("      counts % s" % count)
            average = [count[index] / float(i) for index in range(ncards)]
            print("    averages %s" % average)

            total = sum(average)
            mean = total / float(ncards)
            variance = sum([(average[index] - mean) ** 2
                            for index in range(ncards)])
            variance = variance / (index**0.5)
            stddev = variance**0.5

            print("        mean %s   variance %.6s   standard deviation %.6s"
                  % (mean, variance, stddev))

        # the test of uniformity has shuffled the deck 10000 times and
        # computes the averages of all the cards at each position, and
        # ensures standard deviation of the averages is close to zero

        self.assertAlmostEqual(stddev, 0, delta=0.1)


if __name__ == "__main__":
    # unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestShuffle)
    unittest.TextTestRunner(verbosity=2).run(suite)
