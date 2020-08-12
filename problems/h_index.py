from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # 4, 0, 6, 1, 5
        # 0, 1, 4, 5, 6
        #       ^......
        # length should equal number
        # define candidate h-index, h = n - i
        # from the left, find the first i s.t. h <= a[i]
        # intuition:
        # for j >= i, a[j] >= h, and # of such j == h
        # for j < i, a[j] <= h,
        #
        # Time: O(nlgn)
        # Space: O(1)
        citations.sort()
        n = len(citations)
        for i in range(n):
            h_index = n - i
            if h_index <= citations[i]:
                return h_index
        return 0
