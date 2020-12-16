from unittest import TestCase


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Time Complexity: O(n).
    # Space Complexity: O(1).
    def plusOne(self, head: ListNode) -> ListNode:
        sentinel = ListNode(val=0, next=head)
        last_non_nine_node = None

        # Increment last non-9 value.
        curr = sentinel
        while curr:
            if curr.val != 9:
                last_non_nine_node = curr
            curr = curr.next
        last_non_nine_node.val += 1

        # Set all following 9s to 0.
        curr = last_non_nine_node.next
        while curr:
            curr.val = 0
            curr = curr.next

        return sentinel.next if sentinel.val == 0 else sentinel


class TestSolution(TestCase):
    def test_example_1(self):
        head = ListNode(val=1)
        head.next = ListNode(val=2)
        head.next.next = ListNode(val=3)

        node = Solution().plusOne(head=head)
        assert node.val == 1
        assert node.next.val == 2
        assert node.next.next.val == 4
        assert node.next.next.next is None

    def test_example_2(self):
        head = ListNode(val=0)

        node = Solution().plusOne(head=head)

        assert node.val == 1
        assert node.next is None

    def test_example_3(self):
        head = ListNode(val=9)

        node = Solution().plusOne(head=head)

        assert node.val == 1
        assert node.next.val == 0
        assert node.next.next is None
