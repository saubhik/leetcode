from typing import List


class Solution:
    # Time Complexity: O(n).
    # Space Complexity: O(1).
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)
        max_min_dist_from_neighbors = float("-inf")
        last_seated_pos = next_seated_pos = float("-inf")
        for pos in range(n):
            if seats[pos] == 0:
                if pos > next_seated_pos:
                    next_seated_pos = pos
                    while next_seated_pos < n and seats[next_seated_pos] == 0:
                        next_seated_pos += 1

                max_min_dist_from_neighbors = max(
                    max_min_dist_from_neighbors,
                    min(pos - last_seated_pos, next_seated_pos - pos)
                    if next_seated_pos != n
                    else pos - last_seated_pos,
                )
            else:
                last_seated_pos = pos
        return max_min_dist_from_neighbors
