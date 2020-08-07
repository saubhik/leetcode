from collections import defaultdict
from typing import List


class Solution:
    # This is O(n) time, O(n) space.
    def findDuplicates(self, nums: List[int]) -> List[int]:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1

        result = []
        for key, value in counts.items():
            if value == 2:
                result.append(key)
        return result


class SolutionTwo:
    # O(n) time, O(1) space
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        for num in nums:
            _idx = abs(num) - 1
            if nums[_idx] < 0:
                result.append(_idx + 1)
            else:
                nums[_idx] *= -1
        return result
