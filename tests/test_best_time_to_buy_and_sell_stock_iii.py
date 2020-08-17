import unittest

from best_time_to_buy_and_sell_stock_iii import Solution


class TestBestTimeToBuyAndSellStockIII(unittest.TestCase):
    def test_example_1(self):
        assert Solution().maxProfit(prices=[3, 3, 5, 0, 0, 3, 1, 4]) == 6

    def test_example_2(self):
        assert Solution().maxProfit(prices=[1, 2, 3, 4, 5]) == 4

    def test_example_3(self):
        assert Solution().maxProfit(prices=[7, 6, 4, 3, 1]) == 0

    def test_example_4(self):
        assert Solution().maxProfit(prices=[]) == 0
