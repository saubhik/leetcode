from collections import deque
from typing import Optional
from unittest import TestCase


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def __init__(self, root: TreeNode):
        # O(n) space.
        values = deque([])

        # O(n) time, O(h) space.
        def _dfs(node: Optional[TreeNode]):
            if not node:
                return
            _dfs(node=node.left)
            values.append(node.val)
            _dfs(node=node.right)

        _dfs(node=root)
        self.values = values

    def next(self) -> int:
        # O(1) time.
        return self.values.popleft()

    def hasNext(self) -> bool:
        # O(1) time.
        return bool(self.values)


class BSTIteratorTwo:
    def __init__(self, root: TreeNode):
        self.stack = []
        self._maintain_stack(node=root)

    def _maintain_stack(self, node: TreeNode):
        # O(h) space.
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        # N stack pushes and N stack pops = 2N O(1) operations.
        # Total number of calls = N.
        # Amortized time complexity = O(1).
        node = self.stack.pop()
        if node.right:
            self._maintain_stack(node=node.right)
        return node.val

    def hasNext(self) -> bool:
        # O(1) time.
        return len(self.stack) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()


class TestBSTIterator(TestCase):
    def test_example_1(self):
        for iterator in (BSTIterator, BSTIteratorTwo):
            root = TreeNode(val=7)
            root.left = TreeNode(val=3)
            root.right = TreeNode(val=15)
            root.right.left = TreeNode(val=9)
            root.right.right = TreeNode(val=20)

            bst_iterator = iterator(root=root)

            assert bst_iterator.next() == 3
            assert bst_iterator.next() == 7
            assert bst_iterator.hasNext() is True
            assert bst_iterator.next() == 9
            assert bst_iterator.hasNext() is True
            assert bst_iterator.next() == 15
            assert bst_iterator.hasNext() is True
            assert bst_iterator.next() == 20
            assert bst_iterator.hasNext() is False
