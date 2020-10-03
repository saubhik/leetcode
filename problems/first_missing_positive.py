from typing import List


class OfficialSolution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        == Approach 1: Index as a hash key. ==

        == Data Clean Up ==
        First of all, let's get rid of negative numbers and zeros since there is no
        need of them. One could get rid of all numbers larger than n as well, since the
        first missing positive is for sure smaller or equal to n+1. The case when the
        first missing positive is equal to n+1 will be treated separately.
        What does it mean - to get rid of, if one has to keep O(N) time complexity and
        hence could not pop unwanted elements out? Let's just replace all these by 1s.
        To ensure that the first missing positive is not 1, one has to verify the
        presence of 1 before proceeding to this operation.

        == How to solve in-place ==
        Now that we we have an array which contains only positive numbers in a range
        from 1 to n, and the problem is to find a first missing positive in O(N) time
        and constant space.
        That would be simple, if one would be allowed to have a hash-map positive number
        -> its presence for the array. Sort of "dirty workaround" solution would be to
        allocate a string hash_str with n zeros, and use it as a sort of hash map by
        changing hash_str[i] to 1 each time one meets number i in the array.
        Let's not use this solution, but just take away a pretty nice idea to use index
        as a hash-key for a positive number.
        The final idea is to use index in nums as a hash key and sign of the element as
        a hash value which is presence detector.
        For example, negative sign of nums[2] element means that number 2 is present in
        nums. The positive sign of nums[3] element means that number 3 is not present
        (missing) in nums.
        To achieve that let's walk along the array (which after clean up contains only
        positive numbers), check each element value elem and change the sign of
        element nums[elem] to negative to mark that number elem is present is nums. Be
        careful with duplicates and ensure that the sign was changed only once.

        == Algorithm ==
        - Check if 1 is present in the array. If not, you're done and 1 is the answer.
        - Replace the negative numbers, zeros and numbers larger than n by 1s.
        - Walk along the array. Change the sign of a-th element if you meet number a.
            Be careful with duplicates: do sign change only once.
        - Walk again along the array. Return the index of the first positive element.
        - If nums[0] > 0 return n.
        - If on the previous step you didn't find the positive element in nums, that
            means that the answer is n+1.

        == Complexity Analysis ==
        - Time Complexity: O(N) since all we do here is 3 walks along the array of
            length N.
        - Space Complexity: O(1) since this is a constant space solution.
        """
        n = len(nums)
        one_present = False

        # Replace all numbers < 1 and > n with 1.
        for i in range(n):
            if nums[i] == 1:
                one_present = True
            if nums[i] < 1 or nums[i] > n:
                nums[i] = 1

        # If 1 is not present, return it.
        if one_present is False:
            return 1

        # Now each element of nums is in [1,n]
        # Use index as hash and flip sign to negative.
        for i in range(n):
            if nums[abs(nums[i]) - 1] > 0:
                nums[abs(nums[i]) - 1] *= -1

        # Smallest index of positive element is missing element.
        for i in range(n + 1):
            if i == n or nums[i] > 0:
                return i + 1
