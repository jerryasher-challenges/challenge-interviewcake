#!python

# interviewcake 3, highest product of 3
# https://www.interviewcake.com/question/highest-product-of-3

# Given a list_of_ints, find the highest_product you can get from three of
# the integers.

# The input list_of_ints will always have at least three integers.


# "correct answer for this problem", reduce logic complexity by trying
# all answers, letting some fail, determining correct answer in last comparison

def highest_product0(list_of_ints):
    list_of_ints.sort()
    min0 = list_of_ints[0]
    min1 = list_of_ints[1]

    max0 = list_of_ints[-1]
    max1 = list_of_ints[-2]
    max2 = list_of_ints[-3]

    poss1 = min0 * min1 * max0
    poss2 = max0 * max1 * max2

    return poss1 if poss1 > poss2 else poss2


# first approach, correct and better than brute force, but way too
# many comparisons (ie complex logic)
def highest_product1(list_of_ints):
    neg = []
    pos = []
    for int in list_of_ints:
        if int < 0:
            neg.append(int)
        else:
            pos.append(int)
    neg.sort()
    pos.sort()

    if len(pos) == 0:
        # no pos ints, so highest number are three "small" negs
        return(neg[-3] * neg[-2] * neg[-1])
    elif len(pos) == 1:
        # 1 pos int, so return that * prod of two "large" negs
        return(neg[0] * neg[1] * pos[-1])
    elif len(neg) >= 2:
        maxneg = neg[0] * neg[1]
        if maxneg > pos[-3] * pos[-2]:
            return maxneg * pos[-1]
    elif len(pos) == 2:
        return neg[-1] * pos[-2] * pos[-1]
    else:
        return pos[-3] * pos[-2] * pos[-1]


l = [1, 2, 3]
print(l)
print(highest_product0(l))
print(highest_product1(l))
print()

l = [-1, 0, 1]
print(l)
print(highest_product0(l))
print(highest_product1(l))
print()


l = [-3, -4, 2]
print(highest_product0(l))
print(highest_product1(l))
print()


l = [0, 1, 2, 3, 4, 5]
print(l)
print(highest_product0(l))
print(highest_product1(l))
print()

l = [-1, 0, 1, 2, 3, 4]
print(highest_product0(l))
print(highest_product1(l))
print()

l = [-3, -4, 0, 1, 2, 3, 4]
print(l)
print(highest_product0(l))
print(highest_product1(l))
print()

l = [1, 2, 3, -3, -4, 0, 4]
print(highest_product0(l))
print(highest_product1(l))
print()

l = [-1, -2, -3, 0, 1, 2, 30, 1, 2, -4, -5, 3]
print(l)
print(highest_product0(l))
print(highest_product1(l))
print()

l = [-10, -10, 1, 3, 2]
print(l)
print(highest_product0(l))
print(highest_product1(l))
print()
