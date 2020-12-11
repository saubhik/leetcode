class Solution:
    """
    3: 1 -> 1, 2 -> 10, 3 -> 11
    Find the position of the most significant set bit.
    11011 = 1 * (2**() + 2 * (2**(2)) + 3  * (2**(1)) = 27.

    Time Complexity: O(n).
    Space Complexity: O(1).
    """

    def concatenatedBinary(self, n: int) -> int:
        MOD = 1e9 + 7
        # O(lg(max_num_digits) = lg(5))=O(1) time.
        def _get_num_bits(n: int):
            bits = 0
            while n:
                n >>= 1
                bits += 1
            return bits

        multiplier, ans = 1, 0
        for i in range(n, -1, -1):
            if i <= n - 1:
                multiplier *= 2 ** _get_num_bits(n=i + 1)
                multiplier %= MOD
            ans += i * multiplier
            ans %= MOD
        return int(ans)


class SolutionTwo:
    """
    We want to use only bit operations:
    for num in range(1, n+1):
        result = ((result << length) | num) % MOD
        # where length is the binary length of num.
    How do we get binary length of the number?
    We use num & (num - 1) == 0 to check if num is a power of 2.
    If it's a power of 2, we want to increase the length by 1.

    Remember that | bitwise operator concatenates.
    """

    def concatenatedBinary(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        length, result = 0, 0
        for num in range(1, n + 1):
            if num & (num - 1) == 0:
                length += 1
            result = ((result << length) | num) % MOD
        return result
