from typing import List
from unittest import TestCase

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Standard merge procedure in MergeSort.
    # Time Complexity: O(n).
    # Space Complexity: O(n).
    #   where n is len(l1)+len(l2).
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        sentinel = curr = ListNode()

        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next

        curr.next = l1 if l1 else l2

        return sentinel.next


class TestMergeTwoLists(TestCase):
    def _make_list(self, values: List[int]) -> ListNode:
        sentinel = curr = ListNode()
        for val in values:
            curr.next = ListNode(val=val)
            curr = curr.next
        return sentinel.next

    def _get_values(self, node: ListNode) -> List[int]:
        values = []
        while node:
            values.append(node.val)
            node = node.next
        return values

    def test_example_1(self):
        assert (
            self._get_values(
                Solution().mergeTwoLists(
                    l1=self._make_list(values=[1, 2, 4]),
                    l2=self._make_list(values=[1, 3, 4]),
                )
            )
            == [1, 1, 2, 3, 4, 4]
        )

    def test_example_2(self):
        assert (
            self._get_values(
                Solution().mergeTwoLists(
                    l1=self._make_list(values=[]), l2=self._make_list(values=[])
                )
            )
            == []
        )

    def test_example_3(self):
        assert (
            self._get_values(
                Solution().mergeTwoLists(
                    l1=self._make_list(values=[]),
                    l2=self._make_list(values=[0]),
                )
            )
            == [0]
        )

    def test_example_4(self):
        assert (
            self._get_values(
                Solution().mergeTwoLists(
                    l1=self._make_list(values=[-9, 3]),
                    l2=self._make_list(values=[5, 7]),
                )
            )
            == [-9, 3, 5, 7]
        )
