import bisect
import random
from typing import List


class Solution:
    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.prefixSums = []
        prefixSum = 0
        for x1, y1, x2, y2 in rects:
            prefixSum += (x2 - x1 + 1) * (y2 - y1 + 1)
            self.prefixSums.append(prefixSum)

    def pick(self) -> List[int]:
        n = random.random() * self.prefixSums[-1]
        r = bisect.bisect_left(self.prefixSums, n)
        x1, y1, x2, y2 = self.rects[r]
        rank = int(n - self.prefixSums[r - 1] if r > 0 else n)
        width = y2 - y1 + 1
        return [x1 + rank // width, y1 + rank % width]


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
