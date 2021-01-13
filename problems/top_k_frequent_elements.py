from collections import Counter
from heapq import heappop, heappush, heappushpop, nlargest
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Runtime: 104 ms, faster than 79.04% of Python3 online submissions for Top K
        # Frequent Elements. Memory Usage: 18.2 MB, less than 72.14% of Python3
        # online submissions for Top K Frequent Elements.

        counts = Counter(nums)
        heap = list()
        for num, count in counts.items():
            if len(heap) >= k:
                heappushpop(heap, (count, num))
            else:
                heappush(heap, (count, num))

        result = list()
        while heap:
            result.append(heappop(heap)[1])

        return result

    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
        # Runtime: 88 ms, faster than 99.79% of Python3 online submissions for Top K
        # Frequent Elements. Memory Usage: 18.2 MB, less than 72.90% of Python3
        # online submissions for Top K Frequent Elements.

        # Note how we speed up the worst case complexity

        if k == len(nums):  # O(1) time instead of O(N log N) time
            return nums

        counts = Counter(nums)  # O(N) time
        return nlargest(k, counts, key=counts.get)  # O(N log K) time
