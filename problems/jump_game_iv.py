from typing import List
from unittest import TestCase


class Solution:
    """
    Breadth First Search.

    100,-23,-23,404,100,23,23,23,3,404
    Once considered we will not reconsider a node.

    i=0;jumps=0
    i=1,4;jumps=1
    i=2,3,5;jumps=2
    i=9,6,7;jumps=3

    We are considering every node exactly once.

    Time Complexity: O(n).
    Space Complexity: O(n).
    """

    def minJumps(self, arr: List[int]) -> int:
        jumps = 0
        if len(arr) == 0:
            return jumps

        occurrences = {}  # Value to indices map.
        for i in range(len(arr)):
            if arr[i] in occurrences:
                occurrences[arr[i]].append(i)
            else:
                occurrences[arr[i]] = [i]

        current_nodes = [0]  # Nodes in current level.
        visited = {0}  # If a node is in current level it's already visited.
        while current_nodes:
            next_level_nodes = []  # Nodes in next level.
            while current_nodes:
                node = current_nodes.pop()

                if node == len(arr) - 1:
                    return jumps

                # Get all the neighbors which are equal valued.
                for neighbor in occurrences[arr[node]]:
                    if neighbor not in visited:
                        next_level_nodes.append(neighbor)
                        visited.add(neighbor)

                occurrences[arr[node]].clear()  # No need of these nodes anymore.

                for neighbor in (node - 1, node + 1):
                    if 0 <= neighbor < len(arr) and neighbor not in visited:
                        next_level_nodes.append(neighbor)
                        visited.add(neighbor)

            jumps += 1
            current_nodes = next_level_nodes


class SolutionTwo:
    """
    Bidirectional Breadth First Search.
    Time Complexity: O(n).
    Space Complexity: O(n).
    """

    def minJumps(self, arr: List[int]) -> int:
        jumps = 0
        if len(arr) <= 1:
            return jumps

        occurrences = {}  # Value to indices map.
        for i in range(len(arr)):
            if arr[i] in occurrences:
                occurrences[arr[i]].append(i)
            else:
                occurrences[arr[i]] = [i]

        current_nodes = {0}  # Nodes in current front level.
        other_nodes = {len(arr) - 1}  # Nodes in current back level.
        visited = {0, len(arr) - 1}
        while current_nodes:

            if len(current_nodes) > len(other_nodes):
                current_nodes, other_nodes = other_nodes, current_nodes

            next_level_nodes = set()  # Nodes in next level.

            while current_nodes:
                node = current_nodes.pop()

                # Get all the neighbors which are equal valued.
                for neighbor in occurrences[arr[node]]:
                    if neighbor in other_nodes:
                        return jumps + 1
                    if neighbor not in visited:
                        next_level_nodes.add(neighbor)
                        visited.add(neighbor)

                occurrences[arr[node]].clear()  # No need of these nodes anymore.

                for neighbor in (node - 1, node + 1):
                    if 0 <= neighbor < len(arr):
                        if neighbor in other_nodes:
                            return jumps + 1
                        if neighbor not in visited:
                            next_level_nodes.add(neighbor)
                            visited.add(neighbor)

            jumps += 1
            current_nodes = next_level_nodes


class TestMinJumps(TestCase):
    def test_example_1(self):
        assert (
            Solution().minJumps(arr=[100, -23, -23, 404, 100, 23, 23, 23, 3, 404]) == 3
        )
        assert (
            SolutionTwo().minJumps(arr=[100, -23, -23, 404, 100, 23, 23, 23, 3, 404])
            == 3
        )

    def test_example_2(self):
        assert Solution().minJumps(arr=[7]) == 0
        assert SolutionTwo().minJumps(arr=[7]) == 0

    def test_example_3(self):
        assert Solution().minJumps(arr=[7, 6, 9, 6, 9, 6, 9, 7]) == 1
        assert SolutionTwo().minJumps(arr=[7, 6, 9, 6, 9, 6, 9, 7]) == 1

    def test_example_4(self):
        assert Solution().minJumps(arr=[6, 1, 9]) == 2
        assert SolutionTwo().minJumps(arr=[6, 1, 9]) == 2
