from typing import List
from unittest import TestCase


class Solution:
    # Two Pointer with One Pass.
    # Time Complexity: O(n).
    # Space Complexity: O(1).
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        curr, ans = lower, []
        for i in range(len(nums)):
            if nums[i] > curr:
                if curr == nums[i] - 1:
                    ans.append(f"{curr}")
                else:
                    ans.append(f"{curr}->{nums[i]-1}")
                curr = nums[i] + 1
            elif nums[i] == curr:
                curr += 1
        if curr == upper:
            ans.append(f"{curr}")
        elif curr < upper:
            ans.append(f"{curr}->{upper}")
        return ans


class TestSolution(TestCase):
    def test_example_1(self):
        assert Solution().findMissingRanges(
            nums=[0, 1, 3, 50, 75], lower=0, upper=99
        ) == ["2", "4->49", "51->74", "76->99"]

    def test_example_2(self):
        assert Solution().findMissingRanges(nums=[], lower=1, upper=1) == ["1"]

    def test_example_3(self):
        assert Solution().findMissingRanges(nums=[], lower=-3, upper=-1) == ["-3->-1"]

    def test_example_4(self):
        assert Solution().findMissingRanges(nums=[-1], lower=-1, upper=-1) == []

    def test_example_5(self):
        assert Solution().findMissingRanges(nums=[-1], lower=-2, upper=-1) == ["-2"]
