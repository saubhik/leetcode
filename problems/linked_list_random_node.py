import random


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """Reservoir Sampling.
    Time Complexity: O(n).
    Space Complexity: O(1).
    """

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        curr = self.head
        counter, pick = 1, None
        while curr:
            if random.random() < 1 / counter:
                pick = curr.val
            counter += 1
            curr = curr.next
        return pick


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
