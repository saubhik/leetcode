from typing import List


class Solution:
    # Maintain a partition mapping characters to partitions.
    # Maintain a counts of characters in each partition.
    # For each character in given string:
    # If character is already mapped to a previous partition,
    # remap all the characters which are mapped to greater partitions to the previous
    # partition.
    # Also, update the counts of the partitions which are being updated.
    # Otherwise, just assign to a new partition.
    #
    # We can solve in a cleaner way using the Two Pointer approach. Whenever there is
    # a problem using arrays and intervals/partitions, better to use the Two Pointer
    # approach.
    #
    # Time: O(n) time.
    # Space: O(1) space.
    def partitionLabels(self, S: str) -> List[int]:
        partition = [-1] * 26
        counts = [0] * 26
        last_part = -1

        for char in S:
            part = partition[ord(char) - ord("a")]
            if part != -1:
                for i in range(26):
                    if partition[i] > part:
                        counts[part] += counts[partition[i]]
                        counts[partition[i]] = 0
                        partition[i] = part
                counts[part] += 1
                last_part = part
            else:
                partition[ord(char) - ord("a")] = last_part + 1
                counts[last_part + 1] += 1
                last_part += 1

        return [x for x in counts if x != 0]


class SolutionTwo:
    # Consider "ababcbacadefe".
    # Index:    0123456789012
    #
    # last = {a:8, b:5, c:7, d:9, e:12, f:11}
    # 1st iteration:
    # i = 0, c = a
    # j = max(0, 8) = 8
    # 2nd iteration:
    # i = 1, c = b
    # j = max(8, 5) = 8
    # ...
    # 9th iteration:
    # i = 8, c = a
    # j = 8
    # Time to end this interval.
    # Restart anchor.
    #
    # How could I come up with this?
    # Two pointer approach.
    # Pointer 1 points to start of interval.
    # Pointer 2 points to estimated end of interval.
    # Keep updating pointer 2 during the traversal.
    # If anything in between has a later occurrence, reset pointer 2.
    #
    # Time: O(n)
    # Space: O(1)
    def partitionLabels(self, S: str):
        last = {c: i for i, c in enumerate(S)}
        j = anchor = 0
        ans = []
        for i, c in enumerate(S):
            j = max(j, last[c])
            if i == j:
                ans.append(i - anchor + 1)
                anchor = i + 1

        return ans
