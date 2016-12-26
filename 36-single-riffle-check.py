#!python

from __future__ import print_function
import random
import unittest

######################################################################
# this problem is from
# https://www.interviewcake.com/question/python/single-rifle-check
#

# I figured out how to get rich: online poker.

# I suspect the online poker game I'm playing shuffles cards by doing
# a single "riffle."

# To prove this, let's write a function to tell us if a full deck of
# cards shuffled_deck is a single riffle of two other halves half1 and
# half2.

# We'll represent a stack of cards as a list of integers in the range
# 1..52 (since there are 52 distinct cards in a deck).

# Why do I care? A single riffle is not a completely random
# shuffle. If I'm right, I can make more informed bets and get rich
# and finally prove to my ex that I am not a "loser with an unhealthy
# cake obsession" (even though it's too late now because she let me go
# and she's never getting me back).

######################################################################

# now my turn

# first try:

# a singly riffled deck should have two sets of cards in it,
# for some c in a deck of n cards
# the first set of cards is 1..c
# the second set is c+1..n
# and in the deck the cards from each set are sequential, and interspersed.
# so scan the deck looking for sequential cards in either set
# if you find a non-sequential card, then the deck is not singly riffled.

random.seed()
ncards = 52


def is_first_riffle(deck):
    h1 = 0
    h2 = 0

    for card in deck:
        if card == h1 + 1:
            h1 = card
        else:
            if h2 == 0:
                h2 = card - 1

            if card == h2 + 1:
                h2 = card
            else:
                return False
    return True

# heh. first has little to do with the problem statement, which I now
# realize is about singly riffling a cut, shuffled deck.

# let's write a function to tell us if a full deck of cards
# shuffled_deck is a single riffle of two other halves half1 and
# half2.


# second try, recursive solution:
def is_single_riffle(half1, half2, shuffled_deck):
    """returns True if shuffled_deck may have come from half1 and half2"""
    # base case
    if len(shuffled_deck) == 0:
        return True

    # if the top of shuffled_deck is the same as the top of half1
    # (making sure first that we have a top card in half1)
    if len(half1) and half1[0] == shuffled_deck[0]:

        # take the top cards off half1 and shuffled_deck and recurse
        return is_single_riffle(half1[1:], half2, shuffled_deck[1:])

    # if the top of shuffled_deck is the same as the top of half2
    elif len(half2) and half2[0] == shuffled_deck[0]:

        # take the top cards off half2 and shuffled_deck and recurse
        return is_single_riffle(half1, half2[1:], shuffled_deck[1:])

    # top of shuffled_deck doesn't match top of half1 or half2
    # so we know it's not a single riffle
    else:
        return False

# third try (non-recursive):


def is_single_riffle2(half1, half2, shuffled_deck):
    h1 = 0
    h2 = 0
    for card in shuffled_deck:
        if h1 < len(half1) and card == half1[h1]:
            h1 += 1
            continue
        elif h2 < len(half2) and card == half2[h2]:
            h2 += 1
            continue
        return False
    return True


# helpers


def first_riffle(num_cards=ncards):
    """return a single riffled deck of cards"""
    split = random.randrange(2, ncards - 1)
    h1 = []
    for i in range(1, split):
        h1.append(i)

    h2 = []
    for i in range(split, ncards + 1):
        h2.append(i)

    return h1, h2, shuffle(h1, h2, 3)


def shuffle(h1, h2, maxcards=3):
    """shuffles two decks, with at most, maxcards in a row from a single deck"""
    deck = []
    maxcards += 1
    while((len(h1) > 0) or (len(h2) > 0)):

        h1cards = random.randrange(1, maxcards)
        h1cards = min(h1cards, len(h1))
        h1slice = h1[0:h1cards]
        h1 = h1[h1cards:]

        h2cards = random.randrange(1, maxcards)
        h2cards = min(h2cards, len(h2))
        h2slice = h2[0:h2cards]
        h2 = h2[h2cards:]

        deck.extend(h1slice)
        deck.extend(h2slice)

    return deck


# now test


class TestSingleRiffleCheck(unittest.TestCase):

    def test_1good_riffles(self):
        """test good riffles"""

        h1, h2, deck = first_riffle()
        print("")
        print("h1: %s" % h1)
        print("h2: %s" % h2)
        self.assertTrue(is_single_riffle(h1, h2, deck),
                        "\nh1 %s h2 %s\ndeck %s" % (h1, h2, deck))
        self.assertTrue(is_single_riffle2(h1, h2, deck),
                        "\nh1 %s h2 %s\ndeck %s" % (h1, h2, deck))

        deck = shuffle(h1, h2)
        print("deck: %s" % deck)
        self.assertTrue(is_single_riffle(h1, h2, deck),
                        "\nh1 %s h2 %s\ndeck %s" % (h1, h2, deck))
        self.assertTrue(is_single_riffle2(h1, h2, deck),
                        "\nh1 %s h2 %s\ndeck %s" % (h1, h2, deck))

    def test_2ngood_riffles(self):
        for i in range(100):
            h1, h2, deck = first_riffle()
            self.assertTrue(is_single_riffle(h1, h2, deck),
                            "\nh1 %s h2 %s\ndeck %s" % (h1, h2, deck))
            self.assertTrue(is_single_riffle2(h1, h2, deck),
                            "\nh1 %s h2 %s\ndeck %s" % (h1, h2, deck))

            deck = shuffle(h1, h2)
            self.assertTrue(is_single_riffle(h1, h2, deck),
                            "\nh1 %s h2 %s\ndeck %s" % (h1, h2, deck))
            self.assertTrue(is_single_riffle2(h1, h2, deck),
                            "\nh1 %s h2 %s\ndeck %s" % (h1, h2, deck))

    def test_3nbad_riffles(self):
        for i in range(100):
            h1, h2, deck = first_riffle()
            self.assertTrue(is_single_riffle(h1, h2, deck),
                            "\nh1 %s h2 %s\ndeck %s" % (h1, h2, deck))
            self.assertTrue(is_single_riffle2(h1, h2, deck),
                            "\nh1 %s h2 %s\ndeck %s" % (h1, h2, deck))

            deck = shuffle(h1, h2)
            self.assertTrue(is_single_riffle(h1, h2, deck),
                            "\nh1 %s h2 %s\ndeck %s" % (h1, h2, deck))
            self.assertTrue(is_single_riffle2(h1, h2, deck),
                            "\nh1 %s h2 %s\ndeck %s" % (h1, h2, deck))

            h1index = int(len(h1) / 2)
            h2index = int(len(h2) / 2)
            h1[h1index], h2[h2index] = h2[h2index], h1[h1index]
            h1index -= 1
            h2index += 1
            h1[h1index], h2[h2index] = h2[h2index], h1[h1index]
            self.assertFalse(is_single_riffle(
                h1, h2, deck), "\nh1 %s\nh2 %s\ndeck: %s\nh1index %s\nh2index %s"
                % (h1, h2, deck, h1index, h2index))
            self.assertFalse(is_single_riffle2(
                h1, h2, deck), "\nh1 %s\nh2 %s\ndeck: %s\nh1index %s\nh2index %s"
                % (h1, h2, deck, h1index, h2index))


if __name__ == "__main__":
    # unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSingleRiffleCheck)
    for i in range(1000):
        print(i)
        unittest.TextTestRunner(verbosity=2).run(suite)
