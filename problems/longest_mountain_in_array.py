from typing import List


class Solution:
    # Time Complexity: O(n).
    # Space Complexity: O(1).
    def longestMountain(self, A: List[int]) -> int:
        peak_found = False
        before_peak = False
        max_mountain_length = 0
        mountain_length = 0
        i = 1
        while i < len(A):
            if not peak_found:
                if A[i] > A[i - 1]:
                    mountain_length += 1
                    if not before_peak:
                        before_peak = True
                        mountain_length += 1
                elif A[i] < A[i - 1] and before_peak:
                    # Should not consider first number as peak.
                    peak_found = True
                    mountain_length += 1
                else:
                    before_peak, mountain_length = False, 0
                i += 1
            else:
                if A[i] < A[i - 1]:
                    mountain_length += 1
                    i += 1
                else:
                    # Consider candidate mountains which have peak.
                    max_mountain_length = max(max_mountain_length, mountain_length)
                    before_peak, peak_found, mountain_length = False, False, 0

        if before_peak and peak_found:
            max_mountain_length = max(max_mountain_length, mountain_length)

        return max_mountain_length
