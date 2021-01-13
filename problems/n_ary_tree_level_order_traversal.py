from collections import deque
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root) -> List[List[int]]:
        # Runtime: 52 ms, faster than 76.63% of Python3 online submissions for N-ary
        # Tree Level Order Traversal. Memory Usage: 15.6 MB, less than 70.35% of
        # Python3 online submissions for N-ary Tree Level Order Traversal.
        result = list()

        if root:
            queue = deque([root])

            while queue:
                level_size = len(queue)
                level_nodes = list()

                for _ in range(level_size):
                    node = queue.popleft()
                    level_nodes.append(node.val)
                    for child in node.children:
                        queue.append(child)

                result.append(level_nodes)

        return result
