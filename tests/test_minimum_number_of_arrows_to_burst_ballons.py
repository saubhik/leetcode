import unittest

from minimum_number_of_arrows_to_burst_balloons import OfficialSolution, Solution


class TestMinimumNumberOfArrowsToBurstBalloons(unittest.TestCase):
    def test_example_1(self):
        assert (
            Solution().findMinArrowShots(points=[[10, 16], [2, 8], [1, 6], [7, 12]])
            == 2
        )
        assert (
            OfficialSolution().findMinArrowShots(
                points=[[10, 16], [2, 8], [1, 6], [7, 12]]
            )
            == 2
        )

    def test_example_2(self):
        assert (
            Solution().findMinArrowShots(points=[[1, 2], [3, 4], [5, 6], [7, 8]]) == 4
        )
        assert (
            OfficialSolution().findMinArrowShots(
                points=[[1, 2], [3, 4], [5, 6], [7, 8]]
            )
            == 4
        )

    def test_example_3(self):
        assert (
            Solution().findMinArrowShots(points=[[1, 2], [2, 3], [3, 4], [4, 5]]) == 2
        )
        assert (
            OfficialSolution().findMinArrowShots(
                points=[[1, 2], [2, 3], [3, 4], [4, 5]]
            )
            == 2
        )

    def test_example_4(self):
        assert Solution().findMinArrowShots(points=[[1, 2]]) == 1
        assert OfficialSolution().findMinArrowShots(points=[[1, 2]]) == 1

    def test_example_5(self):
        assert Solution().findMinArrowShots(points=[[2, 3], [2, 3]]) == 1
        assert OfficialSolution().findMinArrowShots(points=[[2, 3], [2, 3]]) == 1

    def test_example_6(self):
        assert Solution().findMinArrowShots(points=[]) == 0
        assert OfficialSolution().findMinArrowShots(points=[]) == 0
