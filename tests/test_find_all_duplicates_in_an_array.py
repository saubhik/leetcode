import unittest

from find_all_duplicates_in_an_array import Solution, SolutionTwo


class TestFindAllDuplicatesInAnArray(unittest.TestCase):
    def test_example_1(self):
        assert set(Solution().findDuplicates(nums=[4, 3, 2, 7, 8, 2, 3, 1])) == {2, 3}

    def test_example_2(self):
        assert set(SolutionTwo().findDuplicates(nums=[4, 3, 2, 7, 8, 2, 3, 1])) == {
            2,
            3,
        }
