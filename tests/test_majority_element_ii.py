import unittest

from majority_element_ii import OfficialSolution


class TestMajorityElementII(unittest.TestCase):
    def test_example_1(self):
        assert OfficialSolution().majorityElement(nums=[3, 2, 3]) == [3]

    def test_example_2(self):
        assert OfficialSolution().majorityElement(nums=[1, 1, 1, 3, 3, 2, 2, 2]) == [
            1,
            2,
        ]

    def test_example_3(self):
        assert OfficialSolution().majorityElement(nums=[0, -1, 2, -1]) == [-1]

    def test_example_4(self):
        assert OfficialSolution().majorityElement(nums=[1, 2, 3, 4]) == []
