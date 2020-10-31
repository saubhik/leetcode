from typing import List


class Solution:
    # 1,3,5,4,7
    # Suppose for sequences ending at i, we knew the length of the longest subsequence,
    # length[i], and the count of such sequences, count[i].
    # nums    1,3,5,4,7
    # length  1,2,3,3,4
    # count   1,1,1,2,2
    #
    # Time Complexity: O(n**2)
    # Space Complexity: O(n)
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 0:
            return 0

        # Length of longest subsequence ending in nums[i].
        length = [1] * n
        # Count of the number of longest subsequences ending with nums[i].
        count = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    new_length = length[j] + 1
                    if new_length > length[i]:
                        length[i], count[i] = new_length, count[j]
                    elif new_length == length[i]:
                        count[i] += count[j]

        lis_length = max(length)
        ans = 0
        for i in range(n):
            if length[i] == lis_length:
                ans += count[i]

        return ans
