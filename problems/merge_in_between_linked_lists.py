# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Time Complexity: O(b + n2).
    # Space Complexity: O(1).
    def mergeInBetween(
        self, list1: ListNode, a: int, b: int, list2: ListNode
    ) -> ListNode:
        curr = node1 = node2 = None
        for pos in range(b + 2):
            if pos == 0:
                curr = list1
            else:
                curr = curr.next
            if pos == a - 1:
                node1 = curr
            if pos == b + 1:
                node2 = curr

        node1.next = list2

        curr, tail = list2, None
        while curr:
            tail = curr
            curr = curr.next

        tail.next = node2

        return list1
