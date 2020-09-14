import unittest

from insert_interval import Solution


class TestInsertInterval(unittest.TestCase):
    def test_example_1(self):
        assert Solution().insert(intervals=[[1, 3], [6, 9]], newInterval=[2, 5]) == [
            [1, 5],
            [6, 9],
        ]

    def test_example_2(self):
        assert Solution().insert(
            intervals=[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], newInterval=[4, 8]
        ) == [[1, 2], [3, 10], [12, 16]]
