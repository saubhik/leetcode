from collections import defaultdict
from typing import List


class Solution:
    # prefix sum technique: prefixSum & hashMap
    # O(n) time, O(n) additional space.
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = 0
        count = 0
        seenCount = defaultdict(int)
        for num in nums:
            prefixSum += num
            if prefixSum == k:
                count += 1
            count += seenCount[prefixSum - k]
            seenCount[prefixSum] += 1
        return count
