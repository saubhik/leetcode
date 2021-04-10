from typing import List, Optional
from unittest import TestCase


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Time Complexity: O(nk)
    #   where n is the number of elements in one list,
    #   and k is the number of lists.
    # Space Complexity: O(nk)
    def mergeKLists(self, lists: List[ListNode]) -> Optional[ListNode]:
        if not lists:
            return None

        left = lists[0]
        for i in range(1, len(lists)):
            head = node = ListNode()
            right = lists[i]

            while left and right:
                if left.val <= right.val:
                    node.next = left
                    left = left.next
                else:
                    node.next = right
                    right = right.next
                node = node.next

            # If left still exists
            if left:
                node.next = left

            # If right still exists
            if right:
                node.next = right

            left = head.next

        return left


class TestSolution(TestCase):
    def test_example_1(self):
        lists = []
        for lis in [[1, 4, 5], [1, 3, 4], [2, 6]]:
            node = sentinel = ListNode()
            for element in lis:
                node.next = ListNode(val=element)
                node = node.next
            lists.append(sentinel.next)

        merged_list = Solution().mergeKLists(lists)

        lis = merged_list
        elements = []
        while lis:
            elements.append(lis.val)
            lis = lis.next

        assert elements == [1, 1, 2, 3, 4, 4, 5, 6]
