class Solution:
    # Straight Forward.
    # Time Complexity: O(n).
    # Space Complexity: O(1).
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if abs(len(s) - len(t)) not in (1, 0) or s == t:
            return False

        i, j, found = 0, 0, False
        while i < len(s) and j < len(t):
            if s[i] != t[j]:
                if found:
                    return False
                found = True

                if len(s) == len(t):
                    # s[i] needs to be replaced
                    i += 1
                    j += 1
                elif len(s) < len(t):
                    # t[j] needs to be deleted
                    j += 1
                else:
                    # s[i] needs to be deleted
                    i += 1

            else:
                i += 1
                j += 1

        return True
