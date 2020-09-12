from typing import List


class SparseVector:
    def __init__(self, nums: List[int]):
        self.length = len(nums)
        # store the SparseVector efficiently
        self.store = {i: num for i, num in enumerate(nums) if num != 0}

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: "SparseVector") -> int:
        ans = 0
        for i in self.store.keys():
            if i in vec.store:
                ans += self.store[i] * vec.store[i]
        return ans


# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
