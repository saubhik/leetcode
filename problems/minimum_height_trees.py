from typing import List


class Solution:
    # Time Complexity: O(|V|).
    # Space Complexity: O(|V|).
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # Create adjacency list representation of the graph.
        # O(|V|) time.
        graph = [[] for _ in range(n)]

        # O(|V| - 1) time.
        # O(|V| + |E|) = O(|V|) space.
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        # O(|V|) time.
        # O(|V|) space.
        leaves = [i for i in range(n) if len(graph[i]) == 1]

        if not leaves:
            return [0]

        remaining_nodes = n

        # O(|V| + |E|) = O(|V| + |V| - 1) = O(|V|) time.
        while remaining_nodes > 2:
            next_leaves = []

            while leaves:
                leaf = leaves.pop()

                leaf_neighbor: int
                for leaf_neighbor in graph[leaf]:
                    # Remove edge from leaf to leaf_neighbor.
                    graph[leaf_neighbor].remove(leaf)

                    # Leaf for next level.
                    if len(graph[leaf_neighbor]) == 1:
                        next_leaves.append(leaf_neighbor)

                # Remove leaf from graph.
                graph[leaf] = []
                remaining_nodes -= 1

            leaves = next_leaves

        return leaves
