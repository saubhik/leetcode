from typing import List


class Solution:
    # XOR between two numbers is high if there is difference in the most significant
    # bits.
    # For each number, during iteration, we need to find if there is another number
    # which has complementary bits starting with the most significant bit.
    # We can use a prefix tree (AKA trie) to store the binary bits.
    # A search in a trie is O(length of trie) = O(32) = O(1) in this case.
    #
    # During iteration, we search in the trie for the ideal number using the
    # complementary bit at each step, starting from the most significant bit.
    # So, time complexity is O(n).
    #
    # Space complexity is the space required to store the trie which is 32 level deep
    # perfect binary tree in worst case. So, 2^32 - 1 units of storage. But it's O(1).
    #
    # Further optimisations:
    # 1. Store bits instead of as strings in the keys of the trie.
    # 2. Instead of storing the number as in node["END"], we can also compute the number
    #    from the path as we traverse.
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie = {"ROOT": {}}

        node = trie["ROOT"]
        for num in nums:
            node = trie["ROOT"]
            for ch in "{:032b}".format(num):
                if not ch in node:
                    node[ch] = {}
                node = node[ch]
            node["END"] = num

        ans = 0

        for num in nums:
            node = trie["ROOT"]
            for ch in "{:032b}".format(num):
                complement = "1" if ch == "0" else "0"
                node = node[complement] if complement in node else node[ch]

            # "END" must be in node
            ans = max(ans, num ^ node["END"])

        return ans
