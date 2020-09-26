import unittest

from largest_number import Solution, OfficialSolution


class TestLargestNumber(unittest.TestCase):
    def test_example_1(self):
        assert Solution().largestNumber(nums=[10, 2]) == "210"
        assert OfficialSolution().largestNumber(nums=[10, 2]) == "210"

    def test_example_2(self):
        assert Solution().largestNumber(nums=[3, 30, 34, 5, 9]) == "9534330"
        assert OfficialSolution().largestNumber(nums=[3, 30, 34, 5, 9]) == "9534330"

    def test_example_3(self):
        assert Solution().largestNumber(nums=[0, 0]) == "0"
        assert OfficialSolution().largestNumber(nums=[0, 0]) == "0"
