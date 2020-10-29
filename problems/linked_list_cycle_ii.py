# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    Based on Floyd's Hare and Tortoise Algorithm.

    Time Complexity: O(n).
    Space Complexity: O(1).
    """

    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None

        # This is O(n) time.
        # Suppose F is the acyclic length. After F iterations, tortoise is at start
        # of cycle node 0 and hare has covered 2F nodes, F of them in acyclic part.
        # So hare is at node h = F (mod C).
        # After C-h more iterations, tortoise is at node C-h in the cycle. Hare is at
        # node h+2(C-h)=2C-h=C-h (mod C). So both point to the same node.
        # Since F+C-h<F+C=n, so hare and tortoise meet before traversing all n nodes.
        ptr1 = slow = fast = head
        ptr2 = None
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                ptr2 = slow
                break

        if slow != fast:
            return None

        # Suppose ptr1 is F distance away from the cycle node 0. And ptr2, i.e. the
        # intersection point is a distance away from the cycle node 0.
        # Tortoise covered F+a nodes. Hare covered 2(F+a) nodes. We have:
        # (F+a)=2(F+a)(mod C). So, F+a=nC. If we move ptr1, reduce F by 1, then
        # ptr2 can be moved until we have F=a=0.
        while ptr1 != ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        return ptr1
