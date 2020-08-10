import unittest

from rotting_oranges import Solution, SolutionTwo


class TestOrangesRotting(unittest.TestCase):
    def test_example_1(self):
        grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
        assert Solution().orangesRotting(grid=grid) == 4

    def test_example_1_two(self):
        grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
        assert SolutionTwo().orangesRotting(grid=grid) == 4

    def test_example_2(self):
        grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
        assert Solution().orangesRotting(grid=grid) == -1

    def test_example_2_two(self):
        grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
        assert SolutionTwo().orangesRotting(grid=grid) == -1

    def test_example_3(self):
        grid = [[0, 2]]
        assert Solution().orangesRotting(grid=grid) == 0

    def test_example_3_two(self):
        grid = [[0, 2]]
        assert SolutionTwo().orangesRotting(grid=grid) == 0

    def test_example_4(self):
        grid = [[1]]
        assert Solution().orangesRotting(grid=grid) == -1

    def test_example_4_two(self):
        grid = [[1]]
        assert SolutionTwo().orangesRotting(grid=grid) == -1

    def test_example_5(self):
        grid = [[0]]
        assert Solution().orangesRotting(grid=grid) == 0

    def test_example_5_two(self):
        grid = [[0]]
        assert SolutionTwo().orangesRotting(grid=grid) == 0
