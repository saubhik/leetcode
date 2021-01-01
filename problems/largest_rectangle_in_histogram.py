from typing import List
from unittest import TestCase


class Solution:
    # Gets TLEd.
    # Time Complexity: O(n^2).
    # Space Complexity: O(1).
    def largestRectangleArea(self, heights: List[int]) -> int:
        n, ans = len(heights), 0
        for i in range(n):
            count = 1

            for l in range(i - 1, -1, -1):
                if heights[l] < heights[i]:
                    break
                count += 1

            for r in range(i + 1, n):
                if heights[r] < heights[i]:
                    break
                count += 1

            ans = max(ans, count * heights[i])
        return ans


class SolutionTwo:
    # Using stack.
    # Time Complexity: O(n).
    #   Push n elements into stack and pop n elements from stack.
    # Space Complexity: O(n).
    def largestRectangleArea(self, heights: List[int]) -> int:
        n, stack, ans = len(heights), [-1], 0
        for i in range(n):
            while stack[-1] != -1 and heights[stack[-1]] > heights[i]:
                index = stack.pop()
                ans = max(ans, heights[index] * (i - 1 - stack[-1]))
            stack.append(i)

        while stack[-1] != -1:
            index = stack.pop()
            ans = max(ans, heights[index] * (n - 1 - stack[-1]))

        return ans


class SolutionThree:
    # Gets TLEd.
    # Divide and Conquer.
    # Time Complexity: O(nlgn); O(n^2) in worst case.
    # Space Complexity: O(n) for recursion stack space.
    def largestRectangleArea(self, heights: List[int]) -> int:
        def helper(left: int = 0, right: int = len(heights) - 1):
            if left > right:
                return 0

            min_height, min_index = float("inf"), -1
            for i in range(left, right + 1):
                if heights[i] < min_height:
                    min_height = heights[i]
                    min_index = i

            return max(
                helper(left=left, right=min_index - 1),
                heights[min_index] * (right - left + 1),
                helper(left=min_index + 1, right=right),
            )

        return helper()


class TestSolution(TestCase):
    def test_example_1(self):
        assert Solution().largestRectangleArea(heights=[2, 1, 5, 6, 2, 3]) == 10
        assert SolutionTwo().largestRectangleArea(heights=[2, 1, 5, 6, 2, 3]) == 10
        assert SolutionThree().largestRectangleArea(heights=[2, 1, 5, 6, 2, 3]) == 10
