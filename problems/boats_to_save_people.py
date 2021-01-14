from typing import List
from unittest import TestCase


class Solution:
    """
    Greedy with Two Pointers.
    Time Complexity: O(nlgn).
    Space Complexity: O(n) (space for Python sort).

    Minimum number of pairs whose sum is at most limit.

    Example:
    [1,2,2,3]
    Sort them.
    If heaviest person can pair with lightest person, go ahead.
    Otherwise, heaviest person goes alone.
    (3) goes alone.
    (1,2) goes.
    (2) goes alone.
    """

    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        lo, hi = 0, len(people) - 1
        count = 0
        while lo < hi:
            if people[lo] + people[hi] <= limit:
                # Pair them up.
                count += 1
                lo += 1
                hi -= 1
            else:
                # Heavy person goes alone.
                count += 1
                hi -= 1

        if lo == hi:
            count += 1

        return count


class TestNumRescueBoats(TestCase):
    def test_example_1(self):
        assert Solution().numRescueBoats(people=[1, 2], limit=3) == 1

    def test_example_2(self):
        assert Solution().numRescueBoats(people=[3, 2, 2, 1], limit=3) == 3

    def test_example_3(self):
        assert Solution().numRescueBoats(people=[3, 5, 3, 4], limit=5) == 4
