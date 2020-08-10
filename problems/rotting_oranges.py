from typing import List


class Solution:
    # Time: O(N), where N is size of input grid
    # Space: O(N), where N is size of input grid
    # Worst case: each orange in each cell of grid is rotten
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minutes = 0
        oranges_count = 0
        sources = []

        rows, cols = len(grid), len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    sources.append((i, j))
                if grid[i][j] != 0:
                    oranges_count += 1

        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        current_sources = sources
        while current_sources:
            next_sources = []
            for row, col in current_sources:
                oranges_count -= 1
                for d in directions:
                    nbr_row, nbr_col = row + d[0], col + d[1]
                    if 0 <= nbr_row < rows and 0 <= nbr_col < cols:
                        if grid[nbr_row][nbr_col] == 1:
                            grid[nbr_row][nbr_col] = 2
                            next_sources.append((nbr_row, nbr_col))
            if next_sources:
                minutes += 1
            current_sources = next_sources

        return minutes if oranges_count == 0 else -1


class SolutionTwo:
    # in-place algorithm
    # Constant space. O(1).
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(-1, 0), (0, 1), (0, -1), (1, 0)]
        timestamp = 2
        continue_bfs = True
        while continue_bfs:
            continue_bfs = False
            for row in range(rows):
                for col in range(cols):
                    if grid[row][col] == timestamp:
                        for d in directions:
                            nbr_row, nbr_col = row + d[0], col + d[1]
                            if 0 <= nbr_row < rows and 0 <= nbr_col < cols:
                                if grid[nbr_row][nbr_col] == 1:
                                    grid[nbr_row][nbr_col] = timestamp + 1
                                    continue_bfs = True
            if continue_bfs:
                timestamp += 1

        # fresh oranges left
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    return -1

        return timestamp - 2
