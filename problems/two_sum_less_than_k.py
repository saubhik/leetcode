from typing import List


class Solution:
    # Two Pointer Approach on Sorted Array.
    # Time Complexity: O(nlgn).
    # Space Complexity: O(n) (because of Tim Sort).
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        A.sort()

        left, right, max_sum = 0, len(A) - 1, 0
        while left < right:
            curr_sum = A[left] + A[right]

            if curr_sum >= K:
                right -= 1
            elif curr_sum < K:
                max_sum = max(max_sum, curr_sum)
                left += 1

        return max_sum if max_sum else -1
