from typing import List


class Solution:
    # Greedy.
    # The idea of greedy algorithm is to pick the locally optimal move at each step,
    # that will lead to the globally optimal solution.
    #
    # newInterval can be:
    # - ends before start of current interval
    # - ends between start and end of current interval
    # - starts between start and end of current interval
    # - starts after end of current interval
    #
    # Time: O(n)
    # Space: O(n) to keep output.
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        merged = False
        ans = []

        for interval in intervals:
            if merged:
                ans.append(interval)

            # ends before start of current interval
            elif newInterval[1] < interval[0]:
                ans.append(newInterval)
                ans.append(interval)
                merged = True

            # ends between start and end of current interval
            elif interval[0] <= newInterval[1] <= interval[1]:
                interval[0] = min(interval[0], newInterval[0])
                ans.append(interval)
                merged = True

            # starts between start and end of current interval
            elif interval[0] <= newInterval[0] <= interval[1]:
                newInterval = [interval[0], max(newInterval[1], interval[1])]

            # starts after end of current interval
            elif interval[1] < newInterval[0]:
                ans.append(interval)

        if not merged:
            ans.append(newInterval)

        return ans
