#!python

from __future__ import print_function
import unittest

######################################################################
# this problem is from
# https://www.interviewcake.com/question/highest-product-of-3

# Given a list_of_ints, find the highest_product you can get from three of
# the integers.

# The input list_of_ints will always have at least three integers.


def highest_product0(list_of_ints):
    """two neg nums may be bigger than three pos nums. do both products. return max"""

    # I think this is the correct approach for this problem, it reduces
    # logic complexity by trying both of the possible answers, determining
    # the actual max in its last comparison

    # it is presumably o(n log n) with one sort that could go to o(n^2)
    # there is an o(n) sol'n but logic is more complex, and requires many many
    # more mults

    list_of_ints.sort()

    min0 = list_of_ints[0]
    min1 = list_of_ints[1]

    max0 = list_of_ints[-1]
    max1 = list_of_ints[-2]
    max2 = list_of_ints[-3]

    poss1 = min0 * min1 * max0
    poss2 = max0 * max1 * max2

    return poss1 if poss1 > poss2 else poss2  # such an ugly ternary conditional


def highest_productordern(list_of_ints):
    """a greedy order n approach taken off web (with a critical bug fix!)"""
    # from
    # https://knaidu.gitbooks.io/problem-solving/content/primitive_types/highest_product_of_3.html

    # Maintain the following values as we traverse the array
    # lowest_number
    # highest_number
    # lowest_product_of_2
    # highest_product_of_2
    # highest_product_of_3

    low = min(list_of_ints[0], list_of_ints[1])
    high = max(list_of_ints[0], list_of_ints[1])

    low_prod2 = high_prod2 = list_of_ints[0] * list_of_ints[1]
    high_prod3 = high_prod2 * list_of_ints[2]

    i = 2
    while i < len(list_of_ints):
        curr = list_of_ints[i]
        high_prod3 = max(
            high_prod2 * curr,
            low_prod2 * curr,
            high_prod3)

        low_prod2 = min(low * curr, low_prod2)
        high_prod2 = max(high * curr, high_prod2)

        high = max(high, curr)
        low = min(low, curr)
        i += 1  # heh, knaidu web book never incrs i, and so oo loop

    return high_prod3


# first approach, correct and better than brute force, but way too
# many comparisons (ie complex logic)
def highest_product1(list_of_ints):
    """return the highest product, use logic to figure out which three operands to use"""

    # this has two sorts, both are of sublists
    # this works, is correct, but logic is a bit complex
    # probably simpler mainteance with highest_product0

    neg = []
    pos = []
    for int in list_of_ints:
        if int < 0:
            neg.append(int)
        else:
            pos.append(int)
    neg.sort()
    pos.sort()

    if len(pos) == 0:
        # no pos ints, so highest number are three "small" negs
        return(neg[-3] * neg[-2] * neg[-1])
    elif len(pos) == 1:
        # 1 pos int, so return that * prod of two "large" negs
        return(neg[0] * neg[1] * pos[-1])
    elif len(neg) >= 2:
        maxneg = neg[0] * neg[1]
        if maxneg > pos[-3] * pos[-2]:
            return maxneg * pos[-1]
    elif len(pos) == 2:
        return neg[-1] * pos[-2] * pos[-1]
    else:
        return pos[-3] * pos[-2] * pos[-1]


class TestHighestProduct(unittest.TestCase):

    def test_givenexample(self):
        """test the example from the problem"""
        for soln, test in [
                [300, [-10, -10, 1, 3, 2]],
        ]:
            self.assertEqual(soln, highest_product0(test))

    def test_givenexampleordern(self):
        """test the example from the problem using order n soln"""
        for soln, test in [
                [300, [-10, -10, 1, 3, 2]],
        ]:
            self.assertEqual(soln, highest_productordern(test))

    def test_highestproduct(self):
        """test all 3 highest_product strategies, make sure they are equal to each other"""
        print("")
        for t in [
                [1, 2, 3],
                [-1, 0, 1],
                [-3, -4, 2],
                [0, 1, 2, 3, 4, 5],
                [-1, 0, 1, 2, 3, 4],
                [-3, -4, 0, 1, 2, 3, 4],
                [1, 2, 3, -3, -4, 0, 4],
                [-1, -2, -3, 0, 1, 2, 30, 1, 2, -4, -5, 3],
                [-10, -10, 1, 3, 2]]:
            print("highest product of %s is %s" % (t, highest_product0(t)))
            self.assertEqual(highest_productordern(t), highest_product0(t))
            self.assertEqual(highest_product0(t), highest_product1(t))

if __name__ == "__main__":
    # # unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestHighestProduct)
    unittest.TextTestRunner(verbosity=2).run(suite)
