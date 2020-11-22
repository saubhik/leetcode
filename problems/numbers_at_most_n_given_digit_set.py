from typing import List


class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        # Find the number of digits in n.
        n_str = str(n)
        k, num_digits = len(n_str), len(digits)

        # Find the number of valid numbers that have less than k digits.
        ans, _tmp = 0, 1
        for i in range(k - 1):
            _tmp *= num_digits
            ans += _tmp

        # Find the number of valid numbers that have equal to k digits.
        _tmp = 1
        for pos in range(k - 1, -1, -1):
            _tmp = len([digit for digit in digits if digit < n_str[pos]]) * (
                num_digits
            ) ** (k - pos - 1) + (_tmp if n_str[pos] in digits else 0)
        ans += _tmp

        return ans
