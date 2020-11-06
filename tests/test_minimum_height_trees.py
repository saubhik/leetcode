import unittest

from minimum_height_trees import Solution


class TestMinimumHeightTrees(unittest.TestCase):
    def test_example_1(self):
        assert Solution().findMinHeightTrees(n=4, edges=[[1, 0], [1, 2], [1, 3]]) == [1]

    def test_example_2(self):
        assert Solution().findMinHeightTrees(
            n=6, edges=[[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]
        ) == [4, 3]

    def test_example_3(self):
        assert Solution().findMinHeightTrees(n=1, edges=[]) == [0]

    def test_example_4(self):
        assert Solution().findMinHeightTrees(n=2, edges=[[0, 1]]) == [0, 1]
