from typing import List


class Solution:
    # D(2,1) I(1,3) I(3,5) D(5,4) I(4,6) -> 2,1,3,5,4,6
    # D(2,1) I(1,3) I(3,4) I(4,5) I(5,10) D(10,9) D(9,8) D(8,7) D(7,6) I(6,11)
    # need to know the number of Ds after an I, but before the next I
    # D(4,3) D(3,2) D(2,1) I(1,5) I(5,10) D(10,9) D(9,8) D(8,7) D(7,6) I(6,11) I(7,12)
    # Start counting from the last D just before I
    # I(3) D(2) D(1) I
    #
    # Time: O(n)
    # Space: O(n)
    def findPermutation(self, s: str) -> List[int]:
        s = "I" + s

        ans = [0] * len(s)
        i, last_i, last_num = 0, -1, 0

        while i < len(ans):
            if not (i + 1 < len(s) and s[i + 1] == "D"):
                ans[last_i + 1 : i + 1] = [
                    last_num + _inc for _inc in range(i - last_i, 0, -1)
                ]
                last_num += i - last_i
                last_i = i
            i += 1

        return ans
