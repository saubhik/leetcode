from typing import List


class OfficialSolution:
    """
    == Approach 1: Boyer-Moore Voting Algorithm ==

    == Intuition ==
    To figure out a O(1) space requirement, we would need to get this simple intuition
    first. For an array of length n:
        - There can be at most one majority element, which is more than floor(n/2)
        times.
        - There can be at most two majority elements, which are more than floor(n/3)
        times.
        - There can be at most three majority elements, which are more than floor(n/4)
        times.
    and so on.

    Knowing this can help us understand how we can keep track of majority elements which
    satisfies O(1) space requirement.

    Let's try to get an intuition for the case where we would like to find a majority
    element which is more than floor(n/2) times in an array of length n.

    The idea is to have two variables, one holding a potential candidate for majority
    element and a counter to keep track of whether to swap a potential candidate or not.
    Why can we get away with only 2 variables? Because there can be at most 1 majority
    element which is more than floor(n/2) times. Therefore, having only one variable to
    hold the only potential candidate and one counter is enough.

    While scanning the array, the counter is incremented if you encounter an element
    which is exactly same as the potential candidate but decremented otherwise. When the
    counter reaches 0, the element which will be encountered next will become the
    potential candidate. Keep doing this procedure while scanning the array. However,
    when you have exhausted the array, you have to make sure that the element recorded
    in the potential candidate variable is the majority element by checking whether it
    occurs more than floor(n/2) times in the array. In the original Majority Element
    problem, it is guaranteed that there is a majority element in the array so your
    implementation can omit the second pass. However, in a general case, you need this
    second pass since your array can have no majority elements at all!

    The counter is initialized as 0 and the potential candidate as None at the start of
    the array.

    If an element is truly a majority element, it will stick in the potential candidate
    variable, no matter how it shows up in the array (i.e. all clustered in the
    beginning of the array, all clustered near the end of the array, or showing up
    anywhere in the array), after the whole array has been scanned. Of course, while you
    are scanning the array, the element might be replaced by another element in the
    process, but the true majority element will definitely remain as the potential
    candidate in the end.

    The above is essentially the Boyer-Moore algorithm we encountered in the Majority
    Element problem.

    Now figuring out the majority elements which show up more than floor(n/3) times is
    not that hard anymore. Using the intuition presented in the beginning, we only need
    4 variables: 2 for holding two potential candidates and 2 for holding the 2
    corresponding counters. Similar to the above case, both candidates are initialized
    as None in the beginning with their corresponding counters being 0. While going
    through the array:
    - If the current element is equal to one of the potential candidate, the count for
    that candidate is increased while leaving the count of the other candidate as it is.
    - If the counter reaches 0, the candidate associated with that counter will be
    replaced with the next element if the next element is not equal to the other
    candidate as well.
    - Both counters are decremented only when the current element is different from
    both candidates.

    == Complexity Analysis ==
    Time Complexity: O(N) where N is the size of nums. We first go through nums looking
        for first and second potential candidates. We then count the number of
        occurrences for these two potential candidates in nums. Therefore, our runtime
        is O(N) + O(N) = O(2N) = O(N).
    Space Complexity: O(1) since we only have 4 variables for holding 2 potential
        candidates and 2 counters. Even the returning array is at most 2 elements.
    """

    def majorityElement(self, nums: List[int]) -> List[int]:
        majority_one = majority_two = None
        count_one = count_two = 0
        for num in nums:
            if count_one == 0 and majority_two != num:
                majority_one = num

            if count_two == 0 and majority_one != num:
                majority_two = num

            if num == majority_one:
                count_one += 1
            elif num == majority_two:
                count_two += 1
            else:
                count_one -= 1
                count_two -= 1

        ans = []
        cutoff = len(nums) // 3

        # verify majority_one is indeed one of the answers
        for majority_candidate in (majority_one, majority_two):
            if nums.count(majority_candidate) > cutoff:
                ans.append(majority_candidate)

        return ans
