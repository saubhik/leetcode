from typing import List


class Solution:
    # Time Complexity: O(n).
    # Space Complexity: O(1).
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        n = len(nums)

        if n == 0:
            return ans

        curr_start = curr_end = -1
        for i in range(n):
            if i == 0:
                curr_start = curr_end = nums[i]
                continue

            if nums[i] == curr_end + 1:
                curr_end = nums[i]
            else:
                if curr_start == curr_end:
                    ans.append(f"{curr_start}")
                else:
                    ans.append(f"{curr_start}->{curr_end}")

                curr_start = curr_end = nums[i]

        last_str = (
            f"{curr_start}->{curr_end}" if curr_start != curr_end else f"{curr_start}"
        )
        if not ans or last_str != ans[-1]:
            ans.append(last_str)

        return ans
