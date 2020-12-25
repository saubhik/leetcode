from unittest import TestCase


# Definition for a Node.
class Node:
    def __init__(
        self,
        val: int = 0,
        left: "Node" = None,
        right: "Node" = None,
        next: "Node" = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    """
    Maintain next_level_start and next_level_end and walk via next links.

    Time Complexity: O(n).
    Space Complexity: O(1).
    """

    def connect(self, root: "Node") -> "Node":
        node, next_level_start, next_level_last = root, None, None
        while node:
            if node.left:
                if next_level_last:
                    next_level_last.next = node.left

                next_level_last = node.left

                if not next_level_start:
                    next_level_start = node.left

            if node.right:
                if next_level_last:
                    next_level_last.next = node.right

                next_level_last = node.right

                if not next_level_start:
                    next_level_start = node.right

            if node.next:
                node = node.next
            else:
                # New level starts.
                node = next_level_start
                next_level_start = None
                next_level_last = None

        return root


class TestConnect(TestCase):
    """
    Iteration 1: node=1
    next_level_last=2, next_level_start=2, 2->3, next_level_last=3, node=2
    Iteration 2: node=2
    next_level_last=4, next_level_start=4, 4->5, next_level_last=5, node=3
    Iteration 3: node=3
    5->7, next_level_last=7, node=4
    ...
    """

    def test_example_1(self):
        root = Node(val=1)
        root.left = Node(val=2)
        root.right = Node(val=3)
        root.left.left = Node(val=4)
        root.left.right = Node(val=5)
        root.right.right = Node(val=7)

        node = Solution().connect(root=root)

        assert node.val == 1
        assert node.next is None

        assert node.left.val == 2
        assert node.right.val == 3
        assert node.left.next == node.right

        assert node.left.left.val == 4
        assert node.left.right.val == 5
        assert node.left.left.next == node.left.right

        assert node.right.right.val == 7
        assert node.left.right.next == node.right.right
