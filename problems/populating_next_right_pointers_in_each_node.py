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
    # Using DFS.
    # Time Complexity: O(nlgn).
    # Space Complexity: O(n) due to function call stack.
    def connect(self, root: "Node") -> "Node":
        if not root:
            return root

        connect_left, connect_right = root.left, root.right
        while connect_left and connect_right:
            connect_left.next = connect_right
            connect_left, connect_right = connect_left.right, connect_right.left

        self.connect(root=root.left)
        self.connect(root=root.right)

        return root


class OfficialSolution:
    # Using O(1) space and O(n) time.
    def connect(self, root: "Node") -> "Node":
        if not root:
            return root

        leftmost = root
        while leftmost.left:
            node = leftmost
            while node:
                node.left.next = node.right
                if node.next:
                    node.right.next = node.next.left
                node = node.next

            leftmost = leftmost.left

        return root
