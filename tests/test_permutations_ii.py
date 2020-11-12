from unittest import TestCase

from permutations_ii import Solution


class TestPermutations(TestCase):
    def test_example_1(self):
        assert Solution().permuteUnique(nums=[1, 1, 2]) == [
            [1, 1, 2],
            [1, 2, 1],
            [2, 1, 1],
        ]
