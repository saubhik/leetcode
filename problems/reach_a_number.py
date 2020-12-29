from unittest import TestCase


class Solution:
    """
    This solution is exponential time and gets TLEd.
    """

    def reachNumber(self, target: int) -> int:
        def compute(source: int = 0, step: int = 0):
            if source == target:
                return 0

            step += 1

            # I can reach any target like this:
            # 0 -> -1 -> 1 -> -2 -> 2 -> -3 -> 3
            # 0 -> 1 -> -1 -> 2 -> -2
            if step >= 2 * abs(target):
                return float("inf")

            return 1 + min(
                compute(source=source - step, step=step),
                compute(source=source + step, step=step),
            )

        return compute()


class SolutionTwo:
    # Mathematical.
    # Time Complexity: O(sqrt(target)).
    # Space Complexity: O(1).
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        k, s = 1, 1  # s = 1 + ... + k.
        while s < target:
            k += 1
            s += k

        if s == target:
            return k

        delta = s - target
        if delta % 2 == 0:
            # We can find a subset of {1, ..., k} which sums to delta/2.
            # We can swap the +s to -s for those elements.
            return k

        # delta is odd. Add k+1 or k+2, as necessary, to make delta even.
        return k + 1 if (k % 2 == 0) else k + 2


class TestReachNumber(TestCase):
    def test_example_1(self):
        assert Solution().reachNumber(target=3) == 2
        assert SolutionTwo().reachNumber(target=3) == 2

    def test_example_2(self):
        assert Solution().reachNumber(target=2) == 3
        assert SolutionTwo().reachNumber(target=2) == 3

    def test_example_3(self):
        assert Solution().reachNumber(target=-1) == 1
        assert SolutionTwo().reachNumber(target=-1) == 1
