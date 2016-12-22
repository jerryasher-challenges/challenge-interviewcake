#!python

from __future__ import print_function
import unittest

######################################################################
# this problem is from
# https://www.interviewcake.com/question/python/reverse-words
#

# You're working on a secret team solving coded transmissions.

# Your team is scrambling to decipher a recent message, worried it's a
# plot to break into a major European National Cake Vault. The message
# has been mostly deciphered, but all the words are backwards! Your
# colleagues have handed off the last step to you.

# Write a function reverse_words() that takes a string message and
# reverses the order of the words in-place

# For example:

# message = 'find you will pain only go you recordings security the into if'
# reverse_words(message)
# returns: 'if into the security recordings you go only pain will you find'

# When writing your function, assume the message contains only letters
# and spaces, and all words are separated by one space.

#
######################################################################

# Now my turn


def reverse_wordssimple(message):
    """reverse the message but not 'in place'"""

    # split the message by spaces
    msg = message.split(" ")

    return " ".join(msg[::-1])  # new trick I learned to reverse a list


# sigh this is a class gotcha question
# if you see the trick you get it, if you don't you never will
def reverse_words(message):
    """reverse the message 'in place' in a mutable byte array"""

    b = bytearray(message)

    # reverse the entire bytearray in place
    reverse_bytes(b, 0, len(b))

    # now walk through the byte array finding words and the reverse
    # each word in place

    start = 0
    space = b.find(" ")
    while space != -1:
        reverse_bytes(b, start, space - start)

        start = space + 1
        space = b.find(" ", start)
    else:
        # reverse the unreversed remainder
        reverse_bytes(b, start, len(b) - start)

    return str(b)


def reverse_bytes(b, start, length):
    """reverses the bytes in array b, starting at start, for length bytes"""
    for i in range(length / 2):
        begin = start + i
        finish = start + (length - 1) - i
        (b[begin], b[finish]) = (b[finish], b[begin])
    return None
# Now Test


class TestReverseWords(unittest.TestCase):

    def test_reversewords(self):
        """test word reversal"""

        for test in ["",
                     "a",
                     "abc def",
                     "abc def ",
                     "the quick brown fox",
                     'find you will pain only go you recordings security the into if']:

            soln = reverse_wordssimple(test)
            self.assertEqual(soln, reverse_words(test))


if __name__ == "__main__":
    # # unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestReverseWords)
    unittest.TextTestRunner(verbosity=2).run(suite)
