from unittest import TestCase

from add_two_numbers_ii import Solution, ListNode


class TestAddTwoNumbersII(TestCase):
    def test_example_1(self):
        l1 = ListNode(
            val=7, next=ListNode(val=2, next=ListNode(val=4, next=ListNode(val=3)))
        )

        l2 = ListNode(val=5, next=ListNode(val=6, next=ListNode(val=4)))

        l3 = Solution().addTwoNumbers(l1=l1, l2=l2)

        assert l3.val == 7
        assert l3.next.val == 8
        assert l3.next.next.val == 0
        assert l3.next.next.next.val == 7
        assert l3.next.next.next.next is None
