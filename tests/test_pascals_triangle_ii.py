import unittest

from pascals_triangle_ii import Solution


class TestPascalsTriangleII(unittest.TestCase):
    def test_example_1(self):
        assert Solution().getRow(rowIndex=3) == [1, 3, 3, 1]

    def test_example_2(self):
        assert Solution().getRow(rowIndex=4) == [1, 4, 6, 4, 1]

    def test_example_3(self):
        assert Solution().getRow(rowIndex=0) == [1]
