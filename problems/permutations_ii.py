from typing import List


class Solution:
    # Time Complexity:
    #   1 + n*(n-1) + n*(n-1)*(n-2) + ... + n! = O(sum_{k=1}_{k=N}(P(N,k)))
    # Space Complexity: O(n)
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        perms = []

        def _backtrack(visited: List[int], current: List[int], current_length: int):
            if current_length == n:
                perms.append(list(current))
                return

            considered = set()

            for i in range(n):
                if i not in visited and nums[i] not in considered:
                    current.append(nums[i])
                    visited.append(i)
                    _backtrack(
                        visited=visited,
                        current=current,
                        current_length=current_length + 1,
                    )
                    visited.pop()
                    current.pop()

                    considered.add(nums[i])

        _backtrack(visited=[], current=[], current_length=0)

        return perms
