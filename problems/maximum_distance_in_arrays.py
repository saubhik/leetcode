from typing import List


class Solution:
    """
    Example:
    [[1,2,3],[4,5],[1,2,3]]
    minimums = [1, 4, 1]
    maximums = [3, 5, 3]

    If index(min(minimums)) != index(max(maximums)), we are done: the answer is
    max(maximums) - min(minimums), since each is coming from a different array.

    Else, check the 2nd maximum with the min(minimums), and the 2nd minimum with the
    max(maximums): max(max(maximums) - min2(minimums), max2(maximums) - min(minimums)).

    Time Complexity: O(m) where m is the number of arrays.
    Space Complexity: O(1).
    """

    def maxDistance(self, arrays: List[List[int]]) -> int:
        min_minimums, max_maximums = 10_001, -10_001
        min2_minimums, max2_maximums = min_minimums, max_maximums
        min_idx, max_idx = -1, -1

        for i, array in enumerate(arrays):
            if array[0] < min_minimums:
                min2_minimums, min_minimums, min_idx = min_minimums, array[0], i
            elif array[0] < min2_minimums:
                min2_minimums = array[0]

            if array[-1] > max_maximums:
                max2_maximums, max_maximums, max_idx = max_maximums, array[-1], i
            elif array[-1] > max2_maximums:
                max2_maximums = array[-1]

        return (
            max_maximums - min_minimums
            if min_idx != max_idx
            else max(max_maximums - min2_minimums, max2_maximums - min_minimums)
        )
