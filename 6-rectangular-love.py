#!python

# https://www.interviewcake.com/question/python/rectangular-love

# A crack team of love scientists from OkEros (a hot new dating site)
# have devised a way to represent dating profiles as rectangles on a
# two-dimensional plane.

# They need help writing an algorithm to find the intersection of two
# users' love rectangles. They suspect finding that intersection is the
# key to a matching algorithm so powerful it will cause an immediate
# acquisition by Google or Facebook or Obama or something.

# Write a function to find the rectangular intersection of two given
# love rectangles.

# As with the example above, love rectangles are always "straight" and
# never "diagonal." More rigorously: each side is parallel with either
# the x-axis or the y-axis.

# They are defined as dictionaries like this:

#   my_rectangle = {

#     # coordinates of bottom-left corner
#     'left_x': 1,
#     'bottom_y': 5,

#     # width and height
#     'width': 10,
#     'height': 4,

# }

# Your output rectangle should use this format as well.

from random import randint


def rectangular_intersection(rect1, rect2):

    (r1, r2) = (rect1, rect2) \
        if rect1['left_x'] <= rect2['left_x'] else (rect2, rect1)

    # r1 = rect1 if rect1['left_x'] <= rect2['left_x'] else rect2
    # r2 = rect2 if rect1['left_x'] <= rect2['left_x'] else rect1

    if r1['left_x'] + r1['width'] <= r2['left_x']:
        return None

    left_x = max(r1['left_x'], r2['left_x'])
    right_x = min(r1['left_x'] + r1['width'], r2['left_x'] + r2['width'])
    width = right_x - left_x

    (r1, r2) = (rect1, rect2) \
        if rect1['bottom_y'] <= rect2['bottom_y'] else (rect2, rect1)

    # r1 = rect1 if rect1['bottom_y'] <= rect2['bottom_y'] else rect2
    # r2 = rect2 if rect1['bottom_y'] <= rect2['bottom_y'] else rect1

    if r1['bottom_y'] + r1['height'] <= r2['bottom_y']:
        return None

    lower_y = max(r1['bottom_y'], r2['bottom_y'])
    upper_y = min(r1['bottom_y'] + r1['height'], r2['bottom_y'] + r2['height'])
    height = upper_y - lower_y

    intersection = {
        'left_x': left_x,
        'bottom_y': lower_y,
        'width': width,
        'height': height
    }

    return intersection


def rectangular_intersection2(r1, r2):

    left_x = max(r1['left_x'], r2['left_x'])
    right_x = min(r1['left_x'] + r1['width'], r2['left_x'] + r2['width'])
    width = right_x - left_x

    lower_y = max(r1['bottom_y'], r2['bottom_y'])
    upper_y = min(r1['bottom_y'] + r1['height'], r2['bottom_y'] + r2['height'])
    height = upper_y - lower_y

    if width <= 0 or height <= 0:
        return None

    intersection = {
        'left_x': left_x,
        'bottom_y': lower_y,
        'width': width,
        'height': height
    }

    return intersection


def make_rectangle(l):
    (l, b, w, h) = l
    return {
        'left_x': l,
        'bottom_y': b,
        'width': w,
        'height': h,
    }

if __name__ == "__main__":

    r1 = make_rectangle([1, 5, 10, 4])
    tests = [
        [make_rectangle([2, 6, 2, 2]),
         make_rectangle([2, 6, 2, 2])],
        [make_rectangle([2, 6, 9, 3]),
         make_rectangle([2, 6, 9, 3])],
        [make_rectangle([2, 6, 10, 4]),
         make_rectangle([2, 6, 9, 3])],
        [make_rectangle([10, 5, 10, 2]),
         make_rectangle([10, 5, 1, 2])],
        [make_rectangle([0, 0, 1, 1]),
         None],
        [make_rectangle([2, 0, 9, 2]),
         None],
        [make_rectangle([2, 10, 10, 4]),
         None]
    ]

    print("test cases")
    for (r2, answer) in tests:
        soln1 = rectangular_intersection(r1, r2)
        soln2 = rectangular_intersection2(r1, r2)

        print("r1 = %s" % r1)
        print("r2 = %s" % r2)
        print("answer = %s" % answer)
        print(" soln1 = %s" % soln1)
        print(" soln2 = %s" % soln2)

        if soln1 != answer:
            print("test case failed, soln1 is not answer")
            raise Exception
        if soln1 != soln2:
            print("test case failed, soln1 is not soln2")
            raise Exception
        print("")

    print("")
    print("random rects")

    r1 = make_rectangle([1, 1, 8, 8])
    overlaps = 0
    for i in range(1000000):
        l = randint(-10, 20)
        b = randint(-10, 20)
        w = randint(1, 15)
        h = randint(1, 15)
        r2 = make_rectangle([l, b, w, h])
        soln1 = rectangular_intersection(r1, r2)
        soln2 = rectangular_intersection2(r1, r2)
        if soln1 != soln2:
            print("trial %s" % i)
            print("soln1 != soln2!")
            print("r1 = %s" % r1)
            print("r2 = %s" % r2)
            print("soln1 = %s" % soln1)
            print("soln2 = %s" % soln2)
            raise Exception
        elif soln1:
            overlaps += 1
            # print("trial %s" % i)
            # print("r2 = %s" % r2)
            # print("soln1 = %s" % soln1)
            # print("soln2 = %s" % soln2)
            # print("")
    print("random rects: %s overlaps found" % overlaps)
