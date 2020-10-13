class Solution:
    # Straight Forward.
    # Time Complexity: O(n).
    # Space Complexity: O(1).
    def buddyStrings(self, A: str, B: str) -> bool:
        n = len(A)
        if n != len(B):
            return False

        if A == B:
            # No different letters.
            # At least 2 letters in A must be same.
            # O(n) time, O(1) space.
            seen = set()
            for ch in A:
                if ch in seen:
                    return True
                seen.add(ch)
            return False

        ai = bi = ""
        count = 0
        for i in range(n):
            if A[i] != B[i]:
                if count > 2:
                    return False
                ai, bi, count = ai + A[i], bi + B[i], count + 1

        return ai[::-1] == bi
