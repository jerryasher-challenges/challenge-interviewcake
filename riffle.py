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

print(riffle())
print(riffle())
print(riffle())
