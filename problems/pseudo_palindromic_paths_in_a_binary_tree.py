from unittest import TestCase


# Definition for a binary tree root.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # DFS with maintaining values in a path in a hash set.
    # Time Complexity: O(n).
    # Space Complexity: O(h) = O(n) in worst case.
    def pseudoPalindromicPaths(self, root: TreeNode) -> int:
        count = 0
        path_values = set()
        counter = {}

        def compute(root: TreeNode):
            counter[root.val] = counter.get(root.val, 0) + 1

            if root.val in path_values:
                path_values.remove(root.val)
            else:
                path_values.add(root.val)

            if not root.left and not root.right:
                if len(path_values) < 2:
                    nonlocal count
                    count += 1

            if root.left:
                compute(root=root.left)

            if root.right:
                compute(root=root.right)

            counter[root.val] -= 1

            # Remove root.val from path_values.
            # If it's a new root.val, remove it.
            # Else, keep one remaining root.val if count is odd.
            if counter[root.val] % 2 == 1:
                path_values.add(root.val)
            else:
                path_values.remove(root.val)
                if counter[root.val] == 0:
                    del counter[root.val]

        compute(root=root)
        return count


class SolutionTwo:
    # Using bit manipulation for checking existence of palindromic configuration
    # on-the-fly.
    # Time Complexity: O(n).
    # Space Complexity: O(h) space.
    def pseudoPalindromicPaths(self, root: TreeNode, path: int = 0) -> int:
        path ^= 1 << root.val
        if not root.left and not root.right:
            # At most one 1 (odd) parity allowed in path.
            return 1 if path & (path - 1) == 0 else 0

        counts = 0
        if root.left:
            counts += self.pseudoPalindromicPaths(root=root.left, path=path)
        if root.right:
            counts += self.pseudoPalindromicPaths(root=root.right, path=path)

        return counts


class TestPseudoPalindromicPaths(TestCase):
    def test_example_1(self):
        root = TreeNode(val=2)
        root.left = TreeNode(val=3)
        root.right = TreeNode(val=1)
        root.left.left = TreeNode(val=3)
        root.left.right = TreeNode(val=1)
        root.right.right = TreeNode(val=1)

        assert Solution().pseudoPalindromicPaths(root=root) == 2
        assert SolutionTwo().pseudoPalindromicPaths(root=root) == 2

    def test_example_2(self):
        root = TreeNode(val=2)
        root.left = TreeNode(val=1)
        root.right = TreeNode(val=1)
        root.left.left = TreeNode(val=1)
        root.left.right = TreeNode(val=3)
        root.left.right.right = TreeNode(val=1)

        assert Solution().pseudoPalindromicPaths(root=root) == 1
        assert SolutionTwo().pseudoPalindromicPaths(root=root) == 1

    def test_example_3(self):
        assert Solution().pseudoPalindromicPaths(root=TreeNode(val=9)) == 1
        assert SolutionTwo().pseudoPalindromicPaths(root=TreeNode(val=9)) == 1
