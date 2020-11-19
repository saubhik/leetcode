from typing import List


class Solution:
    # Linear Scan on Sorted List.
    # Time Complexity: O(nlogn).
    # Space Complexity: O(n), because of Python's TimSort using O(n) space.
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged_intervals = [intervals[0]]

        for interval in intervals:
            last_merged_interval = merged_intervals[-1]
            if interval[0] <= last_merged_interval[1]:
                last_merged_interval[1] = max(last_merged_interval[1], interval[1])
            else:
                merged_intervals.append(interval)

        return merged_intervals
