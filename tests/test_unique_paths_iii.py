import unittest

from unique_paths_iii import Solution


class TestUniquePathsIII(unittest.TestCase):
    def test_example_1(self):
        grid = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]
        assert Solution().uniquePathsIII(grid=grid) == 2

    def test_example_2(self):
        grid = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]]
        assert Solution().uniquePathsIII(grid=grid) == 4

    def test_example_3(self):
        grid = [[0, 1], [2, 0]]
        assert Solution().uniquePathsIII(grid=grid) == 0
