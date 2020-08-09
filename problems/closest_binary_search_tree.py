class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Time: O(lgn) normal case, O(n) worst case
    # Space: O(1)
    def closestValue(self, root: TreeNode, target: float) -> int:
        node, closest = root, root.val
        while node:
            if node.val == target:
                return node.val

            if abs(node.val - target) < abs(closest - target):
                closest = node.val

            node = node.left if target < node.val else node.right

        return closest
