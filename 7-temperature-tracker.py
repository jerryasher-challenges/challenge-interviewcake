#!python

######################################################################
# this problem is from
# from https://www.interviewcake.com/question/python/temperature-tracker

# You decide to test if your oddly-mathematical heating company is
# fulfilling its All-Time Max, Min, Mean and Mode Temperature
# Guarantee.
#
# Write a class TempTracker with these methods:
#
# + insert() - records a new temperature
# + get_max() - returns the highest temp we've seen so far
# + get_min() - returns the lowest temp we've seen so far
# + get_mean() - returns the mean of all temps we've seen so far
# + get_mode() - returns a mode of all temps we've seen so far
#
# Optimize for space and time. Favor speeding up the getter functions
# (get_max(), get_min(), get_mean(), and get_mode()) over speeding up
# the insert() function.
#
# get_mean() should return a float, but the rest of the getter functions
# can return integers. Temperatures will all be inserted as
# integers. We'll record our temperatures in Fahrenheit, so we can
# assume they'll all be in the range 0..110
#
# If there is more than one mode, return any of the modes.
######################################################################

# Now my turn


import unittest


class TempTracker:
    """Temperature Tracker"""

    def __init__(self):
        self.temps = [0] * 111
        self.num_temps = 0
        self.min = 111
        self.max = -1
        self.total = 0
        self.mean = None
        self.max_freq = 0
        self.mode = None

    def insert(self, temp):
        if temp < 0 or temp > 110:
            raise Exception
        self.temps[temp] += 1
        self.num_temps += 1
        if temp < self.min:
            self.min = temp
        if temp > self.max:
            self.max = temp
        self.total += temp
        self.mean = self.total / float(self.num_temps)
        if self.temps[temp] > self.max_freq:
            self.max_freq = self.temps[temp]
            self.mode = temp

    def get_max(self):
        max = self.max
        if max == -1:
            max = None
        return max

    def get_min(self):
        min = self.min
        if min == 111:
            min = None
        return min

    def get_mean(self):
        return self.mean

    def get_mode(self):
        return self.mode


class TestTempTracker(unittest.TestCase):

    def _test_tracker(self, temps, min, max, mean, modes):
        tracker = TempTracker()
        for temp in temps:
            tracker.insert(temp)
        print("")
        print("Test: temps = %s" % temps)
        print(" min %s max %s" % (tracker.get_min(), tracker.get_max()))
        self.assertTrue(tracker.get_min() == min)
        self.assertTrue(tracker.get_max() == max)
        print(" mean %s mode %s" % (tracker.get_mean(), tracker.get_mode()))
        self.assertTrue(tracker.get_mean() == mean)
        self.assertTrue(tracker.get_mode() in modes)

    def test_null(self):
        self._test_tracker([], None, None, None, [None])

    def test_0(self):
        self._test_tracker([0], 0, 0, 0, [0])

    def test_01(self):
        self._test_tracker([0, 1], 0, 1, 0.5, [0, 1])

    def test_011(self):
        self._test_tracker([0, 1, 1], 0, 1, 2 / 3.0, [1])

    def test_0112(self):
        self._test_tracker([0, 1, 1, 2], 0, 2, 4 / 4.0, [1])

    def test_0111225(self):
        self._test_tracker([0, 1, 1, 2, 2, 5], 0, 5, 11 / 6.0, [1, 2])

    def test_011122555(self):
        self._test_tracker([0, 1, 1, 2, 2, 5, 5, 5], 0, 5, 21 / 8.0, [5])

    def test_extremes(self):
        tracker = TempTracker()
        self.assertRaises(Exception, tracker.insert, -1)
        self.assertRaises(Exception, tracker.insert, 111)


if __name__ == "__main__":
    # unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTempTracker)
    unittest.TextTestRunner(verbosity=2).run(suite)
