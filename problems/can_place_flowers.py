from typing import List


class Solution:
    # Greedy. One Pass.
    # Time Complexity: O(n).
    # Space Complexity: O(1).
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True

        n_plots = len(flowerbed)
        count = 0
        for i in range(n_plots):
            if (
                flowerbed[i] == 0
                and (i == 0 or flowerbed[i - 1] == 0)
                and (i == n_plots - 1 or flowerbed[i + 1] == 0)
            ):
                count += 1
                flowerbed[i] = 1
                if count == n:
                    return True
        return False
