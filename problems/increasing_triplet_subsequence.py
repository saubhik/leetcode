from typing import List
from unittest import TestCase


class Solution:
    """
    2, 1, 5, 0, 3, 4
    [1, 5], count=2
    [0, 3, 4], count=3
    New increasing subsequence can start. How do I give space to it in O(1) memory?
    The number at position i can extend the sequence whose last number < nums[i].
    I need to store the last number & count of all increasing sequences so far.
    2 -> [2], count=1
    1 -> 1 < 2, so no need to store 2, [1], count=1
    5 -> 5 > 1, so we extend existing sequence, [1, 5], count=2
    0 -> 0 < 5, 0 < 1, so we create a new sequence [0], count=1
    3 -> 3 < 5, 3 > 1, & 3 > 0 so [1,3],count=2 & [0,3],count=2.
    We can remove one of them.
    I need only 3 variables.
    [1,5]
    [0,]
    """

    def increasingTriplet(self, nums: List[int]) -> bool:
        a = b = c = None
        for num in nums:
            if a is None:
                a = num
            else:
                if b is None:
                    if num <= a:
                        a = num
                    else:
                        b = num
                else:
                    if b < num:
                        return True
                    elif a < num < b:
                        b = num
                    if c is None:
                        if num < a:
                            c = num
                    else:
                        if num < c:
                            c = num
                        elif c < num < a:
                            a, b, c = c, num, None
        return False


class SolutionTwo:
    """
    Linear Scan with only 2 variables.
    "first_min" & "second_min".
    "second_min" is always greater than some historical value of "first_min".
    If a number is greater than the "second_min", then we have an increasing triplet.
    """

    def increasingTriplet(self, nums: List[int]) -> bool:
        first_min = second_min = float("inf")
        for num in nums:
            if num <= first_min:
                first_min = num
            elif num <= second_min:
                second_min = num
            else:
                return True
        return False


class TestIncreasingTriplet(TestCase):
    def test_example_1(self):
        assert Solution().increasingTriplet(nums=[1, 2, 3, 4, 5]) is True
        assert SolutionTwo().increasingTriplet(nums=[1, 2, 3, 4, 5]) is True

    def test_example_2(self):
        assert Solution().increasingTriplet(nums=[5, 4, 3, 2, 1]) is False
        assert SolutionTwo().increasingTriplet(nums=[5, 4, 3, 2, 1]) is False

    def test_example_3(self):
        assert Solution().increasingTriplet(nums=[2, 1, 5, 0, 4, 6]) is True
        assert SolutionTwo().increasingTriplet(nums=[2, 1, 5, 0, 4, 6]) is True
