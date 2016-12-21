def isRiffle(deck):
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

from random import randrange


def riffle():
    split = randrange(0, 52)
    d1 = []
    for i in range(split):
        d1.append(i)

    d2 = []
    for i in range(split, 52):
        d2.append(i)

    return shuffle(d1, d2, 4)


def shuffle(d1, d2, maxcards):
    deck = []

    while((len(d1) > 0) or (len(d2) > 0)):

        d1cards = randrange(1, maxcards)
        d1cards = min(d1cards, len(d1))
        d1slice = d1[0:d1cards]
        d1 = d1[d1cards:]

        d2cards = randrange(1, maxcards)
        d2cards = min(d2cards, len(d2))
        d2slice = d2[0:d2cards]
        d2 = d2[d2cards:]

        deck.extend(d1slice)
        deck.extend(d2slice)

    return deck


def is_single_riffle_recursive(half1, half2, shuffled_deck):

    # base case
    if len(shuffled_deck) == 0:
        return True

    # if the top of shuffled_deck is the same as the top of half1
    # (making sure first that we have a top card in half1)
    if len(half1) and half1[0] == shuffled_deck[0]:

        # take the top cards off half1 and shuffled_deck and recurse
        return is_single_riffle_recursive(half1[1:], half2, shuffled_deck[1:])

    # if the top of shuffled_deck is the same as the top of half2
    elif len(half2) and half2[0] == shuffled_deck[0]:

        # take the top cards off half2 and shuffled_deck and recurse
        return is_single_riffle_recursive(half1, half2[1:], shuffled_deck[1:])

    # top of shuffled_deck doesn't match top of half1 or half2
    # so we know it's not a single riffle
    else:
        return False

deck = riffle()
print(deck)
print(isRiffle(deck))
print(is_single_riffle_recursive(

deck=riffle()
for n in range(5):
    i=randrange(52)
    j=randrange(52)
    (deck[i], deck[j])=(deck[j], deck[i])
print(deck)
print(isRiffle(deck))

deck=riffle()
print(deck)
print(isRiffle(deck))
