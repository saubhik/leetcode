import unittest

from minimum_cost_to_move_chips_to_the_same_position import Solution


class TestMinimumCostToMoveChipsToTheSamePosition(unittest.TestCase):
    def test_example_1(self):
        assert Solution().minCostToMoveChips(position=[1, 2, 3]) == 1

    def test_example_2(self):
        assert Solution().minCostToMoveChips(position=[2, 2, 2, 3, 3]) == 2

    def test_example_3(self):
        assert Solution().minCostToMoveChips(position=[1, 1000000000]) == 1
