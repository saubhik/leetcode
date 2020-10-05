class Solution:
    # Time Complexity: O(lgN).
    # Space Complexity : O(1).
    def bitwiseComplement(self, N: int) -> int:
        if N == 0:
            return 1

        k = 1
        while k <= N:
            k <<= 1
        return k - 1 - N


class OfficialSolution:
    """
    Idea 1:
    XORing with 1 flips bits.

    Idea 2:
    From Henry S. Warren, Jr.'s Hacker's Delight, Addison Wesley, 2002.
    bitmask = N makes sure first bit is set.
    bitmask |= bitmask >> 1 makes sure first 2 bits are set.
    bitmask |= bitmask >> 2 makes sure first 4 bits are set.
    bitmask |= bitmask >> 4 makes sure first 8 bits are set.
    bitmask |= bitmask >> 8 makes sure first 16 bits are set.
    bitmask |= bitmask >> 16 makes sure first 32 bits are set.

    Time Complexity: O(1).
    Space Complexity: O(1).
    """

    def bitwiseComplement(self, N: int) -> int:
        if N == 0:
            return 1

        bitmask = N
        bitmask |= bitmask >> 1
        bitmask |= bitmask >> 2
        bitmask |= bitmask >> 4
        bitmask |= bitmask >> 8
        bitmask |= bitmask >> 16
        return bitmask ^ N
