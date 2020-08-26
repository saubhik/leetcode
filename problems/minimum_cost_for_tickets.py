import bisect
from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0] * len(days)
        for i in range(len(dp)):
            idx_1 = bisect.bisect(days, days[i] - 1) - 1
            cost_1 = (dp[idx_1] if idx_1 >= 0 else 0) + costs[0]
            idx_7 = bisect.bisect(days, days[i] - 7) - 1
            cost_7 = (dp[idx_7] if idx_7 >= 0 else 0) + costs[1]
            idx_30 = bisect.bisect(days, days[i] - 30) - 1
            cost_30 = (dp[idx_30] if idx_30 >= 0 else 0) + costs[2]
            dp[i] = min(cost_1, cost_7, cost_30)
        return dp[-1]
