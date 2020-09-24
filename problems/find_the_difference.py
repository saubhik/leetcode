class Solution:
    # Time Complexity: O(n), where n is the length of t or s.
    # Space Complexity: O(1)
    def findTheDifference(self, s: str, t: str) -> str:
        counts = [0] * 26
        for ch in s:
            counts[ord(ch) - ord("a")] += 1
        for ch in t:
            if counts[ord(ch) - ord("a")] == 0:
                return ch
            counts[ord(ch) - ord("a")] -= 1
        return ""


class OfficialSolution:
    """
    First approach is sorting and comparing character by character.
    Time Complexity: O(nlgn).
    Space Complexity: O(1).

    Second approach is using hash map of 26 keys, which is same as my solution above.
    Time Complexity: O(n).
    Space Complexity: O(1).

    Third approach is bit manipulation. Please check the doc string of the function
    below.
    """

    def findTheDifferenceApproach3(self, s: str, t: str) -> str:
        """
        To use bitwise XOR operation on all elements. XOR would help to eliminate the
        alike and only leave the odd duckling.
        Thus, the left over bits after XORing all the characters from string s and
        string t would be from the extra character of string t.

        Time Complexity: O(n), where N is the length of s or t.
        Space Complexity: O(1).
        """
        xored = 0
        for ch in s:
            xored ^= ord(ch)
        for ch in t:
            xored ^= ord(ch)
        return chr(xored)
