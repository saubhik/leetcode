from typing import List
from unittest import TestCase


class Solution:
    """
    Can using the same array benefit us?
    nums=[1,0,-1,0,-2,2],target=0
    [[1,0,-1,0],[1,-1,-2,2],[0,0,-2,2]]
    1. Consider i=0. Consider (nums[i=1...],target=-1,level=2).
    2. Consider i=1. Consider (nums[i=2...],target=-1,level=3).
    3. Consider i=2. Consider (nums[i=3...],target=0,level=4).
    4. Consider i=3. Return.
    """

    # This gets TLEd.
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n, ans = len(nums), set()

        # Time Complexity: O(n^4).
        # Recursion stack depth is at max 4 units. So O(1) space.
        def recurse(pos: int, target: int, curr: List[int]):
            if len(curr) == 4:
                if target == 0:
                    ans.add(tuple(sorted(curr)))
                return

            for i in range(pos, n):
                recurse(
                    pos=i + 1, target=target - nums[i], curr=curr + [nums[i]],
                )

        recurse(pos=0, target=target, curr=[])
        return list(map(list, ans))


class SolutionTwo:
    """
    How will you solve 3Sum?
    nums=[-1,0,1,2,-1,-4].
    Sort nums.
    -4,-1,-1,0,1,2
     ^  ^        ^
    For each element, check 2Sum.
    -1,-1,0,1,2, target=4
            ^ ^
    We can use a hashset to solve 2Sum also.
    2Sum can be done in linear time.
    So kSum can be done in O(n^(k-1)) time.
    """

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        return self.kSum(k=4, nums=nums, target=target)

    # O(n^(k-1)) time, O(n) space for sorting/recursion stack/hashset.
    def kSum(self, k: int, nums: List[int], target: int) -> List[List[int]]:
        n, ans = len(nums), []

        nums.sort()

        # O(n) time, O(n) space.
        def twoSum(pos: int, target: int, curr: List[int]):
            s, last_added = set(), None
            for i in range(pos, n):
                if target - nums[i] in s and nums[i] != last_added:
                    last_added = nums[i]
                    ans.append(curr + [target - nums[i], nums[i]])
                s.add(nums[i])

        def recurse(pos: int, target: int, curr: List[int]):
            if len(curr) == k - 2:
                twoSum(pos=pos, target=target, curr=curr)
                return

            last_added = None
            for i in range(pos, n):
                if nums[i] != last_added:
                    last_added = nums[i]
                    recurse(pos=i + 1, target=target - nums[i], curr=curr + [nums[i]])

        recurse(pos=0, target=target, curr=[])
        return ans


class TestFourSum(TestCase):
    def test_example_1(self):
        assert Solution().fourSum(nums=[1, 0, -1, 0, -2, 2], target=0) == [
            [-1, 0, 0, 1],
            [-2, 0, 0, 2],
            [-2, -1, 1, 2],
        ]
        assert SolutionTwo().fourSum(nums=[1, 0, -1, 0, -2, 2], target=0) == [
            [-2, -1, 1, 2],
            [-2, 0, 0, 2],
            [-1, 0, 0, 1],
        ]

    def test_example_2(self):
        assert Solution().fourSum(nums=[], target=0) == []
        assert SolutionTwo().fourSum(nums=[], target=0) == []

    def test_example_3(self):
        assert Solution().fourSum(nums=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], target=0) == [
            [0, 0, 0, 0]
        ]
        assert SolutionTwo().fourSum(nums=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], target=0) == [
            [0, 0, 0, 0]
        ]
