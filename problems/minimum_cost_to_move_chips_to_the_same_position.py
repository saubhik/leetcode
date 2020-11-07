from typing import List


class Solution:
    # Time Complexity: O(n).
    # Space Complexity: O(1).
    def minCostToMoveChips(self, position: List[int]) -> int:
        even_chips = odd_chips = 0
        for pos in position:
            if pos % 2 == 0:
                even_chips += 1
            else:
                odd_chips += 1
        return min(odd_chips, even_chips)
