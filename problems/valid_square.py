from math import dist
from typing import List


class Solution:
    # Time Complexity: O(1).
    # Space Complexity: O(1).
    def validSquare(
        self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]
    ) -> bool:
        if p1 == p2 == p3 == p4:
            return False

        if dist(p1, p2) == dist(p1, p3) == dist(p2, p4) == dist(p4, p3):
            if dist(p1, p4) == dist(p2, p3):
                return True
            return False

        if dist(p1, p2) == dist(p1, p4) == dist(p2, p3) == dist(p3, p4):
            if dist(p1, p3) == dist(p2, p4):
                return True
            return False

        if dist(p1, p3) == dist(p1, p4) == dist(p3, p2) == dist(p2, p4):
            if dist(p1, p2) == dist(p3, p4):
                return True
            return False

        return False
