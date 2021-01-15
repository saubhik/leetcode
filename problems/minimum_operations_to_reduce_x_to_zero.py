from typing import List
from unittest import TestCase


class Solution:
    # Either remove the left or right from nums, and subtract from x.
    # Minimum number of operations to reduce x to 0. Otherwise, return -1.
    #
    # nums=[1,1,4,2,3],x=5
    # Choose 3 or 1? Depends on what's next.
    # dp[i][j][x]=min(1+dp[i+1][j][x-nums[i]],1+dp[i][j+1][x-nums[j]])
    # But this gets TLEd.
    def minOperations(self, nums: List[int], x: int) -> int:
        def _recurse(i: int, j: int, x: int):
            if x == 0:
                return 0
            if i > j or x < 0:
                return float("inf")
            return 1 + min(
                _recurse(i=i + 1, j=j, x=x - nums[i]),
                _recurse(i=i, j=j - 1, x=x - nums[j]),
            )

        ans = _recurse(i=0, j=len(nums) - 1, x=x)
        return -1 if ans == float("inf") else ans


class SolutionTwo:
    """
    Find the maximum length subarray with sum = sum(nums) - x.
    Maximum length subarray with sum 6 in [1,1,4,2,3]:
    Two pointers: i and j initially points to 0.
    Consider window represented by i and j.
    So,
        Increase right pointer if window sum is less than target.
        Increase left pointer if window sum is greater than target.
        Increase both if window sum == target, and track the window length.
    """

    def minOperations(self, nums: List[int], x: int) -> int:
        n, target = len(nums), sum(nums) - x

        if target == 0:
            return n

        i, j, window_sum, max_subarray_len = 0, 0, nums[0], 0
        while i < n and j < n:
            if window_sum < target:
                # Expand window.
                j += 1
                if j == n:  # No point in continuing further.
                    break
                window_sum += nums[j]
            else:
                # Shrink window.
                window_sum -= nums[i]
                i += 1

            if window_sum == target:
                max_subarray_len = max(max_subarray_len, j - i + 1)

        return -1 if max_subarray_len == 0 else n - max_subarray_len


class TestMinOperations(TestCase):
    def test_example_1(self):
        assert Solution().minOperations(nums=[1, 1, 4, 2, 3], x=5) == 2
        assert SolutionTwo().minOperations(nums=[1, 1, 4, 2, 3], x=5) == 2

    def test_example_2(self):
        assert Solution().minOperations(nums=[5, 6, 7, 8, 9], x=4) == -1
        assert SolutionTwo().minOperations(nums=[5, 6, 7, 8, 9], x=4) == -1

    def test_example_3(self):
        assert Solution().minOperations(nums=[3, 2, 20, 1, 1, 3], x=10) == 5
        assert SolutionTwo().minOperations(nums=[3, 2, 20, 1, 1, 3], x=10) == 5

    def test_example_4(self):
        assert (
            Solution().minOperations(
                nums=[
                    8828,
                    9581,
                    49,
                    9818,
                    9974,
                    9869,
                    9991,
                    10000,
                    10000,
                    10000,
                    9999,
                    9993,
                    9904,
                    8819,
                    1231,
                    6309,
                ],
                x=134365,
            )
            == 16
        )
        assert (
            SolutionTwo().minOperations(
                nums=[
                    8828,
                    9581,
                    49,
                    9818,
                    9974,
                    9869,
                    9991,
                    10000,
                    10000,
                    10000,
                    9999,
                    9993,
                    9904,
                    8819,
                    1231,
                    6309,
                ],
                x=134365,
            )
            == 16
        )
