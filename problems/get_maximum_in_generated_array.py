from unittest import TestCase


class Solution:
    """
    Straight Forward Linear Scan.
    Time Complexity: O(n).
    Space Complexity: O(n).
    """

    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0

        if n == 1:
            return 1

        nums, d, max_num = [0, 1], 1, 1
        for i in range(2, n + 1):
            _tmp = nums[d]
            if i & 1:
                _tmp += nums[d + 1]
                if _tmp > max_num:
                    max_num = _tmp
                d += 1
            nums.append(_tmp)

        return max_num


class TestGetMaximumGenerated(TestCase):
    def test_example_1(self):
        assert Solution().getMaximumGenerated(n=7) == 3

    def test_example_2(self):
        assert Solution().getMaximumGenerated(n=2) == 1

    def test_example_3(self):
        assert Solution().getMaximumGenerated(n=3) == 2
