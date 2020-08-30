import unittest

from pancake_sorting import Solution


class TestPancakeSorting(unittest.TestCase):
    def test_example_1(self):
        assert Solution().pancakeSort(A=[3, 2, 4, 1]) == [3, 4, 2, 3, 2]

    def test_example_2(self):
        assert Solution().pancakeSort(A=[1, 2, 3, 4, 5]) == []
