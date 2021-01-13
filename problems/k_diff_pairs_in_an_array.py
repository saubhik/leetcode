from collections import Counter, defaultdict
from typing import List


class Solution:
    # Time Complexity: O(n).
    # Space Complexity: O(n).
    def findPairs(self, nums: List[int], k: int) -> int:
        present, ans, considered = defaultdict(bool), 0, set()
        for num in nums:
            if k == 0 and present[num] is True and num not in considered:
                ans += 1
                considered.add(num)
            present[num] = True

        if k != 0:
            for key in list(present.keys()):
                if present[key + k]:
                    ans += 1

        return ans


class OfficialSolution:
    def findPairs(self, nums: List[int], k: int) -> int:
        """
        == Approach 3: Hashmap ==
        == Intuition ==
        This method removes the need to sort the nums array. Rather than that, we will
        be a frequency hash map. This hash map will have every unique number in nums as
        keys and the number of times each number shows up in nums as values.
        Next, we look at a key (let's call x) in the hash map and ask whether:
        - There is a key in the hash map which is equal to x+k if k > 0.
            - For example, if a number in nums is 1 (x=1) and k=3, you would need to
            have 4 to satisfy this condition (thus, we need to look for 1+3=4 in the
            hash map). Using addition to look for a complement pair has the advantage
            of not double-counting the same pair but in reverse order (i.e. if we have
            found a pair (1,4), we won't be counting (4,1)).
        - There is more than one occurrence of x if k = 0.
            - For example, if we have nums = [1,1,1,1] and k = 0, we have one unique
            (1,1) pair. In this case, our hash map will be {1:4}, and this condition is
            satisfied since we have more than one occurrence of number 1.
        If we can satisfy either of the above conditions, we can increment our
        placeholder result variable. Then we look at the next key in the hash map.

        == Complexity Analysis ==
        Let N be the number of elements in the input list.
            - Time Complexity: O(N).
                - It takes O(N) to create an initial frequency hash map and another O(N)
                to traverse the keys of that hash map. One thing to note about is the
                hash key lookup. The time complexity for hash key lookup is O(1) but if
                there are hash key collisions, the time complexity will become O(N).
                However those cases are rare and this, the amortized time complexity is
                O(2N) ~ O(N).
            - Space Complexity: O(N).
                - We keep a table to count the frequency of each unique number in the
                input. In the worst case, all numbers are unique in the array. As a
                result, the maximum size of our table would be O(N).
        """
        result = 0
        counter = Counter(nums)
        for x in counter:
            if k == 0 and counter[x] > 1:
                result += 1
            elif k > 0 and x + k in counter:
                result += 1
        return result
