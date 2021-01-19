from typing import List
from unittest import TestCase


class Solution:
    # Straight Forward DFS.
    # Time Complexity: O(mn).
    # Space Complexity: O(mn).
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]

        def explore(row: int, col: int):
            if not 0 <= row < m or not 0 <= col < n or visited[row][col]:
                return

            visited[row][col] = True

            if grid[row][col] == "0":
                return

            explore(row=row, col=col + 1)
            explore(row=row + 1, col=col)
            explore(row=row, col=col - 1)
            explore(row=row - 1, col=col)

        for row in range(m):
            for col in range(n):
                if not visited[row][col] and grid[row][col] == "1":
                    ans += 1
                    explore(row=row, col=col)

        return ans


class TestNumIslands(TestCase):
    def test_example_1(self):
        assert (
            Solution().numIslands(
                grid=[
                    ["1", "1", "1", "1", "0"],
                    ["1", "1", "0", "1", "0"],
                    ["1", "1", "0", "0", "0"],
                    ["0", "0", "0", "0", "0"],
                ]
            )
            == 1
        )

    def test_example_2(self):
        assert (
            Solution().numIslands(
                grid=[
                    ["1", "1", "0", "0", "0"],
                    ["1", "1", "0", "0", "0"],
                    ["0", "0", "1", "0", "0"],
                    ["0", "0", "0", "1", "1"],
                ]
            )
            == 3
        )

    def test_example_3(self):
        assert Solution().numIslands(grid=[["1", "0", "1", "1", "0", "1", "1"]]) == 3
