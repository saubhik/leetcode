import unittest

from teemo_attacking import OfficialSolution, Solution


class TestTeemoAttacking(unittest.TestCase):
    def test_example_1(self):
        assert Solution().findPoisonedDuration(timeSeries=[1, 4], duration=2) == 4
        assert (
            OfficialSolution().findPoisonedDuration(timeSeries=[1, 4], duration=2) == 4
        )

    def test_example_2(self):
        assert Solution().findPoisonedDuration(timeSeries=[1, 2], duration=2) == 3
        assert (
            OfficialSolution().findPoisonedDuration(timeSeries=[1, 2], duration=2) == 3
        )
