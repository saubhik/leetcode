from unittest import TestCase

from remove_interval import Solution, SolutionTwo


class TestRemoveInterval(TestCase):
    def test_example_1(self):
        assert Solution().removeInterval(
            intervals=[[0, 2], [3, 4], [5, 7]], toBeRemoved=[1, 6]
        ) == [[0, 1], [6, 7]]
        assert SolutionTwo().removeInterval(
            intervals=[[0, 2], [3, 4], [5, 7]], toBeRemoved=[1, 6]
        ) == [[0, 1], [6, 7]]

    def test_example_2(self):
        assert Solution().removeInterval(intervals=[[0, 5]], toBeRemoved=[2, 3]) == [
            [0, 2],
            [3, 5],
        ]
        assert SolutionTwo().removeInterval(intervals=[[0, 5]], toBeRemoved=[2, 3]) == [
            [0, 2],
            [3, 5],
        ]

    def test_example_3(self):
        assert Solution().removeInterval(
            intervals=[[-5, -4], [-3, -2], [1, 2], [3, 5], [8, 9]], toBeRemoved=[-1, 4]
        ) == [[-5, -4], [-3, -2], [4, 5], [8, 9]]
        assert SolutionTwo().removeInterval(
            intervals=[[-5, -4], [-3, -2], [1, 2], [3, 5], [8, 9]], toBeRemoved=[-1, 4]
        ) == [[-5, -4], [-3, -2], [4, 5], [8, 9]]

    def test_example_4(self):
        assert Solution().removeInterval(intervals=[[0, 100]], toBeRemoved=[0, 50]) == [
            [50, 100]
        ]
        assert SolutionTwo().removeInterval(
            intervals=[[0, 100]], toBeRemoved=[0, 50]
        ) == [[50, 100]]
