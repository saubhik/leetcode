# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Depth First Search with Re-Linking Nodes On-The-Fly
    # Time Complexity: O(n)
    # Space Complexity: O(H) = O(n) in worst case.
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def _dfs(node: TreeNode):
            head = tail = node
            if node.left:
                head, tail = _dfs(node=node.left)
                node.left = None
                tail.right = node
                tail = tail.right
            if node.right:
                node.right, tail = _dfs(node=node.right)
            return head, tail

        return _dfs(node=root)[0]
