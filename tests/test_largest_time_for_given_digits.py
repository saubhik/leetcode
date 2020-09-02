import unittest

from largest_time_for_given_digits import Solution


class TestLargestTimeForGivenDigits(unittest.TestCase):
    def test_example_1(self):
        assert Solution().largestTimeFromDigits(A=[1, 2, 3, 4]) == "23:41"

    def test_example_2(self):
        assert Solution().largestTimeFromDigits(A=[5, 5, 5, 5]) == ""
