from collections import defaultdict
from typing import List


class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        count, ans = defaultdict(int), list()
        for i in range(len(s) - 9):
            count[s[i : i + 10]] += 1
        for key, value in count.items():
            if value > 1:
                ans.append(key)
        return ans


class OfficialSolutionApproach1:
    """
    == Overview ==
    Follow-up here is to solve the same problem for arbitrary sequence of length L, and
    to check the situation when L is quite large. Hence, let's use L=10 notation
    everywhere to ease the problem generalisation.
    We will discuss three different ideas how to proceed. They are all based on sliding
    window + hashset. The key point is how to implement a window slice.
    Linear time window slice O(L) is easy stupid, just take a substring. Overall that
    would result in O((N-L)L) time complexity and huge space consumption in the case of
    large sequences.
    Constant-time slice O(1) is where the fun starts, because the way you choose will
    show your actual background. There are 2 ways to proceed:
        - Rabin-Karp: constant-time slice using rolling hash algorithm
        - Bit-manipulation: constant-time slice using bitmasks
    Last 2 approaches have O(N-L) time complexity and moderate space consumption even
    in the case of large sequences.

    == Approach 1: Linear Time Slice Using Substring + HashSet ==
    The idea is straightforward:
        - Move a sliding window of length L along the string of length N.
        - Check if the sequence in the sliding window is in the hash set of already seen
        sequences.
            - If yes, the repeated sequence is right here. Update the output.
            - If not, save the sequence in the sliding window in the hashset.

    This solution is same as the one in above.

    == Complexity Analysis ==
        - Time Complexity: O((N-L)L), i.e. O(N) for the constant L=10. In the loop
        executed N-L+1 one builds a substring of length L. Overall that results in
        O((N-L)L) time complexity.
        - Space Complexity: O((N-L)L) to keep the hashtable/hashset, that results in
        O(N) for the constant L=10.
    """

    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        return Solution().findRepeatedDnaSequences(s=s)


class OfficialSolutionApproach2:
    """
    == Approach 2: Rabin-Karp: Constant-time Slice Using Rolling Hash ==
    Rabin-Karp algorithm is used to perform a multiple pattern search. It's used for
    plagiarism detection and in bioinformatics to look for similarities in 2 or more
    proteins.

    The idea is to slice over the string and to compute the hash of the sequence in the
    sliding window, both in a constant time.

    Let's use the string "ACAACCAGTTGT" as an example.
    First, convert string to integer array:
        "A" -> 0, "C" -> 1, "G" -> 2, "T" -> 3
    So "ACAACCAGTTGT" is 010011023323.
    Compute hash for the first sequence of length L: 0100110233. The sequence could be
    considered as a base 4 number and hashed as: 3 * 4^0 + 3 * 4^1 + ... + 0 * 4^9.
    Now, consider the next slice: "CAACCAGTTG" which can be hashed as:
        2 + 4 * (hash(previous_slice) - 0 * 4^9)
        = 2 + 4 * hash(previous_slice) - 0 * 4^10

    Window slice and hash recomputation are both done in a constant time.

    == Algorithm ==
    - Iterate over the start position of sequence: from 1 to N-L.
        - If start == 0, compute the hash of the first sequence s[0:L].
        - Otherwise, compute rolling hash from the previous hash value.
        - If hash is in the hashset, we have a repeated sequence.
        - Otherwise, add hash in the hashset.
    - Return output list.

    == Complexity Analysis ==
    - Time Complexity: O((N-L)*L), i..e O(N) for the constant L=10. In the loop executed
    N - L + 1 one builds a hash in a constant time,
    - Space Complexity: O(N-L) to keep the hash set.
    """

    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        L, MULTIPLIER, hash = 10, 4 ** 9, 0
        mp = {"A": 0, "C": 1, "G": 2, "T": 3}

        seen, output = set(), set()

        for i in range(len(s) - L + 1):
            if i == 0:
                tmp = 0
                for ch in s[:L]:
                    tmp = 4 * tmp + mp[ch]
                hash = tmp
            else:
                # 4**9 * 1 + 4**8 * 3 + ... + 4**0 * 0
                hash = 4 * (hash - MULTIPLIER * mp[s[i - 1]]) + mp[s[i + L - 1]]

            if hash in seen:
                # O(L) only when it is repeating.
                output.add(s[i : i + L])
            else:
                seen.add(hash)

        return list(output)


class OfficialSolutionApproach3:
    """
    == Approach 3: Bit Manipulation: Constant-time Slice using Bitmask ==
    The idea is to slice over the string and to compute the bitmask of the sequence in
    the sliding window, both in a constant time.

    As for Rabin-Karp, let's start from the conversion of string to 2-bits integer
    array:
        A -> 0 = 00, C -> 1 = 01, G -> 2 = 10, T -> 3 = 11
    For the next slice:
        bitmask <<= 2
        bitmask |= mp[s[i-L+1]]
        bitmask &= -(3 << 2 * L) (This unsets the first 2 bits)

    Window slice and bitmask re-computation are both done in a constant time.

    == Algorithm ==
    - Iterate over the start position of sequence: from 1 to N-L.
        - If start=0, compute the bitmask of the first sequence s[0:L]
        - Otherwise, compute bitmask from the previous bitmask.
        - If bitmask is in the hashset, one met a repeated sequence.
        - Otherwise, add bitmask to hashset.
    - Return the output list.

    == Complexity Analysis ==
    - Time Complexity: O((N-L)L).
    - Space Complexity: O(N-L) to keep the hashset.
    """

    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        L, bitmask = 10, 0
        char_to_num = {"A": 0, "C": 1, "G": 2, "T": 3}

        seen, output = set(), set()

        for i in range(len(s) - L + 1):
            if i == 0:
                for ch in s[:L]:
                    bitmask <<= 2
                    bitmask |= char_to_num[ch]
            else:
                bitmask <<= 2
                bitmask |= char_to_num[s[i + L - 1]]
                bitmask &= ~(3 << 2 * L)

            if bitmask in seen:
                output.add(s[i : i + L])
            else:
                seen.add(bitmask)

        return list(output)
