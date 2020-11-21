from typing import List


class Solution:
    # Time Complexity:
    #   O(logn) in best case, and O(n) in worst case.
    #   With duplicates, sometimes we do not know which way to explore.
    #   Worst Case: All equal in nums and target does not belong to nums.
    # Space Complexity: O(1).
    def search(self, nums: List[int], target: int) -> bool:
        def _is_in_first(elem: int):
            return elem >= nums[0]

        def _check_and_update(mid_index: int, elem: int, start: int, end: int):
            if elem < nums[mid_index]:
                end = mid_index - 1
            else:
                start = mid_index + 1

            return start, end

        start, end, linear_search = 0, len(nums) - 1, False

        while start <= end:
            mid = end - (end - start) // 2

            if nums[mid] == target:
                return True

            # We do not know which way to explore if since mid could be both in
            # first and second sorted array.
            if nums[mid] == nums[0]:
                linear_search = True
                break

            mid_in_first, target_in_first = (
                _is_in_first(elem=nums[mid]),
                _is_in_first(elem=target),
            )

            if mid_in_first and target_in_first:
                start, end = _check_and_update(
                    mid_index=mid, elem=target, start=start, end=end
                )
            elif mid_in_first and not target_in_first:
                start = mid + 1
            elif not mid_in_first and target_in_first:
                end = mid - 1
            else:
                # mid in second, and target in second
                start, end = _check_and_update(
                    mid_index=mid, elem=target, start=start, end=end
                )

        if linear_search:
            # Include end also.
            for i in range(start, end + 1):
                if nums[i] == target:
                    return True

        return False
