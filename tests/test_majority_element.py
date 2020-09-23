import unittest

from majority_element import OfficialSolution


class TestMajorityElement(unittest.TestCase):
    def test_example_1(self):
        assert OfficialSolution().majorityElement(nums=[3, 2, 3]) == 3

    def test_example_2(self):
        assert OfficialSolution().majorityElement(nums=[2, 2, 1, 1, 1, 2, 2]) == 2
