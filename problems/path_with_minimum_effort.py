from typing import List
from unittest import TestCase


class Solution:
    """
    Binary Search with DFS.

    Efforts are from 0 to 10^6.
    Given an effort, I can check if there is a path with that effort from top
    left to bottom right. This can be done in O(mn) time using graph search.

    If effort e leads to a solution, we explore efforts in [0, e).
    If effort e does not lead to a solution, we explore efforts in (e, 10^6].

    Time Complexity: O(mn).
    Space Complexity: O(mn).
    """

    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])

        min_height = min([min(heights[i]) for i in range(m)])
        max_height = max([max(heights[i]) for i in range(m)])

        # Check if reachable using DFS.
        def searchWithEffort(effort, i=0, j=0, visited=None):
            if not visited:
                visited = [[False] * n for _ in range(m)]

            if i == m - 1 and j == n - 1:
                return True

            visited[i][j] = True

            for di, dj in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
                newi, newj = i + di, j + dj
                if 0 <= newi < m and 0 <= newj < n and not visited[newi][newj]:
                    if abs(heights[newi][newj] - heights[i][j]) <= effort:
                        if searchWithEffort(
                            i=newi, j=newj, effort=effort, visited=visited
                        ):
                            return True

            return False

        # Use Binary Search over efforts.
        lo, hi = 0, max_height - min_height
        while lo < hi:
            mid = hi - (hi - lo) // 2
            if searchWithEffort(effort=mid):
                hi = mid - 1
            else:
                lo = mid + 1

        return lo if searchWithEffort(effort=lo) else lo + 1


class TestSolution(TestCase):
    def test_example_1(self):
        heights = [[1, 2, 2], [3, 8, 2], [5, 3, 5]]
        assert Solution().minimumEffortPath(heights=heights) == 2

    def test_example_2(self):
        heights = [[1, 2, 3], [3, 8, 4], [5, 3, 5]]
        assert Solution().minimumEffortPath(heights=heights) == 1

    def test_example_3(self):
        heights = [
            [1, 2, 1, 1, 1],
            [1, 2, 1, 2, 1],
            [1, 2, 1, 2, 1],
            [1, 2, 1, 2, 1],
            [1, 1, 1, 2, 1],
        ]
        assert Solution().minimumEffortPath(heights=heights) == 0
