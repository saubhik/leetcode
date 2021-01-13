from typing import Optional
from unittest import TestCase


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Linear Scan using 3 pointers.
    # Time Complexity: O(n).
    # Space Complexity: O(1).
    def deleteDuplicates(self, head: ListNode) -> Optional[ListNode]:
        if not head:
            return None

        pre, last, curr = ListNode(val=-101), ListNode(val=-101), head
        sentinel = pre

        while curr:
            if last.val != curr.val:
                if pre.next:
                    pre = last
                else:
                    pre.next = curr
            elif pre.next:
                pre.next = None
            last, curr = curr, curr.next

        return sentinel.next


class TestRemoveDuplicatesFromSortedList(TestCase):
    def test_example_1(self):
        sentinel = curr = ListNode(val=101)
        for val in (1, 2, 3, 3, 4, 4, 5):
            curr.next = ListNode(val=val)
            curr = curr.next

        ans = Solution().deleteDuplicates(head=sentinel.next)

        assert ans.val == 1
        assert ans.next.val == 2
        assert ans.next.next.val == 5

    def test_example_2(self):
        sentinel = curr = ListNode(val=101)
        for val in (1, 1, 1, 2, 3):
            curr.next = ListNode(val=val)
            curr = curr.next

        ans = Solution().deleteDuplicates(head=sentinel.next)

        assert ans.val == 2
        assert ans.next.val == 3
