import bisect
from unittest import TestCase


class Solution:
    # Time Complexity: O(n).
    # Space Complexity: O(n) due to tmp array to store digits from end.
    def nextGreaterElement(self, n: int) -> int:
        tmp = [n % 10]
        n //= 10
        while n > 0:
            digit = n % 10
            n //= 10

            if digit < tmp[-1]:
                # Find element which is bigger than digit.
                index = bisect.bisect(tmp, digit)
                ans = n * 10 + tmp.pop(index)
                tmp.insert(index, digit)
                for num in tmp:
                    ans = ans * 10 + num
                return ans if ans < 2 ** 31 - 1 else -1

            tmp.append(digit)
        return -1


class TestNextGreaterElement(TestCase):
    def test_example_1(self):
        assert Solution().nextGreaterElement(n=12) == 21

    def test_example_2(self):
        assert Solution().nextGreaterElement(n=21) == -1

    def test_example_3(self):
        assert Solution().nextGreaterElement(n=12222333) == 12223233

    def test_example_4(self):
        assert Solution().nextGreaterElement(n=1999999999) == -1
