import heapq


class Solution:
    # Time Complexity: O(n).
    # Space Complexity: O(1).
    def kthFactor(self, n: int, k: int) -> int:
        j = 0
        for i in range(1, n + 1):
            if n % i == 0:
                j += 1
                if j == k:
                    return i
        return -1


class SolutionTwo:
    # Push divisor d and n/d into max-heap of size k in O(log k) time.
    # Maintain heap size constant at k throughout.
    # Final head of heap is kth divisor of n.
    # Time Complexity: O(sqrt(n) log k).
    # Space Complexity: O(min(k, sqrt(n)) to store the heap.
    def kthFactor(self, n: int, k: int) -> int:
        i, heap, len_heap = 1, [], 0
        while i * i <= n:
            if n % i == 0:
                heapq.heappush(heap, -1 * i)
                heapq.heappush(heap, -1 * n // i)
                len_heap += 1 if i * i == n else 2
                while len_heap > k:
                    heapq.heappop(heap)
                    len_heap -= 1
            i += 1
        return -1 * heapq.heappop(heap) if len_heap == k else -1


# For Solution Two
# Consider example:
# n = 12, k = 3
# 1, 12 gets pushed. heap = [1, 12]
# 2, 6 gets pushed. heap = [1, 2, 6, 12]. 12 gets popped.
# 3, 4 gets pushed. heap = [1, 2, 3, 4, 6]. 6, 4 gets popped.
# Heap now is [1, 2, 3].


class SolutionThree:
    # Store the divisors in a list.
    # Time Complexity: O(sqrt(n)).
    # Space Complexity: O(min(k, sqrt(n)))
    def kthFactor(self, n: int, k: int) -> int:
        i, divisors, len_divisors = 1, [], 0
        while i * i <= n:
            if n % i == 0:
                divisors.append(i)
                len_divisors += 1
                k -= 1
                if k == 0:
                    return i
            i += 1

        if divisors[-1] * divisors[-1] == n:
            divisors.pop()
            len_divisors -= 1

        return n // divisors[len_divisors - k] if k <= len_divisors else -1


# For Solution Three
# Consider example:
# n = 7, k = 2
# divisors = [1]
# len_divisors - k + 1 = 1 - 2 + 1 = 0
#
# Consider example:
# n = 1, k = 1
# divisors = [1], len_divisors = 1, len_divisors == k -> return 1.
#
# Consider example:
# n = 4, k = 3
# divisors = [1, 2], len_divisors = 2, k = 1
# Since 2 * 2 == 4, divisors = [1], len_divisors = 1
