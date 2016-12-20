#!python

# interviewcake 5 Making Change
# https://www.interviewcake.com/question/python/coin

# Imagine you landed a new job as a cashier...
#
# Your quirky boss found out that you're a programmer and has a weird
# request about something they've been wondering for a long time.
#
# Write a function that, given:
#
# 1. an amount of money
# 2. a list of coin denominations
#
# computes the number of ways to make amount of money with coins of the
# available denominations.
#
# Example: for amount=4 (4c) and denominations=[1,2,3] (1c, 2c and 3c),
# your program would output 4 - the number of ways to make
# 4c with those denominations:
#
# 1c, 1c, 1c, 1c
# 1c, 1c, 2c
# 1c, 3c
# 2c, 2c


def make_change(amount, denominations):
    denominations.sort()
    denominations.reverse()
    patterns = _make_change(amount, denominations)
    uniques = uniquify(patterns)
    count = len(uniques)
    print("%s ways to make change for %s using %s" %
          (count, amount, denominations))
    return count


def uniquify(patterns):
    s = set()
    # patterns is a list of lists
    # each pattern is a decomposition of the summands of the amount in terms
    # of the denominations
    for p in patterns:
        p.sort()
        strp = str(p)
        # print("pattern: %s" % strp)
        s.add(strp)
    elts = list(s)
    elts.sort()
    return elts


def spaces(n):
    spaces = "                    "
    return spaces[0: 2 * n]


def _make_change(amount, denominations, level=0):
    # print("%s _mc: %s with %s" % (spaces(level), amount, denominations))
    patterns = []
    for d in denominations:
        (quotient, remainder) = divmod(amount, d)
        # print("%s _mc: divmod(%s, %s) => quotient %s, remainder %s" %
        #       (spaces(level), amount, d, quotient, remainder))
        if quotient > 0:
            if quotient == 1 and remainder == 0:
                patterns.append([d])
            else:
                sub_patterns = _make_change(
                    amount - d, denominations, level + 1)
                for pattern in sub_patterns:
                    pat = [d]
                    pat.extend(pattern)
                    patterns.append(pat)
                    # print("%s _mc: pat %s, patterns %s" %
                    #       (spaces(level), pat, patterns))
    # print("%s _mc: <- patterns %s" %
    #       (spaces(level), patterns))
    return patterns

if __name__ == "__main__":
    make_change(1, [1])
    make_change(1, [2])
    make_change(1, [3])
    make_change(2, [1])
    make_change(2, [1, 2])
    make_change(2, [1, 2, 3])
    make_change(2, [3])
    make_change(4, [1, 2, 3])
    # make_change(200, [1, 2, 5, 10, 20, 50, 100, 200])
