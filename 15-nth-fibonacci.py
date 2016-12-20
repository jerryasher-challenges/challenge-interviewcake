#!python

from __future__ import print_function
import unittest

######################################################################
# this problem is from
# https://www.interviewcake.com/question/python/nth-fibonacci
#

# Write a function fib() that a takes an integer n and returns the nth fibonacci number.
# Say our fibonacci series is 0-indexed and starts with 0. So:

# fib(0) # => 0
# fib(1) # => 1
# fib(2) # => 1
# fib(3) # => 2
# fib(4) # => 3
# ...


######################################################################

# Now my turn

# the classic fibonacci is:

def fibonacci(n):
    """return nth fibonacci"""
    if n <= 0:
        return 0
    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)

    # which fibonacci is o(2^n)

    # but the work can be reduced via memoization, so memoize
fibs = {0: 0, 1: 1}


def memo_fibonacci(n):
    """return nth fibonacci"""

    if n <= 0:
        return 0

    if n in fibs:
        return fibs[n]

    fibs[n] = memo_fibonacci(n - 1) + memo_fibonacci(n - 2)
    return fibs[n]

# With memoization, fib(n) should be o(n) in time

# but as interviewcake notes, it is also o(n) in space (the stack as
# well as the memo hash table

# instead of using recursion, count up, greedily


def iter_fibonacci(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1

    fibn2 = 0
    fibn1 = 1
    for i in range(2, n + 1):
        fib = fibn1 + fibn2
        fibn2 = fibn1
        fibn1 = fib

    return fib

    # Now let's test


class TestFibonacci(unittest.TestCase):

    def test_classic_fib(self):
        """test classic fibonacci"""
        solns = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,
                 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]

        n = 0
        for soln in solns:
            self.assertEqual(solns[n], fibonacci(n))
            n += 1

    def test_memoized_fib(self):
        """test memoized fibonacci"""
        solns = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,
                 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]

        n = 0
        for soln in solns:
            self.assertEqual(solns[n], memo_fibonacci(n))
            n += 1

    def test_iterative_fib(self):
        """test iterative fibonacci"""
        solns = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,
                 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]

        n = 0
        for soln in solns:
            self.assertEqual(solns[n], iter_fibonacci(n))
            n += 1

if __name__ == "__main__":
    # unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFibonacci)
    unittest.TextTestRunner(verbosity=2).run(suite)
