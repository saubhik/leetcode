from unittest import TestCase


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Time Complexity: O(n).
    # Space Complexity: O(1) additional space.
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return head

        pre, i, j = None, head, head.next

        while j:
            i.next = j.next
            j.next = i

            if pre:
                pre.next = j
            else:
                head = j

            # j -> i -> ...
            pre = i
            i = pre.next
            j = i.next if i else None

        return head


class TestSwapPairs(TestCase):
    def test_example_1(self):
        head = ListNode(val=1)
        head.next = ListNode(val=2)
        head.next.next = ListNode(val=3)
        head.next.next.next = ListNode(val=4)

        node = Solution().swapPairs(head=head)

        assert node.val == 2
        assert node.next.val == 1
        assert node.next.next.val == 4
        assert node.next.next.next.val == 3
        assert node.next.next.next.next is None

    def test_example_2(self):
        assert Solution().swapPairs(head=None) is None

    def test_example_3(self):
        head = ListNode(val=1)
        assert Solution().swapPairs(head=head) is head
