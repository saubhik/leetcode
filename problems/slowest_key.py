from typing import List


class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        n = len(releaseTimes)
        max_tup = (releaseTimes[0], keysPressed[0])
        for i in range(1, n):
            duration = releaseTimes[i] - releaseTimes[i - 1]
            max_tup = max(max_tup, (duration, keysPressed[i]))
        return max_tup[1]
