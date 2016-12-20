#!python

from __future__ import print_function
import unittest

######################################################################
# this problem is from
# https://www.interviewcake.com/question/python/cake-thief
#
#
# You are a renowned thief who has recently switched from stealing
# precious metals to stealing cakes because of the insane profit
# margins. You end up hitting the jackpot, breaking into the
# largest privately owned stock of cakes -- the vault of the Queen of
# England.
#
# While Queen Elizabeth has a limited number of types of cake, she has
# an unlimited supply of each type.
#
# Each type of cake has a weight and a value, stored in a tuple with two
# indices:
#
# 0. An integer representing the weight of the cake in kilograms
# 1. An integer representing the monetary value of the cake in British pounds
#
# For example:
#
# # weighs 7 kilograms and has a value of 160 pounds
# (7, 160)
#
# # weighs 3 kilograms and has a value of 90 pounds
# (3, 90)
#
# You brought a duffel bag that can hold limited weight, and you want to
# make off with the most valuable haul possible.
#
# Write a function max_duffel_bag_value() that takes a list of cake type
# tuples and a weight capacity, and returns the maximum monetary value
# the duffel bag can hold.
#
# For example:
#
# cake_tuples = [(7, 160), (3, 90), (2, 15)]
# capacity    = 20
#
# max_duffel_bag_value(cake_tuples, capacity)
# # returns 555 (6 of the middle type of cake and 1 of the last type of cake)
#
# Weights and values may be any non-negative integer. Yes, it is weird
# to think about cakes that weigh nothing or duffel bags that cannot
# hold anything. But we are not just super mastermind criminals -- we are
# also meticulous about keeping our algorithms flexible and
# comprehensive.
#
######################################################################

# Now my turn
import sys


# first try, define a "density" function of $cake / $pounds of cake
# and try to fill the duffel based on these cake densities

# this is the first strategy, and it's fast and close but suboptimal

inf = float('inf')


def dollar_density(cake):
    """density is value / capacity. If capacity is zero, density is inf"""
    weight, value = cake
    if value == 0:
        return 0
    elif weight == 0:
        return inf
    else:
        return cake[1] / float(cake[0])


def cake_compare(cake0, cake1):
    """compares two cakes by bucks per size"""
    density0 = dollar_density(cake0)
    density1 = dollar_density(cake1)
    if density0 < density1:
        return -1
    elif density0 == density1:
        return 0
    else:
        return 1


def max_duffel_bag_value_density(cake_tuples, capacity):
    # sort the bag according to $ density
    # then add cakes to the duffel bag in order of decreasing "cake
    # dollar/capacity density"
    # interviewcake provides an example where this strategy fails
    # test_0oddsize shows this strategy fails because smaller cakes
    # might better fill the duffel bag with a higher value of cakes
    cake_inventory = sorted(cake_tuples, cake_compare, reverse=True)
    print(cake_inventory)

    total_value = 0
    remaining_space = capacity
    for cake in cake_inventory:
        weight, value = cake
        density = dollar_density(cake)
        if density == inf:
            return inf
        elif density > 0:
            ncake = remaining_space / weight
            if ncake > 0:
                print("%s %s %s" % (ncake, weight, value))
                remaining_space -= ncake * weight
                total_value += ncake * value
    print("%s %s" % (total_value, remaining_space))
    return total_value

# so let's try this again

# interviewcake suggests trying a greedy algorithm and building up
# this is reasonable, but a bit contradictory as interviewcake originally
# suggested that:

# The brute force approach is to try every combination of cakes, but
# that would take a really long time -- you'd surely be captured

# using a greedy algorithm here is not the brutest brute force, but
# it's fairly brute force as it does loop over various combinations
# keeping track of maxium values

# oh well, let's try a greedy approach


def max_duffel_bag_value_greedy(cake_tuples, capacity):

    for weight, value in cake_tuples:
        if weight == 0 and value > 0:
            return float('inf')

    capacity_to_value_map = [0] * (capacity + 1)
    print("\ncake_tuples %s, capacity %s" % (cake_tuples, capacity))

    for cap in range(0, capacity + 1):
        # print("  %s" % cap)
        possible_values = [0]
        for weight, value in cake_tuples:
            if weight <= cap:
                prev_cap = cap - weight
                prev_val = capacity_to_value_map[prev_cap]
                new_val = prev_val + value
                # print("    w %s v %s pc %s pv %s nv %s" %
                #       (weight, value, prev_cap, prev_val, new_val))
                possible_values.append(new_val)

        # print("  poss values %s" % possible_values)
        max_value = max(possible_values)
        if max_value == 0:
            if cap > 0:
                max_value = capacity_to_value_map[cap - 1]

        capacity_to_value_map[cap] = max_value

        # print("  capacity_to_value_map[%s] is %s" %
        #       (cap, capacity_to_value_map[cap]))

    print(capacity_to_value_map[capacity])
    return capacity_to_value_map[capacity]

# hey it works!

# and on further elucidation from interviewcake is
# dynamic
# bottom up
# solution to the unbounded knapsack problem

    # Now let's test


class TestDuffelPacker(unittest.TestCase):

    # # test "naive", "obvious", density packing

    # def test_00dollar_density_weightless_but_worthless(self):
    #     self.assertEqual(dollar_density([0, 0]), 0)

    # def test_00dollar_density_weightless(self):
    #     self.assertEqual(dollar_density([0, 1]), inf)

    # def test_01dollar_density_1typical(self):
    #     self.assertEqual(dollar_density([5, 10]), 2.0)

    # def test_01dollar_density_2typical(self):
    #     self.assertEqual(dollar_density([10, 5]), 0.5)

    # def test_0given_example0(self):
    #     cake_tuples = [(7, 160), (3, 90), (2, 15)]
    #     capacity = 20
    #     self.assertEqual(
    #         555, max_duffel_bag_value_density(cake_tuples, capacity))

    # def test_0given_example1(self):
    #     cake_tuples = [(1, 30), (50, 200)]
    #     capacity = 100
    #     self.assertEqual(
    #         3000, max_duffel_bag_value_density(cake_tuples, capacity))

    # def test_0given_example2(self):
    #     cake_tuples = [(3, 40), (5, 70)]
    #     capacity = 8
    #     self.assertEqual(
    #         110, max_duffel_bag_value_density(cake_tuples, capacity))

    # def test_0oddsize(self):
    #     """this test shows where the naive, obvious solution fails"""
    #     cake_tuples = [(3, 40), (5, 70)]
    #     capacity = 9
    #     self.assertNotEqual(
    #         120, max_duffel_bag_value_density(cake_tuples, capacity))

    # test greedy

    def test_1_simple_example0(self):
        cake_tuples = [(1, 2), (3, 4)]
        capacity = 7
        self.assertEqual(
            14, max_duffel_bag_value_greedy(cake_tuples, capacity))

    def test_1given_example0(self):
        cake_tuples = [(7, 160), (3, 90), (2, 15)]
        capacity = 20
        self.assertEqual(
            555, max_duffel_bag_value_greedy(cake_tuples, capacity))

    def test_1given_example1(self):
        cake_tuples = [(1, 30), (50, 200)]
        capacity = 100
        self.assertEqual(
            3000, max_duffel_bag_value_greedy(cake_tuples, capacity))

    def test_1given_example2(self):
        cake_tuples = [(3, 40), (5, 70)]
        capacity = 8
        self.assertEqual(
            110, max_duffel_bag_value_greedy(cake_tuples, capacity))

    def test_1oddsize(self):
        cake_tuples = [(3, 40), (5, 70)]
        capacity = 9
        self.assertEqual(
            120, max_duffel_bag_value_greedy(cake_tuples, capacity))

    def test_1zerosizedduffed(self):
        """test a duffel that can hold nothing can hold nothing"""
        cake_tuples = [[0, 0], (1, 2), (3, 4)]
        capacity = 0
        self.assertEqual(
            0, max_duffel_bag_value_greedy(cake_tuples, capacity))

    def test_1valuelessweightlesscake(self):
        """test a valueless weightless cake is ignored"""
        cake_tuples = [[0, 0], (1, 2), (3, 4)]
        capacity = 7
        self.assertEqual(
            14, max_duffel_bag_value_greedy(cake_tuples, capacity))

    def test_2valueableweightlesscake(self):
        """test a valuable weightless cake returns inf"""
        cake_tuples = [[0, 5], (1, 2), (3, 4)]
        capacity = 7
        self.assertEqual(
            float('inf'), max_duffel_bag_value_greedy(cake_tuples, capacity))


if __name__ == "__main__":
    # unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestDuffelPacker)
    unittest.TextTestRunner(verbosity=2).run(suite)
