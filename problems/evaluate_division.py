from collections import defaultdict
from typing import List


class OfficialSolution:
    """
    == Overview ==
    The problem can be solved with 2 important data structures, namely Graph and Union-
    Find.
    """

    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        """
        == Approach 1: Path Search in Graph ==
        == Intuition ==
        First, let us look at the example given in the problem description. Given two
        equations, namely a/b=2, b/c=3, we could derive the following equations:
        - 1) b/a = 1/2, c/b = 1/3
        - 2) a/c = a/b . b/c = 6
        Each division implies the reverse of the division, which is how we derive the
        equations in (1). While by chaining up equations, we could obtain new equations
        in (2).

        We could reformulate the equations with the graph data structure, where each
        variable can be represented as a node in the graph, and the division
        relationship between variables can be modeled as edge with direction and weight.

        The direction of edge indicates the order of division, and the weight of edge
        indicates the result of division.

        With the above formulation, we then can convert the initial equations into the
        following graph:

          a/b=2      b/c=3
        a ------> b -------> c
        a <------- b <------ c
          b/a=1/2    c/b=1/3

        To evaluate the query (e.g. a/c = ?) is equivalent to performing two tasks on
        the graph:
        1. Find if there exists a path between the two entities.
        2. If so, calculate the cumulative products along the paths.

        In the above example (a/c = ?), we could find a path between them, and the
        cumulative products are 6. As a result, we can conclude that the result of
        a/c is 2.3 = 6.

        == Algorithm ==
        As one can see, we just transform the problem into a path searching problem in
        a graph.

        More precisely, we can reinterpret the problem as "given two nodes, we are asked
        to check if there exists a path between them. If so, we should return the
        cumulative products along the path as the result."

        Given the above problem statement, it seems intuitive that one could apply the
        backtracking algorithm, or sometimes people might call it DFS (Depth-First
        Search).

        Essentially, we can break down the algorithm into 2 steps overall:
        Step 1. We build the graph out of the list of input equations.
            - Each equation corresponds to two edges in the graph.
        Step 2. Once the graph is built, we then can evaluate the query one by one.
            - The evaluation of the query is done via searching the path between the
            given two variables.
            - Other than the above searching operation, we need to handle two
            exceptional cases as follows:
                - Case 1. If either of the nodes does not exist in the graph, i.e. the
                variables did not appear in any of the input equations, then we can
                assert that no path exists.
                - Case 2. If the origin and the destination are the same node, i.e. a/a,
                we can assume that therre exists an invisible self-loop path for each
                node and the result is 1.

        Note: With the built graph, one could also apply the BFS (Breadth-First Search)
        algorithm, as opposed to the DFS algorithm we employed.

        However, the essence of the solution remains the same, i.e. we are searching for
        a path in a graph.

        == Complexity Analysis ==
        Let N be the number of input equations and M be the number of queries.
        Time Complexity:
            O(MN)
            - First of all, we iterate through the equations to build a graph. Each
            equation takes O(1) time to process. Therefore, this step will take O(N)
            time in total.
            - For each query, we need to traverse the graph. In the worst case, we might
            need to traverse the entire graph, which could take O(N). Hence, in total,
            the evaluation of queries could take M*O(N) = O(MN).
            - To sum up, the overall time complexity of the algorithm is
            O(N) + O(MN) = O(MN).

        Space Complexity:
            O(N)
            - We build a graph out of the equations. In the worst case where there is no
            overlapping among the equations, we would have N edges and 2N nodes in the
            graph. Therefore, the space complexity of the graph is O(N+2N)=O(3N)=O(N).
            - Since we employ the recursion in the backtracking, we would consume
            additional memory in the function call stack, which could amount to O(N)
            space.
            - In addition, we used a set
        """

        # Graph as Adjacency Lists
        graph = defaultdict(defaultdict)

        for (numerator, denominator), value in zip(equations, values):
            graph[numerator][denominator] = value
            graph[denominator][numerator] = 1 / value

        def dfs(curr: str, end: str, visited=None, cum_weight: float = 1.0) -> float:
            if visited is None:
                visited = set()

            if curr == end:
                return cum_weight

            visited.add(curr)

            for node, value in graph[curr].items():
                if node in visited:
                    continue

                ans = dfs(
                    curr=node, end=end, visited=visited, cum_weight=cum_weight * value
                )

                if ans != -1.0:
                    return ans

            visited.remove(curr)

            return -1.0

        ans = []
        for (start, end) in queries:
            if start not in graph:
                ans.append(-1.0)
            else:
                ans.append(dfs(curr=start, end=end))

        return ans
