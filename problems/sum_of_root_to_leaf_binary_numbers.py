# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Normal DFS.
    # Time: O(H) = O(N) in worst case of degenerate tree.
    # Space: O(H) = O(N) in worst case of degenerate tree, due to recursion call stack.
    def sumRootToLeaf(self, root: TreeNode, running_sum: int = 0) -> int:
        if root is None:
            return 0

        running_sum = running_sum * 2 + root.val
        left_sum, right_sum = 0, 0

        if root.left is not None:
            left_sum = self.sumRootToLeaf(root=root.left, running_sum=running_sum)

        if root.right is not None:
            right_sum = self.sumRootToLeaf(root=root.right, running_sum=running_sum)

        if root.left is None and root.right is None:
            # leaf
            return running_sum

        return left_sum + right_sum
