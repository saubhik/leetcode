from collections import Counter, defaultdict
from typing import List
from unittest import TestCase


class Solution:
    # Gets TLEd with one HashMap.
    # Time Complexity: O(n^3)
    # Space Complexity: O(n)
    def fourSumCount(
        self, A: List[int], B: List[int], C: List[int], D: List[int]
    ) -> int:
        n, counter_d, count = len(A), Counter(D), 0
        for a in range(n):
            for b in range(n):
                for c in range(n):
                    num = -1 * (A[a] + B[b] + C[c])
                    if num in counter_d:
                        count += counter_d[num]
        return count


class SolutionTwo:
    # Two HashMaps.
    # Time Complexity: O(n^2).
    # Space Complexity: O(n^2).
    def fourSumCount(
        self, A: List[int], B: List[int], C: List[int], D: List[int]
    ) -> int:
        n = len(A)
        a_plus_b = defaultdict(int)
        for a in range(n):
            for b in range(n):
                a_plus_b[A[a] + B[b]] += 1

        c_plus_d = defaultdict(int)
        for c in range(n):
            for d in range(n):
                c_plus_d[C[c] + D[d]] += 1

        count = 0
        for key in a_plus_b:
            if -key in c_plus_d:
                count += a_plus_b[key] * c_plus_d[-key]

        return count


class SolutionThree:
    # Optimize Solution Two using 1 HashMap.
    # Time Complexity: O(n^2).
    # Space Complexity: O(n^2).
    def fourSumCount(
        self, A: List[int], B: List[int], C: List[int], D: List[int]
    ) -> int:
        partial_sums = dict()
        for a in A:
            for b in B:
                partial_sums[a + b] = partial_sums.get(a + b, 0) + 1

        count = 0
        for c in C:
            for d in D:
                count += partial_sums.get(-(c + d), 0)

        return count


class SolutionFour:
    # Solve the general case: kSumIII.
    def fourSumCount(
        self, A: List[int], B: List[int], C: List[int], D: List[int]
    ) -> int:
        return self.nSumCount(lists=[A, B, C, D])

    def nSumCount(self, lists: List[List[int]]) -> int:
        k = len(lists)
        partial_sums = dict()

        def addToHash(start: int, end: int, partial_sum: int = 0) -> None:
            if start == end:
                partial_sums[partial_sum] = partial_sums.get(partial_sum, 0) + 1
                return
            for elem in lists[start]:
                addToHash(start=start + 1, end=end, partial_sum=partial_sum + elem)

        def countComplements(start: int, end: int, partial_sum: int = 0) -> int:
            if start == end:
                return partial_sums.get(-partial_sum, 0)
            count = 0
            for elem in lists[start]:
                count += countComplements(
                    start=start + 1, end=end, partial_sum=partial_sum + elem
                )
            return count

        mid = k // 2
        addToHash(start=0, end=mid)
        return countComplements(start=mid, end=k)


class TestSolution(TestCase):
    def test_example_1(self):
        assert Solution().fourSumCount(A=[1, 2], B=[-2, -1], C=[-1, 2], D=[0, 2]) == 2
        assert (
            SolutionTwo().fourSumCount(A=[1, 2], B=[-2, -1], C=[-1, 2], D=[0, 2]) == 2
        )
        assert (
            SolutionThree().fourSumCount(A=[1, 2], B=[-2, -1], C=[-1, 2], D=[0, 2]) == 2
        )
        assert (
            SolutionFour().fourSumCount(A=[1, 2], B=[-2, -1], C=[-1, 2], D=[0, 2]) == 2
        )

    def test_example_2(self):
        assert (
            Solution().fourSumCount(
                A=[0, 1, -1], B=[-1, 1, 0], C=[0, 0, 1], D=[-1, 1, 1]
            )
            == 17
        )
        assert (
            SolutionTwo().fourSumCount(
                A=[0, 1, -1], B=[-1, 1, 0], C=[0, 0, 1], D=[-1, 1, 1]
            )
            == 17
        )
        assert (
            SolutionThree().fourSumCount(
                A=[0, 1, -1], B=[-1, 1, 0], C=[0, 0, 1], D=[-1, 1, 1]
            )
            == 17
        )
        assert (
            SolutionFour().fourSumCount(
                A=[0, 1, -1], B=[-1, 1, 0], C=[0, 0, 1], D=[-1, 1, 1]
            )
            == 17
        )
