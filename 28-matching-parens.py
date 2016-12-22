#!python

from __future__ import print_function
import unittest

######################################################################
# this problem is from
# https://www.interviewcake.com/question/python/matching-parens
#

# I like parentheticals (a lot).  "Sometimes (when I nest them (my
# parentheticals) too much (like this (and this))) they get confusing."

# Write a function that, given a sentence like the one above, along with
# the position of an opening parenthesis, finds the corresponding
# closing parenthesis.

# Example: if the example string above is input with the number 10
# (position of the first parenthesis), the output should be 79 (position
# of the last parenthesis).

#
######################################################################

# Now my turn

# I literally do this in my head all the time, ...
# (because years of editing (loving) LISP!)


def find_close_paren(string, start):
    """find the closing paren, return None if not matched"""

    if string[start] != "(":
        raise Exception

    # keep a count of ( and )
    # incr each (
    # decr each )
    # stop when count is 0

    i = start
    end = len(string)
    count = 0
    while i < end:
        ch = string[i]
        if ch == "(":
            count += 1
        elif ch == ")":
            count -= 1
            if count == 0:
                return i
        i += 1
    return None

# And now the tests


class TestMatchingParens(unittest.TestCase):

    def test_0givenexample(self):
        """test the given example"""
        input = "Sometimes (when I nest them (my parentheticals) too " \
                "much (like this (and this))) they get confusing."

        self.assertEqual(79, find_close_paren(input, 10))

    def test_1myfairlady(self):
        """the rain (in spain) (falls ..."""

        s = "the rain (in spain) (falls (ma(i)nly) ((i))n the plain!)"

        parens = [[9, 18],
                  [20, 55],
                  [27, 36],
                  [30, 32]]

        for start, end in parens:
            self.assertEqual(end, find_close_paren(s, start))

    def test_2lispfib(self):
        """test a small lisp routine"""
        input = "(defun fib (n)  (cond ((<= n 1) 1) (t (+ (fib (- n 1)) (fib (- n 2))))))"
        self.assertEqual(71, find_close_paren(input, 0))
        self.assertEqual(13, find_close_paren(input, 11))
        self.assertEqual(70, find_close_paren(input, 16))


if __name__ == "__main__":
    # # unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMatchingParens)
    unittest.TextTestRunner(verbosity=2).run(suite)
