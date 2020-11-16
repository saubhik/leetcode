from typing import List


class Solution:
    # Time Complexity: O(n).
    # Space Complexity: O(n).
    def removeInterval(
        self, intervals: List[List[int]], toBeRemoved: List[int]
    ) -> List[List[int]]:
        ans = []
        for interval in intervals:
            # Case 1
            if interval[1] <= toBeRemoved[0] or toBeRemoved[1] <= interval[0]:
                ans.append(interval)

            # Case 2
            elif interval[0] <= toBeRemoved[0] < interval[1] < toBeRemoved[1]:
                if interval[0] != toBeRemoved[0]:
                    ans.append([interval[0], toBeRemoved[0]])

            # Case 3
            elif interval[0] <= toBeRemoved[0] < toBeRemoved[1] < interval[1]:
                if interval[0] != toBeRemoved[0]:
                    ans.append([interval[0], toBeRemoved[0]])
                ans.append([toBeRemoved[1], interval[1]])

            # Case 4
            elif toBeRemoved[0] <= interval[0] < toBeRemoved[1] < interval[1]:
                ans.append([toBeRemoved[1], interval[1]])

        return ans


class SolutionTwo:
    # Uniform treatment for every interval.
    # Instead of breaking down into cases.
    def removeInterval(
        self, intervals: List[List[int]], toBeRemoved: List[int]
    ) -> List[List[int]]:
        ans = []
        ta, tb = toBeRemoved
        for a, b in intervals:
            t = min(ta, b)
            if t > a:
                ans.append([a, t])

            t = max(a, tb)
            if t < b:
                ans.append([t, b])

        return ans
