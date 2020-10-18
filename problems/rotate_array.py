from math import gcd
from typing import List


class Solution:
    """
    Would like one-pass (O(n)) and O(1) space.
    Consider nums=[1,2,3,4,5,6,7], k=3.
    We have i -> (i+k)%n.
    Algorithm Dry Run:
        Send i to (i+k)%n.
        nums=[?,2,3,1,5,6,7].
        Now we have tmp=4. Where should it go?
        Since it's index is j=(i+k)%n, it should go to (j+k)%n.
        nums=[?,2,3,1,5,6,4].
        Now we have tmp=7. Where should it go?
        nums=[?,2,7,1,5,6,4].
        Now we have tmp=3. Where should it go?
        nums=[?,2,7,1,5,3,4].
        Now we have tmp=6. Where should it go?
        nums=[?,6,7,1,5,3,4].
        Now we have tmp=2. Where should it go?
        nums=[?,6,7,1,2,3,4].
        Now we have tmp=5. Where should it go?
        nums=[5,6,7,1,2,3,4].
        Done.
    """

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        Time Complexity: O(n). One-Pass.
        Space Complexity: O(1) additional space.
        This is modifying the array in-place.
        """
        if k == 0:
            return

        n, tmp_idx = len(nums), 0

        def _rotate(tmp_idx: int, rng: int):
            tmp = nums[tmp_idx]
            for i in range(rng):
                nxt_tmp_idx = (tmp_idx + k) % n
                tmp_idx, tmp, nums[nxt_tmp_idx] = nxt_tmp_idx, nums[nxt_tmp_idx], tmp

        div = gcd(n, k)

        if div > 1:
            for _ in range(div):
                _rotate(tmp_idx=tmp_idx, rng=n // div)
                tmp_idx += 1
        else:
            _rotate(tmp_idx=tmp_idx, rng=n)


class OfficialSolutionApproach4:
    """
    == Approach 4: Using Reverse ==
    == Algorithm ==
    This approach is based on the fact that when we rotate the array k times, k elements
    from the back end of the array come to the front and the rest of the elements from
    the front shift backwards.
    In this approach, we firstly reverse all the elements in the array.
    Then, reversing the first k elements, followed by reversing the rest n-k elements
    gives us the required result.

    1,2,3,4,5,6,7; k=3
    7,6,5,4,3,2,1
    5,6,7,4,3,2,1
    5,6,7,1,2,3,4

    == Complexity Analysis ==
    Time Complexity: O(n), n elements are reversed a total of 3 times.
    Space Complexity: O(1).
    """

    def rotate(self, nums: List[int], k: int) -> None:
        def _reverse(start: int, end: int) -> None:
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start, end = start + 1, end - 1

        n = len(nums)

        _reverse(start=0, end=n - 1)
        _reverse(start=0, end=k - 1)
        _reverse(start=k, end=n - 1)
