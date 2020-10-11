import bisect
from collections import defaultdict


class TwoSum:
    """
    This is my original solution, which matches Official Solution's Approach 2.

    == Approach 2: Hash Table ==
    == Intuition ==
    As an alternative solution to the original Two Sum problem, one could employ the
    HashTable to index each number.
    Given a desired sum value S, for each number a, we just need to verify if there
    exists a complement number (S-a) in the table.
    As we know, the data structure of hash table could offer us a quick lookup as well
    as an insertion operation, which fits well with the above requirements.

    == Algorithm ==
    - First, we initialize a hash table container in our data structure.
    - For the add(number) function, we build a frequency hash table with the number as
    key and the frequency of the number as value in the table.
    - For the find(value) function, we iterate through the hashtable over the keys.
    For each key (number), we check if there exists a complement (value - number) in the
    table. If so, we could terminate the loop and return the result.
    - In a particular case, where the number and its complement are equal, we then need
    to check if there exists at least 2 copies of the number in the table.

    == Complexity Analysis ==
    - Time Complexity:
        - For the add(number) function: O(1), since it takes a constant time to update
        an entry in hashtable.
        - For the find(value) function: O(n), where n is the total number of unique
        numbers. In the worst case, we would iterate through the entire table.
    - Space Complexity: O(n), where n is the total number of unique numbers that we will
        see during the usage of the data structure.
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.sums = defaultdict(int)

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        # O(1) time.
        self.sums[number] += 1

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        # O(n) time.
        for key in self.sums.keys():
            if value - key in self.sums:
                if value - key == key and self.sums[key] < 2:
                    continue
                return True
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)


class OfficialSolutionTwoSumApproach1:
    """
    == Approach 1: Sorted List ==
    == Intuition ==
    First of all, the problem description is not terribly clear on the requirements of
    time and space complexity. But let us consider this as part of the challenge or a
    freedom of design. We could figure out the desired complexity for each function,
    by trial and error.
    Given a list, one of the solutions to the Two Sum problem if called "Two-Pointers
    Iteration" where we iterate through the list from two directions with two pointers
    approaching each other.
    However, one of the preconditions for the Two-Pointers Iteration solution is that
    the input list should be sorted.
    So now, here are the questions:
        - Should we keep the list in order while inserting new numbers in the function
        add(number)?
        - Or should we do the sorting on demand, i.e. at the invocation of find(value)?

    == Algorithm ==
    Let us first give the algorithm of Two-Pointers Iteration to find the two-sum
    solution from a sorted list:
        - We initialize two pointers, low and high which point to the head and the tail
        elements of the list respectively.
        - With the two pointers, we start a loop to iterate the list. The loop would
        terminate when we find the two sum solution or the two pointers meet each other.
        - Within the loop, at each step, we would move either of the pointers, according
        to different conditions:
            - If the sum of the elements pointed by the current pointers is less than
            the desired value, then we should try to increase the sum to meet the
            desired value, i.e. we should move the low pointer forwards to have a larger
            value.
            - Similarly, if the sum of the elements pointed by the current pointers is
            greater than the desired value, we then should try to reduce the sum by
            moving the high pointer towards the low pointer.
            - If the sum happen to the desired value, then we could simply do an early
            return of the function.
        - If the loop is terminated at the case where the two pointers meet each other,
        then we can be sure that there is no solution to the desired value.

    The usage pattern of the desired data structure in the online judge, as we would
    discover, is that the add(number) function would be called frequently which might be
    followed a less frequent call of the find(value) function.

    The usage pattern implies that we should try to minimize the cost of add(number)
    function. As a result, we sort the list within the find(value) function instead of
    the add(number) function.

    So to the above questions about where to place the sort operation, actually both
    options are valid and correct. Due to the usage pattern of the two functions though,
    it is less optimal to sort the list at each add operation.

    On the other hand, we do not do sorting at each occasion of the find(value) either.
    But rather, we sort on demand, i.e. only when the list is updated. As a result, we
    amortize the cost of the sorting over the time. And this is the optimization trick
    for the solution to pass the online judge.

    == Complexity Analysis ==
    - Time Complexity:
        - For the add(number) function: O(1) since we simply append the element into the
        list.
        - For the find(value) function: O(nlgn). In the worst case, we would need to
        sort the list first, which is of O(nlgn) time complexity normally. And later,
        again in the worst case, we need to iterate through the entire list, which is of
        O(n) time complexity. As a result, the overall time complexity of the function
        lies on O(nlgn) of the sorting operation, which dominates over the later
        iteration part.

    - Space Complexity:
        - The overall space complexity of the data structure is O(n) where n is the
        total number of numbers that have been added.
    """

    def __init__(self):
        self.nums = []
        self.length = 0
        self.is_sorted = True

    def add(self, value: int) -> None:
        # O(lgn) time insertion.
        # idx = bisect.bisect(self.nums, value)
        # self.nums.insert(idx, value)
        self.nums.append(value)
        self.is_sorted = False
        self.length += 1

    def find(self, value: int) -> bool:
        if not self.is_sorted:
            self.nums.sort()
            self.is_sorted = True

        lo, hi = 0, self.length - 1
        while lo < hi:
            if self.nums[lo] + self.nums[hi] < value:
                lo += 1
            elif self.nums[lo] + self.nums[hi] > value:
                hi -= 1
            else:
                return True

        return False
