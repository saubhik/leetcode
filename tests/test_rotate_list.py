import unittest

from rotate_list import Solution, ListNode


class TestRotateList(unittest.TestCase):
    def test_example_1(self):
        head = ListNode(
            val=1,
            next=ListNode(
                val=2,
                next=ListNode(
                    val=3, next=ListNode(val=4, next=ListNode(val=5, next=None))
                ),
            ),
        )
        node = Solution().rotateRight(head=head, k=2)
        assert node.val == 4
        assert node.next.val == 5
        assert node.next.next.val == 1
        assert node.next.next.next.val == 2
        assert node.next.next.next.next.val == 3
        assert node.next.next.next.next.next is None

    def test_example_2(self):
        head = ListNode(val=0, next=ListNode(val=1, next=ListNode(val=2, next=None)))
        node = Solution().rotateRight(head=head, k=4)
        assert node.val == 2
        assert node.next.val == 0
        assert node.next.next.val == 1
        assert node.next.next.next is None

    def test_example_3(self):
        head = ListNode(val=1)
        node = Solution().rotateRight(head=head, k=1)
        assert node.val == 1
        assert node.next is None
