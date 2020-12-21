from unittest import TestCase


class Solution:
    """
    Time Complexity: O(|S|). Two-pass.
    Space Complexity: O(1).
    """

    def decodeAtIndex(self, S: str, K: int) -> str:
        decoded_length = 0
        for char in S:
            if char.isalpha():
                decoded_length += 1
            else:
                decoded_length *= int(char)

        for pos in range(len(S) - 1, -1, -1):
            if K == decoded_length:
                # Get the last alphabet.
                while pos >= 0:
                    if S[pos].isalpha():
                        return S[pos]
                    pos -= 1

            if S[pos].isalpha():
                decoded_length -= 1
            else:
                decoded_length /= int(S[pos])
                if K > decoded_length:
                    K %= decoded_length
                    if K < 1:
                        K += decoded_length


class TestDecodeAtIndex(TestCase):
    def test_example_1(self):
        assert Solution().decodeAtIndex(S="leet2code3", K=10) == "o"

    def test_example_2(self):
        assert Solution().decodeAtIndex(S="ha22", K=5) == "h"

    def test_example_3(self):
        assert Solution().decodeAtIndex(S="a2345678999999999999999", K=1) == "a"

    def test_example_4(self):
        """
        Length=((2*6+1)*5+3)*9+1=613.
        1. Pick out "v". Length=612.
        2. Pick out "9". Length=68. K>Length, K=10.
        3. Pick out "q". Length=67.
        4. Pick out "h". Length=66.
        5. Pick out "x". Length=65.
        6. Pick out "5". Length=13.
        7. Pick out "u". Length=12.
        8. Pick out "6". Length=2. K>Length, K=2. Return last_alpha.
        """
        assert Solution().decodeAtIndex(S="vk6u5xhq9v", K=554) == "k"
