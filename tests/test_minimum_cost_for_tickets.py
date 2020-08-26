import unittest

from minimum_cost_for_tickets import Solution


class TestMinimumCostForTickets(unittest.TestCase):
    def test_example_1(self):
        assert (
            Solution().mincostTickets(days=[1, 4, 6, 7, 8, 20], costs=[2, 7, 15]) == 11
        )

    def test_example_3(self):
        assert (
            Solution().mincostTickets(
                days=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], costs=[2, 7, 15]
            )
            == 17
        )
