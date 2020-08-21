from collections import deque


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Time: O(n)
    # Space: O(n)
    # I think using a queue here might not be a good thing. We should do it without
    # using additional data structures. But problem description did not mention.
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        if head is None:
            return head

        reversed_nodes = deque()

        def _f(head):
            if head.next is not None:
                _f(head=head.next)
            reversed_nodes.append(head)

        _f(head=head)

        while head is not None:
            res = reversed_nodes.popleft()

            if head == res:
                head.next = None
                break

            tmp = head.next
            head.next = res
            res.next = tmp

            if res.next == res:
                res.next = None
                break

            head = tmp
