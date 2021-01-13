import unittest

from linked_list_cycle_ii import ListNode, Solution


class TestLinkedListCycleII(unittest.TestCase):
    def test_example_1(self):
        head = ListNode(x=3)
        head.next = ListNode(x=2)
        head.next.next = ListNode(x=0)
        head.next.next.next = ListNode(x=-4)
        head.next.next.next.next = head.next

        assert Solution().detectCycle(head=head) == head.next

    def test_example_2(self):
        head = ListNode(x=1)
        head.next = ListNode(x=2)
        head.next.next = head

        assert Solution().detectCycle(head=head) == head

    def test_example_3(self):
        head = ListNode(x=1)

        assert Solution().detectCycle(head=head) is None

    def test_example_4(self):
        assert Solution().detectCycle(head=None) is None

    def test_example_5(self):
        head = ListNode(x=1)
        head.next = ListNode(x=2)

        assert Solution().detectCycle(head=head) is None
