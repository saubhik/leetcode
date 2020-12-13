from collections import Counter, defaultdict
from typing import List
from unittest import TestCase


class Solution:
    # Using Counter hash map.
    # Time Complexity: O(n).
    # Space Complexity: O(n) in worst case.
    def maxOperations(self, nums: List[int], k: int) -> int:
        n, counter, count = len(nums), Counter(nums), 0
        for num in nums:
            if counter[k - num] > 0 and counter[num] > 0:
                if num == k - num and counter[num] == 1:
                    continue
                count += 1
                counter[num] -= 1
                counter[k - num] -= 1
        return count


class SolutionTwo:
    # One-Pass using a Counter hash-map.
    # Time Complexity: O(n).
    # Space Complexity: O(n).
    def maxOperations(self, nums: List[int], k: int) -> int:
        counter, count = defaultdict(int), 0
        for num in nums:
            if counter[k - num] > 0:
                counter[k - num] -= 1
                count += 1
            else:
                counter[num] += 1
        return count


class SolutionThree:
    # Two Pointers Using Sort.
    # Time Complexity: O(nlgn).
    # Space Complexity: O(n), due to Python's sort implementation.
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        left, right, count = 0, len(nums) - 1, 0
        while left < right:
            curr_sum = nums[left] + nums[right]
            if curr_sum > k:
                right -= 1
            elif curr_sum < k:
                left += 1
            else:
                # curr_sum == k
                count += 1
                left += 1
                right -= 1
        return count


class TestSolution(TestCase):
    def test_example_1(self):
        assert Solution().maxOperations(nums=[1, 2, 3, 4], k=5) == 2
        assert SolutionTwo().maxOperations(nums=[1, 2, 3, 4], k=5) == 2
        assert SolutionThree().maxOperations(nums=[1, 2, 3, 4], k=5) == 2

    def test_example_2(self):
        assert Solution().maxOperations(nums=[3, 1, 3, 4, 3], k=6) == 1
        assert SolutionTwo().maxOperations(nums=[3, 1, 3, 4, 3], k=6) == 1
        assert SolutionThree().maxOperations(nums=[3, 1, 3, 4, 3], k=6) == 1

    def test_example_3(self):
        assert (
            Solution().maxOperations(
                nums=[2, 5, 4, 4, 1, 3, 4, 4, 1, 4, 4, 1, 2, 1, 2, 2, 3, 2, 4, 2], k=3
            )
            == 4
        )
        assert (
            SolutionTwo().maxOperations(
                nums=[2, 5, 4, 4, 1, 3, 4, 4, 1, 4, 4, 1, 2, 1, 2, 2, 3, 2, 4, 2], k=3
            )
            == 4
        )
        assert (
            SolutionThree().maxOperations(
                nums=[2, 5, 4, 4, 1, 3, 4, 4, 1, 4, 4, 1, 2, 1, 2, 2, 3, 2, 4, 2], k=3
            )
            == 4
        )
