from typing import List


class Solution:
    def checkArithmeticSubarrays(
        self, nums: List[int], l: List[int], r: List[int]
    ) -> List[bool]:
        q = len(l)
        ans = []
        for i in range(q):
            subarray = sorted(nums[l[i] : r[i] + 1])
            diff = subarray[1] - subarray[0]
            is_arithmetic = True
            for j in range(1, r[i] - l[i] + 1):
                if subarray[j] - subarray[j - 1] != diff:
                    is_arithmetic = False
                    break
            ans.append(is_arithmetic)
        return ans
