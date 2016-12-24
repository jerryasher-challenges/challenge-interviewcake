#!python

from __future__ import print_function
import unittest

######################################################################
# this problem is from
# https://www.interviewcake.com/question/python/top-scores
#

# You created a game that is more popular than Angry Birds.

# You rank players in the game from highest to lowest score. So far
# you're using an algorithm that sorts in O(n log(n)) time, but
# players are complaining that their rankings aren't updated fast
# enough. You need a faster sorting algorithm.

# Write a function that takes:

# + a list of unsorted_scores
# + the highest_possible_score in the game

# and returns a sorted list of scores in less than O(n log(n)) time.

# For example:

#  unsorted_scores = [37, 89, 41, 65, 91, 53]
#  HIGHEST_POSSIBLE_SCORE = 100

# sort_scores(unsorted_scores, HIGHEST_POSSIBLE_SCORE)
# # returns [37, 41, 53, 65, 89, 91]

# We're defining n as the number of unsorted_scores because we're
# expecting the number of players to keep climbing.

# And we'll treat highest_possible_score as a constant instead of
# factoring it into our big O time and space costs, because the highest
# possible score isn't going to change. Even if we do redesign the game
# a little, the scores will stay around the same order of magnitude.


#
######################################################################

# Now my turn

# after some googling, this seems to call for a count sort which is
# o(n) if you know the highest value
# this is a translation of the wiki pseudo code at
# https://en.wikipedia.org/wiki/Counting_sort#The_algorithm
# which is basically python into python and into the specific
# requirements of this problem.

# note: I try this twice with sort_scores and sort_scores2, where
# sort_scores2 is a cleaned up and optimized version of
# sort_scores. Both work, but sort_scores2 is more understandable,
# uses less space, and should basically have the same runtime and
# complexity

def sort_scores(scores, high):
    """sorts a list of scores. high is the highest possible"""

    print("")

    # variables:
    #    scores -- the array of items to be sorted;
    #    high -- a number such that all keys are in the range 0..high - 1
    #    count -- an array of numbers, with indexes 0..k-1, initially all zero
    #    n -- length of scores array
    #    sorted_scores -- an array of items, with indexes 0..n-1
    #    x -- an individual input item, used within the algorithm
    #    total, oldCount, i -- numbers used within the algorithm

    count = [0] * (high + 1)

    # calculate the histogram of scores:
    for x in scores:
        count[x] += 1

    print("%s scores" % ((len(scores))))
    print(scores)
    print("%s counts" % ((len(count) + 1)))
    print(count)

    # calculate the starting index for each key:

    total = 0
    for i in range(high + 1):   # i = 0, 1, ... k-1
        oldCount = count[i]
        count[i] = total
        total += oldCount

    print(count)

    # copy to output array, preserving order of scores with equal keys:
    sorted_scores = [0] * (len(scores))
    for x in scores:
        index = count[x]
        sorted_scores[index] = x
        count[x] += 1

    return sorted_scores


# so count sort  is a pretty interesting sorting algorithm, but it would
# seem to be appropriate only when the high value is itself a
# relatively low number as we have to alloc an array of that size.

# it's apparently NOT the interview cake soln as this soln is
# o(highest score) in size and interview cake insists it can be done
# in o(n) space.

# let's rethink this.

# there is a lot of empty space in the count array, maybe we can turn
# that into a dict where keys of the dict are the scores

def sort_scores2(scores, high):
    """sorts a list of scores. high is the highest possible"""

    count = {}

    # calculate the histogram of scores:
    for x in scores:
        score = count.get(x, 0)
        count[x] = score + 1

    # transcribe the histogram into the sorted scores
    sorts = []
    for i in range(high + 1):   # i = 0, 1, ... k-1
        if i in count:
            eyes = [i] * count[i]
            sorts.extend(eyes)

    print("scores %s sorted is %s" % (scores, sorts))
    return sorts

# Conclusion: the count combined with a has reduces the space of a
# sparse set of scores immensely. I would say this sort is o(n + k)
# where n is the number of input scores and k is the high score.

# Conclusion2: sort_scores2 using the dict, seems more pythonic, and
# also seems much easier to understand. In comparison, sort_scores is
# very clunky, although the unmodified wiki algorithm it came with has
# the machinery to sort more than just a list of scores.

# And now the tests


class TestTopScores(unittest.TestCase):

    def test_examples(self):
        """test some examples"""
        tests = [
            [[3, 8, 5, 3, 2], 11],
            [[37, 89, 41, 65, 91, 53], 100],
            [[37, 89, 41, 65, 91, 53, 41], 100],
            [[37, 89, 41, 45, 45, 45, 45, 45, 45, 65, 91, 53, 37, 41, 65], 100],
            [[37, 89, 41, 65, 91, 53, 37, 41, 65], 100],
        ]

        for fn in (sort_scores, sort_scores2):

            print("")
            print(fn.__name__)

            for unsortd, high in tests:
                sortd = sorted(unsortd)
                result = fn(unsortd, high)
                self.assertEqual(result, sortd,
                                 "sorting %s should be %s was %s" %
                                 (unsortd, sortd, result))

        print("")


if __name__ == "__main__":
    # unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTopScores)
    unittest.TextTestRunner(verbosity=2).run(suite)
