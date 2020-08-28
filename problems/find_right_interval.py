from typing import List


class Solution:
    # Gets TLE'd.
    # Time: O(n^2)
    # Space: O(n)
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        ans = [-1] * n
        for i in range(n):
            min_diff = float("inf")
            for j in range(n):
                if j != i and 0 <= (intervals[j][0] - intervals[i][1]) < min_diff:
                    min_diff = intervals[j][0] - intervals[i][1]
                    ans[i] = j
        return ans


# Approach 5: Using Two Arrays
# Maintain two arrays:
# 1. intervals, which is sorted based on the start points
# 2. endIntervals, which is sorted based on the end points
class SolutionTwo:
    # Time: O(nlogn)
    # Space: O(n)
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        intervals = [
            (interval[0], interval[1], i) for i, interval in enumerate(intervals)
        ]
        n = len(intervals)
        ans, j = [-1] * n, 0
        intervals_st = sorted(intervals, key=lambda x: x[0])
        intervals_en = sorted(intervals, key=lambda x: x[1])
        for i in range(n):
            while j < n:
                if intervals_st[j][0] >= intervals_en[i][1]:
                    ans[intervals_en[i][2]] = intervals_st[j][2]
                    break
                j += 1
        return ans
