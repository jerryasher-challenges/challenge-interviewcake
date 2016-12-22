#!python

from __future__ import print_function
import unittest

######################################################################
# this problem is from
# https://www.interviewcake.com/question/python/product-of-other-numbers

# You have a list of integers, and for each index you want to find the
# product of every integer except the integer at that index.

# Write a function get_products_of_all_ints_except_at_index() that takes
# a list of integers and returns a list of the products.

# For example, given:
#   [1, 7, 3, 4]
# your function would return:
#   [84, 12, 28, 21]
# by calculating:
#   [7*3*4, 1*3*4, 1*7*4, 1*7*3]

# Do not use division in your solution.

#
######################################################################

# Now my turn


# obvious solution THAT USES DIVISION
def get_products_of_all_ints_except_at_indexDIVISION(l):
    """uses n mults and n divides"""
    if len(l) == 0:
        return []

    if len(l) == 1:
        return [1]

    prod = 1
    for n in l:
        prod *= n

    prods = []
    for i in range(len(l)):
        if l[i] != 0:
            prods.append(int(prod / l[i]))
        else:
            prods.append(int(prod))

    return prods

# okay, so no division...


def get_products_of_all_ints_except_at_indexn2(l):
    """uses n squared mults, no divides, ie brute force"""
    if len(l) == 0:
        return []

    if len(l) == 1:
        return [1]

    prods = [1] * len(l)
    n = len(prods)

    for i in range(n):
        for j in range(i):
            prods[j] = prods[j] * l[i]
        for j in range(i + 1, n):
            prods[j] = prods[j] * l[i]

    return prods

# interview cake suggests "greedy" and shows a pattern of accumulating
# products from the left and the right and asks us to generalize...

# so the pattern and generalization seems to suggests scanning left
# across the list of factors accumulating the product as we go and
# progressively assigning product i as product list element i + 1

# then scanning right across the list of factors accumulating a new
# product from the right then multiplying that new product by the
# existing prior product of products list element.

# in this way, each products list element i becomes the prod(all
# factors(j) except for i)


def get_products_of_all_ints_except_at_index(l):
    """greedy: n space approx 4n mults"""
    if len(l) < 1:
        return []

    prods = [1] * len(l)
    n = len(prods)

    left = 1
    for i in range(0, n):
        prods[i] = prods[i] * left
        left = left * l[i]

    # fun with zero based left marching range indices!
    right = 1
    for i in range(n - 1, -1, -1):
        prods[i] = prods[i] * right
        right = right * l[i]

    return prods

# all in all pretty clever
# I would bomb this terribly if asked for it on the fly in an
# interview.  but yeah, if you ask me, this question is inappropriate
# for an interview, unless the goal is to make people sweat OR to
# filter for people who have seen this problem before


class TestGetProductsExcept(unittest.TestCase):

    def test_givenexample(self):
        """test the given example"""
        example = [1, 7, 3, 4]
        soln = [84, 12, 28, 21]
        self.assertEqual(
            soln,
            get_products_of_all_ints_except_at_indexDIVISION(example))

        self.assertEqual(
            soln,
            get_products_of_all_ints_except_at_indexn2(example))

        self.assertEqual(
            soln,
            get_products_of_all_ints_except_at_index(example))

    def test_0sandEmpties(self):
        """test edge cases"""
        self.assertEqual(
            [], get_products_of_all_ints_except_at_indexDIVISION([]))
        self.assertEqual(
            [1], get_products_of_all_ints_except_at_indexDIVISION([5]))
        self.assertEqual(
            [1], get_products_of_all_ints_except_at_indexDIVISION([0]))
        self.assertEqual(
            [0, 0], get_products_of_all_ints_except_at_indexDIVISION([0, 0]))
        self.assertEqual(
            [0, 0, 0],
            get_products_of_all_ints_except_at_indexDIVISION([0, 0, 0]))

        self.assertEqual(
            [], get_products_of_all_ints_except_at_index([]))
        self.assertEqual(
            [1], get_products_of_all_ints_except_at_index([5]))
        self.assertEqual(
            [1], get_products_of_all_ints_except_at_index([0]))
        self.assertEqual(
            [0, 0], get_products_of_all_ints_except_at_index([0, 0]))
        self.assertEqual(
            [0, 0, 0], get_products_of_all_ints_except_at_index([0, 0, 0]))


if __name__ == "__main__":
    # unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestGetProductsExcept)
    unittest.TextTestRunner(verbosity=2).run(suite)
