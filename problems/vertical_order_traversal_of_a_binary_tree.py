from collections import deque
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        nodes = []

        queue = deque([(root, 0, 0)])
        while queue:
            node, x, y = queue.popleft()

            nodes.append((x, y, node.val))

            if node.left is not None:
                queue.append((node.left, x - 1, y + 1))

            if node.right is not None:
                queue.append((node.right, x + 1, y + 1))

        nodes.sort()

        result = [[]]
        last_x = nodes[0][0]
        for x, y, val in nodes:
            if x != last_x:
                result.append([val])
            else:
                result[-1].append(val)
            last_x = x

        return result
