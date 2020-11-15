# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Time Complexity: O(n). (Low is far left leaf, high is far right leaf)
    # Space Complexity: O(H). Worst case is O(n).
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if low > high or not root:
            return 0

        return (
            self.rangeSumBST(root=root.left, low=low, high=min(root.val, high))
            + self.rangeSumBST(root=root.right, low=max(root.val, low), high=high)
            + (root.val if low <= root.val <= high else 0)
        )
