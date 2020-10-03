import unittest

from first_missing_positive import OfficialSolution


class TestFirstMissingPositive(unittest.TestCase):
    def test_example_1(self):
        assert OfficialSolution().firstMissingPositive(nums=[1, 2, 0]) == 3

    def test_example_2(self):
        assert OfficialSolution().firstMissingPositive(nums=[3, 4, -1, 1]) == 2

    def test_example_3(self):
        assert OfficialSolution().firstMissingPositive(nums=[7, 8, 9, 11, 12]) == 1
