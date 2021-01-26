class Solution:
    # Straight Forward.
    # Time Complexity: O(n).
    # Space Complexity: O(1),
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        dist = k  # Initialize with k to not go inside if condition.
        for num in nums:
            if num == 1:
                if dist < k:
                    return False
                dist = 0
            else:
                dist += 1
        return True
