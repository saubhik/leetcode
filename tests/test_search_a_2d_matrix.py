import unittest

from search_a_2d_matrix import Solution


class TestSearchA2DMatrix(unittest.TestCase):
    def test_example_1(self):
        assert (
            Solution().searchMatrix(
                matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], target=3
            )
            is True
        )

    def test_example_2(self):
        assert (
            Solution().searchMatrix(
                matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], target=13
            )
            is False
        )

    def test_example_3(self):
        assert Solution().searchMatrix(matrix=[], target=0) is False

    def test_example_4(self):
        assert Solution().searchMatrix(matrix=[[]], target=1) is False

    def test_example_5(self):
        assert Solution().searchMatrix(matrix=[[1, 1]], target=2) is False

    def test_example_6(self):
        assert Solution().searchMatrix(matrix=[[1], [3]], target=4) is False

    def test_example_7(self):
        assert (
            Solution().searchMatrix(
                matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], target=11
            )
            is True
        )
