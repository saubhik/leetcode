import unittest

from insertion_sort_list import Solution, ListNode


class TestInsertionSortList(unittest.TestCase):
    def test_example_1(self):
        head = ListNode(val=4)
        head.next = ListNode(val=2)
        head.next.next = ListNode(val=1)
        head.next.next.next = ListNode(val=3)

        head = Solution().insertionSortList(head=head)
        assert head.val == 1
        assert head.next.val == 2
        assert head.next.next.val == 3
        assert head.next.next.next.val == 4

    def test_example_2(self):
        head = ListNode(val=-1)
        head.next = ListNode(val=5)
        head.next.next = ListNode(val=3)
        head.next.next.next = ListNode(val=4)
        head.next.next.next.next = ListNode(val=0)

        head = Solution().insertionSortList(head=head)
        assert head.val == -1
        assert head.next.val == 0
        assert head.next.next.val == 3
        assert head.next.next.next.val == 4
        assert head.next.next.next.next.val == 5
