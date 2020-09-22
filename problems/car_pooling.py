from collections import defaultdict
from typing import List


class Solution:
    # Since the max drop location can be 1000, we can store number of people in the
    # car at every location in a hash map. It will take O(1) space.
    # We iterate over every element of trips, and update our hash map.
    #
    # Time: O(1)
    # Space: O(1)
    # Since the number of trips is bounded.
    #
    # Further optimizations:
    # As we will see in the official solution, we could keep only the changes (the
    # delta) in the hash map.
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        counts = defaultdict(int)
        max_count = 0
        for trip in trips:
            for loc in range(trip[1], trip[2]):
                counts[loc] += trip[0]
                max_count = max(max_count, counts[loc])
                if max_count > capacity:
                    return False
        return True


class OfficialSolution:
    """
    == Overview ==
    It is one of the classical problems related to intervals, and we have some similar
    problems such as Meeting Rooms II at LeetCode. Below, two approaches are introduced:
    the simple Time Stamp approach, and the Bucket Sort approach.
    """

    def carPoolingApproach1(self, trips: List[List[int]], capacity: int) -> bool:
        """
        == Approach 1: Time Stamp ==
        == Intuition ==
        A simple idea is to go through from the start to end, and check if the actual
        capacity exceeds `capacity`. To know the actual capacity, we just need the number of
        passengers changed at each timestamp.
        We can save the number of passengers changed at each time, sort it by timestamp, and
        finally iterate it to check the actual capacity.

        == Algorithm ==
        We will initialize a list to store the number of passengers changed and the
        corresponding timestamp and then sort it.
        Finally, we just need to iterate from the start timestamp to the end timestamp, and
        check if the actual capacity meets the condition.

        == Complexity Analysis ==
        Assume N is the length of the trips.
        Time Complexity: O(NlgN) since we need to iterate over trips and sort our timestamp.
            Iterating costs O(N), and sorting costs O(NlgN), and adding together we have
            O(N) + O(NlgN) = O(NlgN).
        Space Complexity: O(N) to store timestamp.
        """
        timestamp = []
        for trip in trips:
            timestamp.append([trip[1], trip[0]])
            timestamp.append([trip[2], -trip[0]])

        timestamp.sort()

        used_capacity = 0
        for time, passenger_change in timestamp:
            used_capacity += passenger_change
            if used_capacity > capacity:
                return False

        return True

    def carPoolingApproach2(self, trips: List[List[int]], capacity: int) -> bool:
        """
        == Approach 2: Bucket Sort ==
        == Intuition ==
        Note that in the problem there is a interesting constraint:
            0 <= trips[i][1] < trips[i][2] <= 1000
        What pops into the mind is Bucket Sort, which is a sorting algorithm in O(N)
        time but requires prior knowledge for the range of the data.
        We can use it instead of the normal sorting in this method.
        What we do is initial 1001 buckets, and put the number of passengers changed in
        corresponding buckets, and collect the buckets one by one.

        == Algorithm ==
        We will initialize 1001 buckets, iterate `trips`, and save the number of
        passengers changed at i mile in the i-th bucket.

        == Complexity Analysis ==
        Assume N is the length of the trip.
        Time Complexity: O(max(N, 10001)), since we need to iterate over trips and then
            iterate over 1001 buckets.
        Space Complexity: O(1001) = O(1) since we have 1001 buckets.
        """
        timestamp = [0] * 1001
        for trip in trips:
            timestamp[trip[1]] += trip[0]
            timestamp[trip[2]] -= trip[0]

        used_capacity = 0
        for passenger_change in timestamp:
            used_capacity += passenger_change
            if used_capacity > capacity:
                return False

        return True
