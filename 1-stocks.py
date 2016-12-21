#!python

from __future__ import print_function
import unittest

######################################################################
# this problem is from
# https://www.interviewcake.com/question/python/stock-price

# Writing programming interview questions hasn't made me rich. Maybe
# trading Apple stocks will.

# Suppose we could access yesterday's stock prices as a list, where:

# + The indices are the time in minutes past trade opening time, which
#   was 9:30am local time.
# + The values are the price in dollars of Apple stock at that time.

# So if the stock cost $500 at 10:30am, stock_prices_yesterday[60] =
# 500.

# Write an efficient function that takes stock_prices_yesterday and
# returns the best profit I could have made from 1 purchase and 1 sale
# of 1 Apple stock yesterday.

# For example:

# stock_prices_yesterday = [10, 7, 5, 8, 11, 9]

# get_max_profit(stock_prices_yesterday)
# returns 6 (buying for $5 and selling for $11)

# No "shorting" - you must buy before you sell. You may not buy and sell
# in the same time step(at least 1 minute must pass).

######################################################################

# this solution is pretty much what is on the site as I just followed
# it along as a "free question" to help determine if these examples
# were interesting.


def get_max_profit(stock_prices_yesterday):

    if len(stock_prices_yesterday) < 2:
        raise IndexError('Getting a profit requires at least 2 prices')

    # min_price = stock_prices_yesterday[0]
    # max_profit = 0

    min_price = stock_prices_yesterday[0]
    max_profit = stock_prices_yesterday[1] - stock_prices_yesterday[0]

    print("")
    for current_price in stock_prices_yesterday:

        # ensure min_price is the lowest price we've seen so far
        min_price = min(min_price, current_price)

        # see what our profit would be if we bought at the
        # min price and sold at the current price
        potential_profit = current_price - min_price

        # update max_profit if we can do better
        max_profit = max(max_profit, potential_profit)

        print("   cur_price %s min_price %s pot_profit %s max_profit %s" %
              (current_price, min_price, potential_profit, max_profit))

    return max_profit

# Now let's test


class TestStockPrice(unittest.TestCase):

    def test_given_obvious_edge_case(self):
        stock_prices_yesterday = [10, 10, 10, 10]
        max_profit = get_max_profit(stock_prices_yesterday)
        self.assertEqual(0, max_profit)

    def test_given_example(self):
        """test the example given at interviewcake"""
        stock_prices_yesterday = [10, 7, 5, 8, 11, 9]
        max_profit = get_max_profit(stock_prices_yesterday)
        self.assertEqual(6, max_profit)

    def test_given_example(self):
        """test a day where there are no good deals"""
        stock_prices_yesterday = [10, 7, 5, 4, 2, 0]
        max_profit = get_max_profit(stock_prices_yesterday)
        self.assertEqual(0, max_profit)


if __name__ == "__main__":
    # unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestStockPrice)
    unittest.TextTestRunner(verbosity=2).run(suite)
