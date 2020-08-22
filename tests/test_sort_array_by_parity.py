import unittest

from sort_array_by_parity import Solution, SolutionTwo


class TestSortArrayByParity(unittest.TestCase):
    def test_example_1(self):
        assert Solution().sortArrayByParity(A=[3, 1, 2, 4]) == [2, 4, 3, 1]

    def test_example_2(self):
        assert SolutionTwo().sortArrayByParity(A=[3, 1, 2, 4]) == [4, 2, 1, 3]
