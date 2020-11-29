from collections import deque
from typing import List


class Solution:
    # Time Complexity:
    #   O(n) since every element is processed at mose twice
    #   Once while appending the index, and then popping the index.
    # Space Complexity:
    #   O(k) for the deque.
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans, queue = [], deque()

        for i in range(len(nums)):
            # Size constraint.
            if queue and queue[-1] - queue[0] + 1 >= k:
                queue.popleft()

            # Keep only a decreasing sequence in the queue.
            while queue and nums[queue[0]] < nums[i]:
                queue.popleft()
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()

            queue.append(i)
            if i + 1 >= k:
                ans.append(nums[queue[0]])

        return ans
