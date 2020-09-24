from typing import List


class Solution:
    # Keep track of amount in tank.
    # Example:
    # 1, 2, 3, 4, 5
    # 3, 4, 5, 1, 2
    #
    # tank:
    # 0, -2         <- disqualified
    #    0, -2      <- disqualified
    #       0, -2   <- disqualified
    # 6, 4, 2, 0, 3 <- qualified
    #
    # For O(n) time disqualification, I propose the following conjecture:
    # Consider a list of integers, L.
    # Sum of integers in L is >= 0 <=> There exists a run in L which consist of
    # cumulative sums of corresponding integers in the run, each having value >= 0.
    #
    # To find the exact run, we need O(n^2) time.
    #
    # Time Complexity: O(n ^ 2).
    # Space Complexity: O(1) additional space.
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) - sum(cost) < 0:
            # Rejection in O(n) time, O(1) space.
            return -1

        n = len(gas)
        for i in range(n):
            cum_sum, j = 0, i
            while True:
                cum_sum += gas[j] - cost[j]
                if cum_sum < 0:
                    break
                j = (j + 1) % n
                if j == i:
                    return i


class OfficialSolution:
    """
    == Approach 1: One Pass. ==
    == Intuition ==
    The first idea is to check every single station.
    - Choose the station as starting point.
    - Perform the road trip and check how much gas we have in tank at each station.
    That means O(N ^ 2) time complexity, and for sure once could od better.

    Let's notice two things.
    1. It's impossible to perform the road trip if sum(gas) < sum(cost). In this
        situation, the answer is -1.
        One could compute total amount of gas in the tank total_tank = sum(gas) -
        sum(cost) during the round trip, and then return -1 if total_tank < 0.
    2. It's impossible to start at a station i if gas[i] - cost[i] < 0, because then
        there is not enough gas in the tank to travel to i + 1 station.
        The second fact could be generalized. Let's introduce curr_tank variable to
        track the current amount of gas in the tank. If at some station curr_tank is
        less than 0, that means that one couldn't reach this station.
        Next step is to mark this station as a new starting point, and reset curr_tank to 0
        since one starts with no gas in tank.

    == Algorithm ==
    Now the algorithm is straight forward.
    1. Initiate total_tank and curr_tank as 0, and choose station 0 as a starting
        station.
    2. Iterate over all stations:
        - Update total_tank and curr_tank at each step, by adding gas[i] and subtracting
        cost[i].
        - If curr_tank < 0 at i + 1 station, make i + 1 station a new starting point and
        rest curr_tank = 0 to start with an empty tank.
    3. Return -1 if total_tank < 0 and starting station otherwise.

    == Complexity Analysis ==
    Time Complexity = O(N), since there is only 1 loop over all stations here.
    Space Complexity = O(1) since it's a constant space solution.

    == Idea ==
    During scanning, whenever we find curr_tank is becoming negative, we reset curr_tank
    to 0, and consider the next index as our potential candidate for starting position.

    This is a specific to a general problem solving heuristic:
    Whenever some variable of interest does not match the value who want it to contain,
    reset it and reset the potential candidate. This is useful for giving O(n) time
    algorithms.

    Why does this work?
    Suppose total_tank >= 0.
    Consider the starting position given by the algorithm is Ns.
    For all gas stations to the right (till 0), our curr_tank is >= 0.
    This is maintained by the algorithm.
    What about the reverse run from 0 to Ns?
    Suppose curr_tank is negative at some k, between 0 and Ns.
    This means sum of deltas (gas-cost) is negative from Ns to 0 and then 0 to k.
    Also sum of deltas (gas-cost) is negative from k to Ns, otherwise the starting
    position would be before Ns.
    This means total_tank < 0, which is contradiction.
    """

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_tank = curr_tank = start_index = 0
        n = len(gas)
        for i in range(n):
            total_tank += gas[i] - cost[i]
            if curr_tank < 0:
                curr_tank = 0
                start_index = i
            curr_tank += gas[i] - cost[i]
        return -1 if total_tank < 0 else start_index
