from typing import List
from unittest import TestCase


class Solution:
    # Using HashMap like TwoSum.
    # Time Complexity: O(n).
    # Space Complexity: O(1) since keys of hashmap are 0, 1, ..., 59.
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count = 0
        counter = dict()
        for num in time:
            num %= 60
            if num == 0 and 0 in counter:
                count += counter[0]
            elif 60 - num in counter:
                count += counter[60 - num]
            counter[num] = counter.get(num, 0) + 1
        return count


class TestNumPairsDivisibleBy60(TestCase):
    def test_example_1(self):
        """
        30, 20, 30, 40, 40
        """
        assert Solution().numPairsDivisibleBy60(time=[30, 20, 150, 100, 40]) == 3

    def test_example_2(self):
        assert Solution().numPairsDivisibleBy60(time=[60, 60, 60]) == 3
