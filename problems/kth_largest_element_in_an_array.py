import heapq
import random
from typing import List
from unittest import TestCase


class Solution:
    # Heap.
    # Time Complexity: O(n lgk).
    # Space Complexity: O(k).
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # heap = []
        # for num in nums:
        #     if len(heap) < k:
        #         heapq.heappush(heap, num)
        #     else:
        #         heapq.heappushpop(heap, num)
        # return heapq.heappop(heap)
        return heapq.nlargest(k, nums)[-1]


class SolutionTwo:
    # Use QuickSelect.
    # Time Complexity: O(n) in average case, O(n^2) worst case.
    # Space Complexity: O(1).
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)

        def quick_select(left: int, right: int):
            # Lomuto Partition Scheme
            pivot_idx = random.randint(left, right)
            pivot = nums[pivot_idx]
            nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]
            store_index = left
            for i in range(left, right):
                if nums[i] <= pivot:
                    nums[store_index], nums[i] = nums[i], nums[store_index]
                    store_index += 1
            nums[right], nums[store_index] = nums[store_index], nums[right]

            if store_index == n - k:
                return pivot
            elif store_index > n - k:
                return quick_select(left=left, right=store_index - 1)
            else:
                return quick_select(left=store_index + 1, right=right)

        return quick_select(left=0, right=n - 1)


class TestFindKthLargest(TestCase):
    def test_example_1(self):
        assert Solution().findKthLargest(nums=[3, 2, 1, 5, 6, 4], k=2) == 5
        assert SolutionTwo().findKthLargest(nums=[3, 2, 1, 5, 6, 4], k=2) == 5

    def test_example_2(self):
        assert Solution().findKthLargest(nums=[3, 2, 3, 1, 2, 4, 5, 5, 6], k=4) == 4
        assert SolutionTwo().findKthLargest(nums=[3, 2, 3, 1, 2, 4, 5, 5, 6], k=4) == 4
