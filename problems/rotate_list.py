# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    # This is almost same as Official Solution.
    def rotateRight(self, head: ListNode, k: int) -> Optional[ListNode]:
        if k == 0 or head is None:
            return head

        node, length = head, 1
        while node.next is not None:
            length += 1
            node = node.next
        tail = node

        head_idx = (length - k) % length
        if head_idx == 0:
            return head

        parent, node, idx = None, head, 0
        while True:
            if idx == head_idx:
                # Convert from:
                # head -> ... -> parent -> node -> .... -> tail
                # to:
                # node -> ... -> tail -> head -> ... -> parent
                tail.next, parent.next = head, None
                return node
            idx, parent, node = idx + 1, node, node.next
