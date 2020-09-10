class Solution:
    # Time: O(N1+N2+max(N1, N2))
    # Space: O(N1+N2)
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = list(map(int, version1.split(sep=".")))
        v2 = list(map(int, version2.split(sep=".")))

        i = 0

        while i < len(v1) and i < len(v2):
            if v1[i] < v2[i]:
                return -1
            elif v1[i] > v2[i]:
                return 1
            i += 1

        while i < len(v1):
            if v1[i] != 0:
                return 1
            i += 1

        while i < len(v2):
            if v2[i] != 0:
                return -1
            i += 1

        return 0


class SolutionTwo:
    # Two Pointers, One Pass Method
    # Time: O(max(N1, N2))
    # Space: O(max(N1, N2))
    # Idea is to do processing during iteration.
    def compareVersion(self, version1: str, version2: str) -> int:
        p1 = p2 = 0
        n1, n2 = len(version1), len(version2)

        while p1 < n1 or p2 < n2:
            i1, p1 = self.get_next_chunk(version1, n1, p1)
            i2, p2 = self.get_next_chunk(version2, n2, p2)
            if i1 != i2:
                return 1 if i1 > i2 else -1

        return 0

    def get_next_chunk(self, version: str, n: int, p: int):
        if p > n - 1:
            return 0, p

        p_end = p
        while p_end < n and version[p_end] != ".":
            p_end += 1

        # Space: O(max(N1, N2)) worst case.
        i = int(version[p:p_end]) if p_end != n - 1 else int(version[p:n])
        p = p_end + 1

        return i, p
