from math import sqrt
from typing import List


class Solution:
    # candies=10, num_people=3
    # 1,2,3
    # 4
    # (i+1)+(n+i+1)+(2*n+i+1)+...= n(0+1+2+...+k-1) + k(i+1).
    # each person gets (n)(k-1)(k)/2 + (k)(i+1) candies after k rounds.
    # 1+2+...+m = c; m(m+1)=2c; m^2+m-2c=0; m=(-1+sqrt(1+8c))/2.
    # Total rounds, k = int(m/n).
    #
    # Time: O(n)
    # Space: O(n)
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:

        ans = [0] * num_people

        # total candies distributed
        t = 0

        # max number of rounds in which we can distribute completely
        mr = int((-1 + sqrt(1 + 8 * candies)) / (2 * num_people))

        for i in range(1, num_people + 1):
            _c = num_people * ((mr * (mr - 1)) // 2) + mr * i
            t += _c
            ans[i - 1] += _c

        # last person in last round got this many candies
        l = mr * num_people

        for i in range(1, num_people + 1):
            if t < candies:
                _c = min(l + i, candies - t)
                t += _c
                ans[i - 1] += _c
            else:
                break

        return ans
