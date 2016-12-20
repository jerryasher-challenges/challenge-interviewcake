#!python

from __future__ import print_function
import unittest

######################################################################
# this problem is from
# https://www.interviewcake.com/question/python/find-rotation-point
#

# I want to learn some big words so people think I'm smart.

# I opened up a dictionary to a page in the middle and started flipping
# through, looking for words I didn't know. I put each word I didn't know
# at increasing indices in a huge list I created in memory. When I reached
# the end of the dictionary, I started from the beginning and did the same
# thing until I reached the page I started at.

# Now I have a list of words that are mostly alphabetical, except they
# start somewhere in the middle of the alphabet, reach the end, and then
# start from the beginning of the alphabet. In other words, this is an
# alphabetically ordered list that has been "rotated." For example:

words = [
    'pto',
    'ret',
    'sup',
    'und',
    'xen',
    'asy',  # <-- rotates here!
    'bab',
    'ban',
    'eng',
    'kar',
    'oth',
]

# Write a function for finding the index of the "rotation point,"
# which is where I started working from the beginning of the
# dictionary. This list is huge (there are lots of words I don't know) so
# we want to be efficient here.

######################################################################

# Now my turn


def find_rotation_point(words):
    """return the index of the rotation point of a sorted word list"""

    # basically a modified binary search
    index = 0
    n = len(words)
    if n > 1:
        left = 0
        right = n - 1

        while (right - left) > 1:
            if words[left] > words[right]:
                # the pivot is somewhere within this interval
                # but where?
                # split the interval in half
                # check each half for the pivot
                # use the half that contains the pivot
                nexttry = int((left + right) / 2.0 + 0.5)
                if words[nexttry] > words[right]:
                    left = nexttry
                else:
                    right = nexttry
            else:
                # Boy: Do not try and find the pivot. That's
                #      impossible. Instead only try to realize the truth.
                # Neo: What truth?
                # Boy: There is no pivot.
                return left

        if words[left] <= words[right]:
            index = left
        else:
            index = right

    return index

# Now let's test


class TestFindRotationPoint(unittest.TestCase):

    @staticmethod
    def right_rotate(l, n):
        """a helper function: rotate right a list l right by n positions, return a new list"""
        if n < 0:
            raise ValueError(
                "Right rotations only please, negative drehungen sind verboten"
                ", move along, move along.")
        n = n % len(l)
        if n == 0 or len(l) == 0:
            return l[:]
        return l[-n:] + l[:len(l) - n]

    def test_00rotate(self):
        """test our helper list rotation function"""
        self.assertRaises(ValueError, self.right_rotate, [1, 2, 3, 4], -1)
        tests = [
            [0, [1, 2, 3, 4]],
            [1, [4, 1, 2, 3]],
            [2, [3, 4, 1, 2]],
            [3, [2, 3, 4, 1]],
            [4, [1, 2, 3, 4]],
            [7, [2, 3, 4, 1]],
        ]
        for (positions, soln) in tests:
            case = [1, 2, 3, 4]
            result = self.right_rotate(case, positions)
            msg = "right_rotate({}, {}) should be {} was {}".format(
                case, positions, soln, result)
            self.assertEquals(soln, result, msg)

    def test_0words(self):
        """test the case in the problem statement"""
        n = find_rotation_point(words)
        self.assertEqual(5, n)

    def test_1words(self):
        """test the words in the problem statement at all rotations"""
        words.sort()
        for i in range(0, len(words)):
            wordlist = self.right_rotate(words, i)
            n = find_rotation_point(wordlist)
            msg = "rotation point {} should have been {} [{}]".format(
                n, i, wordlist)
            self.assertEquals(n, i, msg)

    def test_ultrawords(self):
        """test all sizes of substrings of the words in the problem statement at all rotations"""
        words.sort()
        for j in range(0, len(words)):
            wordlist = words[0:j]
            for i in range(0, len(wordlist)):
                rotated_list = self.right_rotate(wordlist, i)
                n = find_rotation_point(rotated_list)
                msg = "[{}, {}] rp {} should've been {} [{}]".format(
                    j, i, n, i, rotated_list)
                self.assertEquals(n, i, msg)

if __name__ == "__main__":
    # unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFindRotationPoint)
    unittest.TextTestRunner(verbosity=2).run(suite)
