import unittest

from best_time_to_buy_and_sell_stock import Solution


class TestBestTimeToBuyAndSellStock(unittest.TestCase):
    def test_example_1(self):
        assert Solution().maxProfit(prices=[7, 1, 5, 3, 6, 4]) == 5

    def test_example_2(self):
        assert Solution().maxProfit(prices=[]) == 0

    def test_example_3(self):
        assert Solution().maxProfit(prices=[7, 6, 4, 3, 1]) == 0
