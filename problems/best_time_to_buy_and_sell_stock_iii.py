from typing import List


class Solution:
    # [3,3,5,0,0,3,1,4]
    # left_profits:
    # [0,0,2,2,2,3,3,4]
    # right profits:
    # [3,3,3,3,3,3,3,0]
    #
    # Time: O(n)
    # Space: O(n)
    # Bidirectional Dynamic Programming
    def maxProfit(self, prices: List[int]) -> int:
        # O(n) time, O(n) space
        left_profits = []
        min_price_so_far = float("inf")
        max_profit_so_far = float("-inf")
        for price in prices:
            if price < min_price_so_far:
                min_price_so_far = price
            max_profit_so_far = max(max_profit_so_far, price - min_price_so_far)
            left_profits.append(max_profit_so_far)

        # O(n) time, O(n) space
        right_profits = []
        max_profit_so_far = float("-inf")
        max_price_so_far = float("-inf")
        for price in reversed(prices):
            if price > max_price_so_far:
                max_price_so_far = price
            max_profit_so_far = max(max_profit_so_far, max_price_so_far - price)
            right_profits.append(max_profit_so_far)
        right_profits.reverse()

        # O(n) time
        n = len(prices)
        max_profit = 0
        for i in range(n):
            if i + 1 < n:
                max_profit = max(max_profit, left_profits[i] + right_profits[i + 1])
            else:
                max_profit = max(max_profit, left_profits[i])

        return max_profit
