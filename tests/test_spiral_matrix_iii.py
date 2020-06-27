import unittest

from spiral_matrix_iii import Solution


class TestSpiralMatrixIII(unittest.TestCase):
    def setUp(self) -> None:
        self.solve = Solution().spiralMatrixIII

    def test_example_1(self):
        self.assertEqual(
            first=self.solve(R=1, C=4, r0=0, c0=0),
            second=[[0, 0], [0, 1], [0, 2], [0, 3]],
        )

    def test_example_2(self):
        self.assertEqual(
            first=self.solve(R=5, C=6, r0=1, c0=4),
            second=[
                [1, 4],
                [1, 5],
                [2, 5],
                [2, 4],
                [2, 3],
                [1, 3],
                [0, 3],
                [0, 4],
                [0, 5],
                [3, 5],
                [3, 4],
                [3, 3],
                [3, 2],
                [2, 2],
                [1, 2],
                [0, 2],
                [4, 5],
                [4, 4],
                [4, 3],
                [4, 2],
                [4, 1],
                [3, 1],
                [2, 1],
                [1, 1],
                [0, 1],
                [4, 0],
                [3, 0],
                [2, 0],
                [1, 0],
                [0, 0],
            ],
        )
