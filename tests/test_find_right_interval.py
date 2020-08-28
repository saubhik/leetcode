import unittest

from find_right_interval import Solution, SolutionTwo


class TestFindRightInterval(unittest.TestCase):
    def test_example_1(self):
        assert Solution().findRightInterval(intervals=[[1, 2]]) == [-1]
        assert SolutionTwo().findRightInterval(intervals=[[1, 2]]) == [-1]

    def test_example_2(self):
        assert Solution().findRightInterval(intervals=[[3, 4], [2, 3], [1, 2]]) == [
            -1,
            0,
            1,
        ]
        assert SolutionTwo().findRightInterval(intervals=[[3, 4], [2, 3], [1, 2]]) == [
            -1,
            0,
            1,
        ]

    def test_example_3(self):
        assert Solution().findRightInterval(intervals=[[1, 4], [2, 3], [3, 4]]) == [
            -1,
            2,
            -1,
        ]
        assert SolutionTwo().findRightInterval(intervals=[[1, 4], [2, 3], [3, 4]]) == [
            -1,
            2,
            -1,
        ]
