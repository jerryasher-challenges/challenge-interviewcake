#!python

######################################################################
# this problem is from
# https://www.interviewcake.com/question/python/compress-url-list?
#
# I'm making a search engine called MillionGazillion
#
# I wrote a crawler that visits web pages, stores a few keywords in a
# database, and follows links to other web pages. I noticed that my
# crawler was wasting a lot of time visiting the same pages over and
# over, so I made a set, visited, where I'm storing URLs I've already
# visited. Now the crawler only visits a URL if it hasn't already been
# visited.
#
# Thing is, the crawler is running on my old desktop computer in my
# parents' basement (where I totally don't live anymore), and it keeps
# running out of memory because visited is getting so huge.
#
# How can I trim down the amount of space taken up by visited?
######################################################################

# So my naive quick and dirty take would be to hash it until it
# becomes a problem then rethink. (Don't optimize too soon)

# Then maybe compress the url ala bitly, using "readable" base 36 or base
# 62 or unreadable base 256 (because this is for an internal db,
# readability could be tossed) then hash it.

# Maybe if it were a real problem try other known compression
# algorithms, or heavens google for clues or speak to folks who have
# experience.

# Well, skipping ahead, interviewcake suggests storing this in a
# 'trie', a data structure I know nothing of other than its name.

# But I can google, and sometimes even understand what I google.

# At any rate, interviewcake provides a sample implementation of a
# trie using a large organized cluster of organized clusters of
# dictionaries.

######################################################################
# Let's make visited a nested dictionary where each map has keys of just
# one character. So we would store 'google.com' as
# visited['g']['o']['o']['g']['l']['e']['.']['c']['o']['m']['*'] = True.
#
# The '*' at the end means 'this is the end of an entry'. Otherwise we
# wouldn't know what parts of visited are real URLs and which parts are
# just prefixes. In the example above, 'google.co' is a prefix that we
# might think is a visited URL if we didn't have some way to mark 'this
# is the end of an entry.'
######################################################################

# interviewake suggests this is not the be all and end all of trie
# implementations, but it's what it's going with.

# So I try it, and sure, it works pretty well, but wow, nested
# directories seems to be a pretty convoluted way to store these urls
# and I really have to wonder, how does that compare to my naive hash
# table implementation?

# And the answer seems to be, not well. MORE on that below, but the
# take away is that while a trie structure may have many wonderful
# uses, a trie structure made of hash tables is about 10x worse in
# terms of space that just using a single hash table at least for
# Python 2.7

# what I took from this question:

# + trie structure
# + how to measure structure size in python
# + a bit more sophistication using python unittest
# + how to calculate the variance and std deviation of a stream of input


# Conclusion: this question helps demonstrate the adage, don't
# optimize prematurely, or in its strong form, "Premature optimization
# is the root of all evil." -- Donald Knith. In this question, it's
# pretty clear interviewcake optimized too soon.

# so here we go

from __future__ import print_function
from sys import getsizeof, stderr
from itertools import chain
from collections import deque
import unittest
import random
import string
import math

try:
    from reprlib import repr
except ImportError:
    pass


# 1. Interview Cake's Trie implementation:

class Trie:

    def __init__(self):
        self.root_node = {}

    def check_present_and_add(self, word):

        current_node = self.root_node
        is_new_word = False

        # Work downwards through the trie, adding nodes
        # as needed, and keeping track of whether we add
        # any nodes.
        for char in word:
            if char not in current_node:
                is_new_word = True
                current_node[char] = {}
            current_node = current_node[char]

        # Explicitly mark the end of a word.
        # Otherwise, we might say a word is
        # present if it is a prefix of a different,
        # longer word that was added earlier.
        if "End Of Word" not in current_node:
            is_new_word = True
            current_node["End Of Word"] = {}

        return is_new_word

# 15 lines. As usual I find Interviewcake's code elegant and simple,
# and find I am yet again jealous of their coding talents.

# Well, let's play with it, and test it.

# First let's create a class to generate words. In the interviewcake
# example, these words are urls, in which

# 1. urls can form families, as in google.com, www.google.com,
#    www.google.com/about, etc.

# 2. urls might be up to 2000 characters longer

# to simulate urls, let's generate words of a random length.  To
# simulate url families, let's create one long random string, and then
# allocate all the words out of that long random string. Url families
# are when these strings start with the same index.


class WordGenerator:

    def __init__(self, length=100000):
        self.charlen = length
        self.chars = string.ascii_lowercase + string.ascii_uppercase
        self.charlist = \
            ''.join(random.choice(self.chars) for _ in range(length))
        print("init: %s chars" % length)

    def gen(self, max_length=None):

        length = random.randrange(0, max_length)
        start = random.randint(0, self.charlen)
        end = start + length
        if end > self.charlen:
            end = self.charlen
        word = self.charlist[start:end]
        return word

# Now let's test
# Let's generate a large number of words
# and store each word in a trie of hash tables and just one hash table
# let's measure the storage required for the trie and for the hash table
# and let's measure the mean and std. deviation of the words.

# to measure the memory, we'll use a "recipe" from ActiveState
# from https://code.activestate.com/recipes/577504/
# recursive version of getsizeof
#


class TestTrieVsHash(unittest.TestCase):

    def a_test(self, number_of_words=1000, max_word_size=20, text_size=10000):

        # Our Trie of hash tables
        self.t = Trie()

        # Our naive hash table
        self.h = {}

        sizes_t = []
        sizes_h = []

        sizes_t.append(total_size(self.t.root_node))
        sizes_h.append(total_size(self.h))

        self.words = WordGenerator(length=text_size)

        bucket_size = int(math.ceil(number_of_words / 10.0))

        # https://en.wikipedia.org/wiki/Algorithms_for_calculating_variance#Online_algorithm
        n = 0
        mean = 0.0
        M2 = 0.0

        for i in range(number_of_words):

            # get a word
            word = self.words.gen(max_length=max_word_size)

            # store a word
            self.t.check_present_and_add(word)
            self.h[word] = True

            # keep a running sum of the variance of word length
            n += 1
            x = len(word)
            delta = x - mean
            mean += delta / n
            delta2 = x - mean
            M2 += delta * delta2

            # print("n %s  len %s  delta %s  mean %s delta2 %s  M2 %s" %
            #       (n, x, delta, mean, delta2, M2))

            if i % bucket_size == 0:
                sizes_t.append(total_size(self.t.root_node))
                sizes_h.append(total_size(self.h))

        # all done, print out a csv of the results
        print("\nwords, trie bytes, hash bytes")
        for i in range(len(sizes_t)):
            # print("%s words, trie %s bytes, hash %s" %
            #       (i * bucket_size, sizes_t[i], sizes_h[i]))
            print("%s, %s, %s" %
                  (i * bucket_size, sizes_t[i], sizes_h[i]))

        if n < 2:
            stddev = float('nan')
        else:
            variance = M2 / (n - 1)
            stddev = math.sqrt(variance)

        print("\n%s words, mean length = %s, std. deviation = %s" %
              (n, mean, stddev))

        print("")

    def test_1small_words(self):
        self.a_test(max_word_size=20)

    def test_2big_words(self):
        self.a_test(max_word_size=200)

    def test_3small_corpus(self):
        self.a_test(text_size=1000, number_of_words=10000, max_word_size=20)

    def test_4lots_of_words(self):
        self.a_test(number_of_words=100000)

    # def test_0statistics(self):
    #     self.a_test(text_size=100, number_of_words=2, max_word_size=20)
    #     self.a_test(text_size=100, number_of_words=5, max_word_size=20)
    #     self.a_test(text_size=100, number_of_words=10, max_word_size=20)
    #     self.a_test(text_size=100, number_of_words=100, max_word_size=20)
    #     self.a_test(text_size=1000, number_of_words=1000, max_word_size=20)
    #     self.a_test(text_size=1000, number_of_words=1000, max_word_size=20)
    #     self.a_test(text_size=1000, number_of_words=10000, max_word_size=20)

# So each run of this script will produce different results, but one
# such run looks like this:

# $ py -2 11-compress-url-list.py
#
# words, trie bytes, hash bytes
# 0, 140, 140
# 1000, 31416, 387
# 2000, 18017816, 174823
# 3000, 35784028, 397537
# 4000, 53562164, 548605
# 5000, 71300648, 698388
# 6000, 88432436, 845175
# 7000, 105592728, 1289495
# 8000, 122474404, 1437768
# 9000, 139042184, 1584284
# 10000, 156160852, 1733523
#
# 10000 words, mean length = 127.7944, std. deviation = 73.2895904276
# .
# --------------------------------------------------------------------
# Ran 1 test in 42.856s


# from https://code.activestate.com/recipes/577504/
# recursive version of getsizeof

def total_size(o, handlers={}, verbose=False):
    """ Returns the approximate memory footprint an object and all of its contents.

    Automatically finds the contents of the following builtin containers and
    their subclasses:  tuple, list, deque, dict, set and frozenset.
    To search other containers, add handlers to iterate over their contents:

        handlers = {SomeContainerClass: iter,
                    OtherContainerClass: OtherContainerClass.get_elements}

    """
    dict_handler = lambda d: chain.from_iterable(d.items())
    all_handlers = {tuple: iter,
                    list: iter,
                    deque: iter,
                    dict: dict_handler,
                    set: iter,
                    frozenset: iter,
                    }
    all_handlers.update(handlers)  # user handlers take precedence
    seen = set()                  # track object id's already seen
    # estimate sizeof object without __sizeof__
    default_size = getsizeof(0)

    def sizeof(o):
        if id(o) in seen:       # do not double count the same object
            return 0
        seen.add(id(o))
        s = getsizeof(o, default_size)

        if verbose:
            print(s, type(o), repr(o), file=stderr)

        for typ, handler in all_handlers.items():
            if isinstance(o, typ):
                s += sum(map(sizeof, handler(o)))
                break
        return s

    return sizeof(o)


if __name__ == "__main__":
    # unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTrieVsHash)
    unittest.TextTestRunner(verbosity=2).run(suite)
