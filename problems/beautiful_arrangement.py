from unittest import TestCase


class Solution:
    # Examples:
    #     n=3
    #     1,2,3
    #     perm[i] is divisible by i.
    #     i is divisible by perm[i].
    #     There is at least 1 beautiful arrangement: 1, ..., n.
    #     Consider the reverse: 3, 2, 1. This is also beautiful.
    #     1, 3, 2 or 2, 3, 1 is not beautiful.
    #     4, 3, 2, 1 is not beautiful.
    #     1, 2, 3, 4 is beautiful.
    #     1, 4, 3, 2 is beautiful.
    #     3, 4, 1, 2 is beautiful.
    #     3, 1, 2, 4 is not beautiful.
    # ith place will have multiples or factors of i.
    # Consider each factor or multiple of i and build up answer.
    # Backtracking solution.
    #
    # Time Complexity: O(n!) but pruned.
    # Space Complexity: O(n) due to recursion stack.
    def countArrangement(self, n: int) -> int:
        visited, count = 0, 0

        def backtrack(pos: int = 1):
            nonlocal visited, count

            if pos == n + 1:
                count += 1

            for i in range(1, n + 1):
                mask = 1 << i - 1
                if visited & mask == 0 and (i % pos == 0 or pos % i == 0):
                    visited ^= mask
                    backtrack(pos=pos + 1)
                    visited ^= mask

        backtrack()
        return count


class TestCountArrangement(TestCase):
    def test_example_1(self):
        assert Solution().countArrangement(n=2) == 2

    def test_example_2(self):
        assert Solution().countArrangement(n=1) == 1
