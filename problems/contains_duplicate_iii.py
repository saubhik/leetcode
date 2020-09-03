from typing import List


class Solution:
    # This gets TLEd.
    # Time: O(n*k)
    # Space: O(1)
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        n = len(nums)
        for i in range(n):
            for j in range(max(i - k, 0), min(i + k + 1, n)):
                if j != i and abs(nums[i] - nums[j]) <= t:
                    return True
        return False


class SolutionTwo:
    # Time: O(n)
    # Space: O(min(n,k))
    # maintain buckets [0,t],[t+1,2t+1],...
    # maintain only k buckets
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if t < 0:
            return False

        buckets = {}

        def get_id(num):
            return (num + 1) // (t + 1) if t == 0 else num // t

        for i, num in enumerate(nums):
            bucket_id = get_id(num=num)
            if bucket_id in buckets:
                return True
            if (bucket_id - 1) in buckets and num - buckets[bucket_id - 1] <= t:
                return True
            if (bucket_id + 1) in buckets and buckets[bucket_id + 1] - num <= t:
                return True
            buckets[bucket_id] = num
            if i >= k:
                del buckets[get_id(num=nums[i - k])]
        return False
