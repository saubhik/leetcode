from typing import List

# class Solution:
#     # [[0,4],[1,3],[2,4],[3,4],[1,2],[2,3]]
#     # overlap lists -> O(n^2) time, O(n^2) space.
#     # [0,4]: [[1,3],[2,4],[3,4],[1,2],[2,3]]
#     # [1,3]: [[0,4],[2,4],[1,2],[2,3]]
#     # [2,4]: [[0,4],[1,3],[3,4],[2,3]]
#     # [3,4]: [[0,4],[2,4]]
#     # [1,2]: [[0,4],[1,3]]
#     # [2,3]: [[0,4],[1,3],[2,4]]
#     # next step: remove [0,4]
#     # [1,3]: [[2,4],[1,2],[2,3]]
#     # [2,4]: [[1,3],[3,4],[2,3]]
#     # [3,4]: [[2,4]]
#     # [1,2]: [[1,3]]
#     # [2,3]: [[1,3],[2,4]]
#     # next step: remove [1,3]
#     # [2,4]: [[3,4],[2,3]]
#     # [3,4]: [[2,4]]
#     # [1,2]: []
#     # [2,3]: [[2,4]]
#     # next step: remove [2,4]
#     # [3,4]: []
#     # [1,2]: []
#     # [2,3]: []
#     # done.
#     # Remove nodes which have most connections, till no one has any connection.
#     def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
#         if not intervals:
#             return 0
#
#         overlap_list = defaultdict(list)
#
#         class Node:
#             def __init__(self, ls: List[int]):
#                 self.st = ls[0]
#                 self.en = ls[1]
#
#         def overlap(node_one: Node, node_two: Node):
#             return (
#                 (
#                     # ..[...]..
#                     # [...]...
#                     node_two.st
#                     < node_one.st
#                     < node_two.en
#                     <= node_one.en
#                 )
#                 or (
#                     # ...[...]...
#                     # ....[.]....
#                     node_one.st
#                     <= node_two.st
#                     < node_two.en
#                     <= node_one.en
#                 )
#                 or (
#                     # ...[...]...
#                     # .....[...].
#                     node_one.st
#                     <= node_two.st
#                     < node_one.en
#                     < node_two.en
#                 )
#             )
#
#         # O(n) time
#         nodes = []
#         for interval in intervals:
#             node = Node(interval)
#             nodes.append(node)
#
#         # O(n^2) time, O(n^2) space
#         for curr_node in nodes:
#             for other_node in nodes:
#                 if curr_node != other_node:
#                     # different node objects but same interval can overlap
#                     if overlap(curr_node, other_node):
#                         overlap_list[curr_node].append(other_node)
#                         overlap_list[other_node].append(curr_node)
#
#         def get_max_overlap_node():
#             # O(n) time
#             max_count, max_node = 0, None
#             for node, edges in overlap_list.items():
#                 if len(edges) > max_count:
#                     max_count = len(edges)
#                     max_node = node
#             return max_node
#
#         ans = 0
#
#         # O(n^2) time
#         max_node = get_max_overlap_node()
#         while max_node is not None:
#             nbrs = overlap_list.pop(max_node)
#             for nbr in nbrs:
#                 overlap_list[nbr].remove(max_node)
#             max_node = get_max_overlap_node()
#             ans += 1
#
#         return ans


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        dp, n = [], len(intervals)

        intervals.sort(key=lambda interval: interval[0])

        for i in range(n):
            max_dp_j = 0
            for j in range(i):
                if intervals[j][1] <= intervals[i][0]:
                    if dp[j] > max_dp_j:
                        max_dp_j = dp[j]
            dp.append(1 + max_dp_j)

        return n - max(dp, default=0)
