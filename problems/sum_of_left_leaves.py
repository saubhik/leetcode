# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # BFS
    # Time: O(n)
    # Space: O(n)
    # where n is the number of nodes
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root is None:
            return 0

        level_nodes = [(False, root)]

        left_leaves_sum = 0

        while level_nodes:
            next_level_nodes = []
            for is_left, node in level_nodes:
                if is_left and node.left is None and node.right is None:
                    left_leaves_sum += node.val
                else:
                    if node.left is not None:
                        next_level_nodes.append((True, node.left))
                    if node.right is not None:
                        next_level_nodes.append((False, node.right))
            level_nodes = next_level_nodes

        return left_leaves_sum
