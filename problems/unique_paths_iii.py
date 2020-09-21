from typing import List


class Solution:
    # We have the following grid:
    # 1, 0, 0,  0
    # 0, 0, 0,  0
    # 0, 0, 2, -1
    # Walk over every non-obstacle square exactly once.
    #
    # 1, 0, 0, 0
    # 0, 0, 0, 0
    # 0, 0, 0, 2
    #
    # Straight Forward DFS.
    # Time: O(4 ^ (r * c)), exponential time.
    # Space: O(r * c)
    # where r and c are the number of rows or columns.
    #
    # Since r * c <= 20, this solution is accepted.
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        rows, cols, paths, visited, num_valid_squares, start_i, start_j = (
            len(grid),
            len(grid[0]),
            0,
            set(),
            0,
            None,
            None,
        )

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] in (0, 1):
                    num_valid_squares += 1
                    if grid[i][j] == 1:
                        start_i, start_j = i, j

        def dfs(i, j):
            if grid[i][j] == 2:
                if len(visited) == num_valid_squares:
                    nonlocal paths
                    paths += 1

                return

            visited.add((i, j))

            for dir in ((1, 0), (0, -1), (-1, 0), (0, 1)):
                nbr_i, nbr_j = i + dir[0], j + dir[1]
                if (
                    0 <= nbr_i < rows
                    and 0 <= nbr_j < cols
                    and grid[nbr_i][nbr_j] != -1
                    and (nbr_i, nbr_j) not in visited
                ):
                    dfs(i=nbr_i, j=nbr_j)

            visited.remove((i, j))

        dfs(i=start_i, j=start_j)

        return paths
