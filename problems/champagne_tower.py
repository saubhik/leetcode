class Solution:
    # Simulation.
    # When it is too mathy, try simulation!
    # Time Complexity: O(R^2) where R is the number of rows.
    # Space Complexity: O(R^2).
    # We can optimize the space to use only consider 2 rows at a time.
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        volume_in_glass = [[0] * k for k in range(1, 102)]
        volume_in_glass[0][0] = poured
        for row in range(query_row + 1):
            for col in range(row + 1):
                overflow = (volume_in_glass[row][col] - 1) / 2
                if overflow > 0:
                    volume_in_glass[row + 1][col] += overflow
                    volume_in_glass[row + 1][col + 1] += overflow
                    volume_in_glass[row][col] = 1
        return volume_in_glass[query_row][query_glass]
