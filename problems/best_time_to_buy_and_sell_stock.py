from typing import List


class Solution:
    # Straight Forward DP.
    #
    # Time: O(n). One Pass.
    # Space: O(1) additional space.
    #
    #              [ 7,    1, 5, 3, 6, 4]
    # min_cost  :  inf,  inf, 1, 1, 1, 1
    # profit_i  : -inf, -inf, 4, 2, 5, 3
    # Max of profit_i is 5.
    def maxProfit(self, prices: List[int]) -> int:
        min_cost_before_i = float("inf")
        max_profit = 0
        for price in prices:
            max_profit = max(max_profit, price - min_cost_before_i)
            min_cost_before_i = min(min_cost_before_i, price)
        return max_profit
