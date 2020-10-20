import unittest

from minimum_domino_rotations_for_equal_row import Solution


class TestMinimumDominoRotationsForEqualRow(unittest.TestCase):
    def test_example_1(self):
        assert (
            Solution().minDominoRotations(A=[2, 1, 2, 4, 2, 2], B=[5, 2, 6, 2, 3, 2])
            == 2
        )

    def test_example_2(self):
        assert Solution().minDominoRotations(A=[3, 5, 1, 2, 3], B=[3, 6, 3, 3, 4]) == -1
