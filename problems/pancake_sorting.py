from typing import List


class Solution:
    # Idea like Bubble Sort
    # Time: O(n^2)
    # Space: O(n), O(1) additional space.
    def pancakeSort(self, A: List[int]) -> List[int]:
        def flip(sublist, k):
            # includes k in flipping
            i = 0
            while i < k / 2:
                sublist[i], sublist[k - i] = sublist[k - i], sublist[i]
                i += 1

        n = len(A)
        last, pivots = n, []
        while last >= 2:
            max_num_idx = A.index(last)

            if max_num_idx != last - 1:
                if max_num_idx != 0:
                    # reverse 0...max_num_idx
                    pivots.append(max_num_idx + 1)
                    flip(sublist=A, k=max_num_idx)

                # reverse 0...last - 1
                pivots.append(last)
                flip(sublist=A, k=last - 1)

            last -= 1

        return pivots
