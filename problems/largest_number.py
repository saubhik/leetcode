from functools import cmp_to_key
from typing import List


class Solution:
    # Time Complexity: O(nlgn)
    # Space Complexity: O(n) for sorted(...) returns a new list.
    def largestNumber(self, nums: List[int]) -> str:
        # Degenerate Case: all 0s in nums
        # Executes in O(n) time, O(1) space.
        all_zeros = True
        for num in nums:
            if num != 0:
                all_zeros = False
                break

        if all_zeros is True:
            return "0"

        def compare(x: str, y: str):
            if (y + x) > (x + y):
                return 1
            elif (x + y) > (y + x):
                return -1
            else:
                return 0

        return "".join(sorted(map(str, nums), key=cmp_to_key(compare)))


class OfficialSolution:
    def largestNumber(self, nums: List[int]) -> str:
        """
        Approach 1: Sorting vis Custom Comparator
        == Intuition ==
        To construct the largest number, we want to ensure that the most significant
        digits are occupied by the largest digits.

        == Algorithm ==
        First, we convert each integer to a string. Then, we sort the array of strings.
        While it might be tempting to simply sort the numbers in descending order, this
        causes problems for sets of numbers with the same leading digit. For example,
        sorting the problem example in descending order would produce the number
        9534303, while the correct answer can be achieved by transposing the 3 and 30.
        Therefore, for each pairwise comparison during the sort, we compare the numbers
        achieved by concatenating the pair in both orders. We can prove that this sorts
        into the proper order as follows:
        We want to prove that this pairwise comparison leads to overall correct order.
        Suppose not. Suppose we have an incorrect ordering.
        Assume that (without loss of generality), for some pair of integers a and b, our
        comparator dictates that a should precede b in sorted order. This means that
        a+b > b+a (where + represents concatenation). For the sort to produce an
        incorrect ordering, there must be some c for which b precedes c and c precedes
        a. This is a contradiction because a+b > b+a and b+c > c+b implies a+c > c+a.
        In other words, our custom comparator preserves transitivity, so the sort is
        correct.
        (The above lines are hand wavy. Check out
            https://leetcode.com/problems/largest-number/discuss/291988/
            A-Proof-of-the-Concatenation-Comparator's-Transtivity
        for a rigorous proof)
        Once the array is sorted, the most "significant" number will be at the front.
        There is a minor edge case that comes up when the array consists of only zeroes,
        so if the most significant number is 0, we can simply return 0. Otherwise, we
        build a string out of the sorted array and return it.

        == Complexity Analysis ==
        - Time Complexity: O(nlgn)
            Although we are doing extra work in our comparator, it is only by a constant
            factor. Therefore, the overall run time is dominated by the complexity of
            srt, which is O(nlgn) in Python.

        - Space Complexity: O(n)
            Here, we allocate O(n) additional space to store the copy of nums. Although
            we could do that work in place (if we decide that it is okay to modify
            nums), we must allocate O(n) space for the final return string. Therfore,
            the overall memory footprint is linear in the length of nums.
        """
        largest_num = "".join(sorted(map(str, nums), key=LargerNumKey))
        return "0" if largest_num[0] == "0" else largest_num


class LargerNumKey(str):
    def __lt__(x, y):
        return x + y > y + x
