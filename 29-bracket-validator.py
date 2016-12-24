#!python

from __future__ import print_function
import unittest

######################################################################
# this problem is from
# https://www.interviewcake.com/question/python/bracket-validator
#

# You're working with an intern that keeps coming to you with JavaScript
# code that won't run because the braces, brackets, and parentheses are
# off. To save you both some time, you decide to write a
# braces/brackets/parentheses validator.

# Let's say:

# + '(', '{', '[' are called "openers."
# + ')', '}', ']' are called "closers."

# Write an efficient function that tells us whether or not an input
# string's openers and closers are properly nested.

# Examples:

# + "{ [ ] ( ) }" should return True
# + "{ [ ( ] ) }" should return False
# + "{ [ }" should return False

#
######################################################################

# Now my turn

# So this is very similar to 28-matching-parens.py, but instead of just
# counting the parens, this time whenever we find an opener, we'll push
# it onto a stack and when we find a closer, we'll pop the stack and see
# if what was popped was matches the closer we just found.


def has_valid_brackets(string):
    """returns True if a strings brackets are properly nested"""

    brackets = []
    bracket_map = {
        '(': 0,
        '{': 0,
        '[': 0,
        ')': '(',
        '}': '{',
        ']': '[',
    }
    for ch in string:
        if ch in bracket_map:
            brack = bracket_map[ch]
            if brack == 0:
                brackets.append(ch)
            else:
                if len(brackets) <= 0:
                    return False
                top = brackets.pop()
                if brack != top:
                    return False
    if len(brackets) == 0:
        return True

    return False

    # And now the tests


class TestValidBrackets(unittest.TestCase):

    def test_0givenexample(self):
        """test the given example"""

        tests = [
            [True, "{ [ ] ( ) }"],
            [False, "{ [ ( ] ) }"],
            [False, "{ [ }"]]

        for valid, string in tests:
            self.assertEqual(valid, has_valid_brackets(string),
                             "%s should be %s" % (string, valid))

    def test_1myfairlady(self):
        """the rain (in spain) (falls ..."""
        s = "the rain (in spain) (falls (ma(i)nly) ((i))n the plain!)"
        self.assertEqual(True, has_valid_brackets(s))

    def test_2simpletons(self):
        """some more simple tests"""
        tests = [
            [True,
             """{
                 "id": 1,
                 "name": "A green door",
                 "price": 12.50,
                 "tags": ["home", "green"]
             }"""],
            [True,
             """{
                 "$schema": "http://json-schema.org/draft-04/schema#",
                 "properties": {
                     "id": {
                         "description": "The unique identifier for a product",
                         "type": "integer"
                     }
                 },
                 "required": ["id"]
             }"""],
            [False,
             """[("sensor","string", {"Sensor name"}), 
                 ("timestamp","string", } "Time"),
                 ("value","string", "Sensor value")]"""
             ]]

        for valid, string in tests:
            self.assertEqual(valid, has_valid_brackets(string),
                             "%s should be %s" % (string, valid))


if __name__ == "__main__":
    # unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestValidBrackets)
    unittest.TextTestRunner(verbosity=2).run(suite)
