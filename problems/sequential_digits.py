from typing import List


class Solution:
    # Straight Forward Iterative.
    #
    # Time: O(1)
    # Space: O(1)
    #
    # Examples:
    # low = 100, high = 300
    # [123, 234]
    # low = 1000, high = 13000
    # [1234, 2345, 3456, 4567, 5678, 6789, 12345]
    # 10 <= low <= high <= 10^9
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        def get_num_digits(num: int):
            # O(1) time, O(1) space.
            num_digits = 0
            while num:
                num //= 10
                num_digits += 1
            return num_digits

        low_num_digits = get_num_digits(num=low)
        high_num_digits = get_num_digits(num=high)

        def get_sequential_numbers(num_digits: int):
            # O(1) time, O(1) space
            # 1 <= num_digits <= 9
            for digit in range(1, 10 - num_digits + 1):
                num = 0
                for _ in range(num_digits):
                    num = num * 10 + digit
                    digit += 1
                yield num

        # O(1) time, O(1) additional space
        ans = []
        for num_digits in range(low_num_digits, high_num_digits + 1):
            for num in get_sequential_numbers(num_digits=num_digits):
                if low <= num <= high:
                    ans.append(num)

        return ans


class SolutionTwo:
    # Sliding Window.
    #
    # All sequential numbers are substrings of the string "123456789".
    # We slide over the string, with window length = number of digits, which itself
    # iterates from number of digits in low, and the number of digits in high.
    #
    # Time: O(1)
    # Space: O(1)
    def sequentialDigits(self, low: int, high: int):
        sample = "123456789"
        ans = []
        for length in range(len(str(low)), len(str(high)) + 1):
            for start in range(10 - length):
                num = int(sample[start : start + length])
                if low <= num <= high:
                    ans.append(num)
        return ans


class SolutionThree:
    # Pre-computation.
    # Time: O(1)
    # Space: O(1)
    def sequentialDigits(self, low: int, high: int):
        sequential_numbers = [
            12,
            23,
            34,
            45,
            56,
            67,
            78,
            89,
            123,
            234,
            345,
            456,
            567,
            678,
            789,
            1234,
            2345,
            3456,
            4567,
            5678,
            6789,
            12345,
            23456,
            34567,
            45678,
            56789,
            123456,
            234567,
            345678,
            456789,
            1234567,
            2345678,
            3456789,
            12345678,
            23456789,
            123456789,
        ]

        return [num for num in sequential_numbers if low <= num <= high]
