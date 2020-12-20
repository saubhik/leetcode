from typing import List
from unittest import TestCase


class Solution:
    # Dynamic Programming (Top Down) with Memoization.
    # Time Complexity: O(M*N*N).
    # Space Complexity: O(M*N*N).
    def cherryPickup(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        # O(M*N*N) space.
        cache = [
            [[None for _ in range(cols)] for _ in range(cols)] for _ in range(rows)
        ]

        def compute(row: int, col1: int, col2: int):
            if cache[row][col1][col2]:
                return cache[row][col1][col2]

            current_cherries = (
                grid[row][col1] + grid[row][col2] if col1 != col2 else grid[row][col1]
            )

            if row == rows - 1:
                return current_cherries

            ans = -1
            for next_col1 in (col1 - 1, col1, col1 + 1):
                if 0 <= next_col1 < cols:
                    for next_col2 in (col2 - 1, col2, col2 + 1):
                        if 0 <= next_col2 < cols:
                            ans = max(
                                ans,
                                compute(row=row + 1, col1=next_col1, col2=next_col2),
                            )

            ans += current_cherries
            cache[row][col1][col2] = ans
            return ans

        return compute(row=0, col1=0, col2=cols - 1)


class SolutionTwo:
    # Dynamic Programming (Bottom Up) with State Compression.
    # Since dp[row][col1][col2] depends only on dp[row+1][...][...], we do not need to
    # store the row dimension. This is state compression.
    # Time Complexity: O(M*N^2).
    # Space Complexity: O(N^2).
    def cherryPickup(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dp = [[-1 for _ in range(cols)] for _ in range(cols)]

        for col1 in range(cols):
            for col2 in range(cols):
                dp[col1][col2] = (
                    grid[rows - 1][col1] + grid[rows - 1][col2]
                    if col1 != col2
                    else grid[rows - 1][col1]
                )

        for row in range(rows - 2, -1, -1):
            tmp = [[-1 for _ in range(cols)] for _ in range(cols)]
            for col1 in range(cols):
                for col2 in range(cols):
                    for c1 in (col1 - 1, col1, col1 + 1):
                        if 0 <= c1 < cols:
                            for c2 in (col2 - 1, col2, col2 + 1):
                                if 0 <= c2 < cols:
                                    tmp[col1][col2] = max(tmp[col1][col2], dp[c1][c2])
                    tmp[col1][col2] += (
                        grid[row][col1] + grid[row][col2]
                        if col1 != col2
                        else grid[row][col1]
                    )
            dp = tmp

        return dp[0][cols - 1]


class TestCherryPickup(TestCase):
    def test_example_1(self):
        assert (
            Solution().cherryPickup(grid=[[3, 1, 1], [2, 5, 1], [1, 5, 5], [2, 1, 1]])
            == 24
        )
        assert (
            SolutionTwo().cherryPickup(
                grid=[[3, 1, 1], [2, 5, 1], [1, 5, 5], [2, 1, 1]]
            )
            == 24
        )

    def test_example_2(self):
        assert (
            Solution().cherryPickup(
                grid=[
                    [1, 0, 0, 0, 0, 0, 1],
                    [2, 0, 0, 0, 0, 3, 0],
                    [2, 0, 9, 0, 0, 0, 0],
                    [0, 3, 0, 5, 4, 0, 0],
                    [1, 0, 2, 3, 0, 0, 6],
                ]
            )
            == 28
        )
        assert (
            SolutionTwo().cherryPickup(
                grid=[
                    [1, 0, 0, 0, 0, 0, 1],
                    [2, 0, 0, 0, 0, 3, 0],
                    [2, 0, 9, 0, 0, 0, 0],
                    [0, 3, 0, 5, 4, 0, 0],
                    [1, 0, 2, 3, 0, 0, 6],
                ]
            )
            == 28
        )

    def test_example_3(self):
        assert (
            Solution().cherryPickup(
                grid=[[1, 0, 0, 3], [0, 0, 0, 3], [0, 0, 3, 3], [9, 0, 3, 3]]
            )
            == 22
        )
        assert (
            SolutionTwo().cherryPickup(
                grid=[[1, 0, 0, 3], [0, 0, 0, 3], [0, 0, 3, 3], [9, 0, 3, 3]]
            )
            == 22
        )

    def test_example_4(self):
        assert Solution().cherryPickup(grid=[[1, 1], [1, 1]]) == 4
        assert SolutionTwo().cherryPickup(grid=[[1, 1], [1, 1]]) == 4
