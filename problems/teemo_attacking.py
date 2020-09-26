from typing import List


class Solution:
    # timeSeries = [1, 3, 8, 19], duration = 5
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        ans, last = 0, float("-inf")
        for t in timeSeries:
            ans += duration
            if (t - last) < duration:
                ans -= duration - (t - last)
            last = t
        return ans


class OfficialSolution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        """
        The problem is an example of merge interval questions which are now quite
        popular in Google.
        Typically such problems could be solved in linear time in the case of sorted
        input, and in O(nlgn) time otherwise.
        Here one deals with a sorted input, and the problem could be solved in one pass
        with a constant space. The idea is straightforward: consider only the interval
        between two attacks. Ashe spends in a poisoned condition the whole time interval
        if this interval is shorter than the poisoning time duration, and duration
        otherwise.

        == Algorithm ==
        - Initiate total time in poisoned condition, total = 0.
        - Iterate over timeSeries list. At each step add to the total time the minimum
            between interval length and the poisoning time duration.
        - Return total + duration to take the last attack into account.

        == Complexity Analysis ==
        - Time Complexity: O(n) where n is the length of the input list, since we
            iterate the entire list.
        - Space Complexity: O(1), it's a constant space solution.
        """
        n = len(timeSeries)
        if n == 0:
            return 0

        total = 0
        for i in range(n - 1):
            total += min(timeSeries[i + 1] - timeSeries[i], duration)
        return total + duration
