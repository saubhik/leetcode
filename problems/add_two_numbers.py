from unittest import TestCase


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Straight Forward.
    # Time Complexity: O(max(n1, n2)).
    # Space Complexity: O(1) additional space.
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry, list_node = 0, ListNode()
        sentinel = list_node

        while l1 or l2 or carry:
            _sum = carry

            if l1:
                _sum += l1.val
                l1 = l1.next

            if l2:
                _sum += l2.val
                l2 = l2.next

            carry, val = divmod(_sum, 10)

            list_node.next = ListNode(val=val)
            list_node = list_node.next

        return sentinel.next


class TestAddTwoNumbers(TestCase):
    def test_example_1(self):
        l1 = ListNode(val=2, next=ListNode(val=4, next=ListNode(val=3)))
        l2 = ListNode(val=5, next=ListNode(val=6, next=ListNode(val=4)))

        node = Solution().addTwoNumbers(l1=l1, l2=l2)

        assert node.val == 7
        assert node.next.val == 0
        assert node.next.next.val == 8
        assert node.next.next.next is None

    def test_example_2(self):
        l1 = ListNode()
        l2 = ListNode()

        node = Solution().addTwoNumbers(l1=l1, l2=l2)

        assert node.val == 0
        assert node.next is None

    def test_example_3(self):
        l1_sentinel = curr = ListNode()
        for val in (9, 9, 9, 9, 9, 9, 9):
            curr.next = ListNode(val=val)
            curr = curr.next

        l2_sentinel = curr = ListNode()
        for val in (9, 9, 9, 9):
            curr.next = ListNode(val=val)
            curr = curr.next

        node = Solution().addTwoNumbers(l1=l1_sentinel.next, l2=l2_sentinel.next)

        values = []
        while node:
            values.append(node.val)
            node = node.next

        assert values == [8, 9, 9, 9, 0, 0, 0, 1]
