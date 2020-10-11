# There are some spherical balloons spread in two-dimensional space.
# For each balloon, provided input is the start and end coordinates of the horizontal
# diameter. Since it's horizontal, y-coordinates don't matter, and hence the
# x-coordinates of start and end of the diameter suffice.
# The start is always smaller than the end.
#
# An arrow can be shot up exactly vertically from different points along the x-axis.
# A balloon with xstart and xend bursts by an arrow shot at x if xstart ≤ x ≤ xend.
# There is no limit to the number of arrows that can be shot. An arrow once shot keeps
# traveling up infinitely.
#
# Given an array points where points[i] = [xstart, xend], return the minimum number of
# arrows that must be shot to burst all balloons.
#
# Input: points = [[10,16],[2,8],[1,6],[7,12]]
# Output: 2
# Explanation: One way is to shoot one arrow for example at x = 6 (bursting the
# balloons [2,8] and [1,6]) and another arrow at x = 11 (bursting the other two
# balloons).
#
# Input: points = [[1,2],[3,4],[5,6],[7,8]]
# Output: 4
from typing import List


class Solution:
    """
    [[10,16], [2,8], [1,6], [7,12], [11,13]]
    I want to find the list of x-coordinates which is contained in most of the
    intervals.

    1. First sort it, based on left endpoint first and break ties using right endpoint.
        [[1,6], [2,8], [7,12], [10,16], [11,13]]
    2. Walk over the sorted intervals.
        Intersect them with the last intersection.
        If no intersection, consider the interval new intersection, and increment the
        counter.

    Time Complexity: O(nlgn), where n is the number of points (intervals).
    Space Complexity: O(n), due to Python's Tim Sort.
    """

    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        left, right, count = float("-inf"), float("inf"), 1
        points.sort()
        for point in points:
            if point[0] > left:
                left = point[0]
            if point[1] < right:
                right = point[1]
            if left > right:
                left, right = point
                count += 1

        return count


class OfficialSolution:
    """
    Greedy problems usually look like "Find minimum number of something to do something"
    or "Find maximum number of something to fit in some conditions", and typically
    propose an unsorted input.

    The idea of greedy algorithm is to pick the locally optimal move at each step, that
    will lead to the globally optimal solution.

    The standard solution has O(nlgn) time complexity and consists of 2 parts:
        - Figure out how to sort the input data (O(nlgn) time). That could be done
        directly by a sorting or indirectly by a heap usage. Typically sort is better
        than the heap usage because of the gain in space.
        - Parse the sorted input to have a solution in O(n) time.

    Please notice that in case of well-sorted input one doesn't need the first part and
    the greedy solution could have O(n) time complexity.

    How to prove that your greedy algorithm provides globally optimal solution?
    Usually you could use proof by contradiction.

    == Intuition ==
    Let's sort the ballons by the end coordinate, and then check them one by one. The
    first balloon is a green one number 0, it ends at coordinate 6, and there are no
    balloons ending before it because of sorting.
    The other balloons have two possibilities:
        - To have a start coordinate smaller than 6, like a red balloon. These ones
        could burst together with the balloon 0 by one arrow.
        - To have a start coordinate larger than 6, like a yellow balloon. These ones
        couldn't be burst together with the balloon 0 by one arrow, and hence one needs
        to increase the number of arrows here.

    That means that one could always track the end of the current balloon, and ignore
    all the balloons which end before it. Once the current balloon is ended (= the next
    balloon starts after the current balloon), one has to increase the number of arrows
    by one and start to track the end of the next balloon.

    Compared to my solution, this only requires 1 extra variable to maintain the end
    point.

    == Complexity Analysis ==
    - Time Complexity: O(nlgn) because of sorting of input data.
    - Space Complexity: O(n) or O(lgn)
        - The space complexity of the sorting algorithm depends on the implementation of
        each programming language.
        - For instance, the list.sort() function in Python is implemented using Timsort
        algorithm whose space complexity is O(n).
        - In Java, the Arrays.sort() is implemented as a variant of quicksort algorithm
        whose space complexity is O(lgn).
    """

    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        # Sort by the end points.
        # [[10,16], [2,8], [1,6], [7,12], [11,13]]
        # [[1,6], [2,8], [7,12], [11,13], [10,16]]
        #     6 ,    6 ,    12 ,     12 ,     12   <- x_end
        points.sort(key=lambda x: x[1])

        count, x_end = 0, float("-inf")
        for point in points:
            if point[0] > x_end:
                count += 1
                x_end = point[1]

        return count
