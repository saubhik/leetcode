from typing import List


class Solution:
    # 1,3,5,4,7
    # Suppose for sequences ending at i, we knew the length of the longest subsequence,
    # length[i], and the count of such sequences, count[i].
    # nums    1,3,5,4,7
    # length  1,2,3,3,4
    # count   1,1,1,2,2
    #
    # Time Complexity: O(n**2)
    # Space Complexity: O(n)
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 0:
            return 0

        # Length of longest subsequence ending in nums[i].
        length = [1] * n
        # Count of the number of longest subsequences ending with nums[i].
        count = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    new_length = length[j] + 1
                    if new_length > length[i]:
                        length[i], count[i] = new_length, count[j]
                    elif new_length == length[i]:
                        count[i] += count[j]

        lis_length = max(length)
        ans = 0
        for i in range(n):
            if length[i] == lis_length:
                ans += count[i]

        return ans


class SolutionSegmentTree:
    """
    Time Complexity: O(nlgn).
    Space Complexity: O(n).
    """

    class Node:
        def __init__(self, range_left: int, range_right: int):
            self.range_left = range_left
            self.range_right = range_right
            self._left = None
            self._right = None
            self.val = 0, 1

        @property
        def range_mid(self) -> int:
            return (self.range_left + self.range_right) // 2

        @property
        def left(self):
            if self._left is None:
                self._left = self.__class__(
                    range_left=self.range_left, range_right=self.range_mid
                )
            return self._left

        @property
        def right(self):
            if self._right is None:
                self._right = self.__class__(
                    range_left=self.range_mid + 1, range_right=self.range_right
                )
            return self._right

    @staticmethod
    def merge(val1, val2):
        if val1[0] == val2[0]:
            if val1[0] == 0:
                return 0, 1
            return val1[0], val1[1] + val2[1]
        return max(val1, val2)

    def query(self, node: Node, key: int):
        if node.range_right <= key:
            return node.val
        elif key < node.range_left:
            return 0, 1
        else:
            return self.merge(
                val1=self.query(node=node.left, key=key),
                val2=self.query(node=node.right, key=key),
            )

    def insert(self, node: Node, key: int, val: tuple):
        if node.range_left == node.range_right:
            node.val = self.merge(val1=node.val, val2=val)
            return
        if key <= node.range_mid:
            self.insert(node=node.left, key=key, val=val)
        else:
            self.insert(node=node.right, key=key, val=val)
        node.val = self.merge(val1=node.left.val, val2=node.right.val)

    def findNumberOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        root = self.Node(range_left=min(nums), range_right=max(nums))
        for num in nums:
            # O(lg n) operation.
            length, count = self.query(node=root, key=num - 1)
            # O(lg n) operation.
            self.insert(node=root, key=num, val=(length + 1, count))
        return root.val[1]
