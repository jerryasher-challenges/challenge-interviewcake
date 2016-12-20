#!python

from __future__ import print_function
import unittest

######################################################################
# this problem is from
# https://www.interviewcake.com/question/python/inflight-entertainment
#
#
# You've built an in-flight entertainment system with on-demand movie
# streaming.
#
# Users on longer flights like to start a second movie right when their
# first one ends, but they complain that the plane usually lands before
# they can see the ending. So you're building a feature for choosing two
# movies whose total runtimes will equal the exact flight length.
#
# Write a function that takes an integer flight_length (in minutes) and
# a list of integers movie_lengths (in minutes) and returns a boolean
# indicating whether there are two numbers in movie_lengths whose sum
# equals flight_length.
#
# When building your function:
#
# + Assume your users will watch exactly two movies
# + Don't make your users watch the same movie twice
# + Optimize for runtime over memory
######################################################################

# Now my turn


def matching_movies(flight_length, movie_lengths):
    """return true if two movies sum up to a flight length duration"""

    lengths = {}  # a 1:many map of lengths to their movies
    for length in movie_lengths:
        # put each length of a movie into a hash table as we scan over
        # all the movies (by length) see if the complement movie is
        # already in lengths.  by the time we reach the end of the
        # movies by lengths every movie has been checked for its
        # complement and since we check before insertion, no one has
        # to watch the same movie twice.

        complement = flight_length - length
        if complement in lengths:
            return True

        lengths[length] = True

    return False


# Now let's test


class TestMatchingMovies(unittest.TestCase):

    def setUp(self):
        self.movies = range(100, 120)

    def test_1no_matches(self):
        self.assertFalse(matching_movies(256, self.movies))

    def test_2one_match(self):
        self.movies[5] = 256 - self.movies[10]
        self.assertTrue(matching_movies(256, self.movies))

    def test_2theother_match(self):
        self.movies[10] = 256 - self.movies[5]
        self.assertTrue(matching_movies(256, self.movies))
        # self.assertRaises(EarlyMatch, matching_movies, 256, self.movies)

    def test_one_match_but_same_movie(self):
        self.movies[5] = 128
        self.assertFalse(matching_movies(256, self.movies))

    def test_two_matches(self):
        self.movies[5] = 128
        self.movies[15] = 128
        self.assertTrue(matching_movies(256, self.movies))

if __name__ == "__main__":
    # unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMatchingMovies)
    unittest.TextTestRunner(verbosity=2).run(suite)
