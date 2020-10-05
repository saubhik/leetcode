from functools import cmp_to_key
from typing import List


class Solution:
    """
    [[1,4],[3,6],[2,8]]
    Sort them based on ascending left end points, and then by descending right end
    points to get:
        [[1,4],[2,8],[3,6]]
    Start walking the array.
    If the current right end point is <= maximum of left end points so far.

    If an interval on left [li, lj] is covered by interval on right [ri, rj]:
        1. ri <= li and lj <= rj by definition of cover.
        2. li <= ri by sorting order. So, li == ri.
        3. But by sorting order, we have lj >= rj if li == ri. So, lj == rj.
        4. But intervals are distinct. Contradiction.
    So, an interval on left cannot be covered by interval on right. QED.

    This algorithm matches with the Official Solution!

    == Complexity Analysis ==
    - Time Complexity: O(n lgn).
    - Space Complexity: O(n) in Python, O(lgn) in Java.
    - The space complexity of the sorting algorithm depends on the implementation
        of each programming language.
    - For instance, the `sorted()` function in Python is implemented with the
        Timsort algorithm whose space complexity is O(n).
    - In Java, the Arrays.sort() is implemented as a variant of quicksort algorithm
        whose space complexity is O(lgN).
    """

    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        # def cmp(interval1, interval2):
        #     left1, right1 = interval1
        #     left2, right2 = interval2
        #
        #     if left1 < left2:
        #         return -1
        #     elif left1 > left2:
        #         return 1
        #     elif right1 < right2:
        #         return 1
        #     elif right1 > right2:
        #         return -1
        #     else:
        #         return 0
        #
        # intervals.sort(key=cmp_to_key(cmp))
        intervals.sort(key=lambda x: (+x[0], -x[1]))

        # 0 <= intervals[i][0] < intervals[i][1] <= 10^5
        max_right, ans = -1, 0

        for left, right in intervals:
            if right > max_right:
                ans += 1
            max_right = max(max_right, right)
        return ans
