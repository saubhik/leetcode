from collections import Counter


class OfficialSolution:
    """
    == Intuition ==
    First we should make sure we understand what "lexicographical order" means.
    Comparing strings doesn't work the same way as comparing numbers. Strings are
    compared from the first character to the last one. Which string is greater depends
    on the comparison between the first unequal corresponding character in the two
    strings. As a result, any string beginning with a will always be less than any
    string beginning with b, regardless of the ends of both strings.

    Because of this, the optimal solution will have the smallest characters as early
    as possible. We draw 2 conclusions that provide different methods of solving this
    problem in O(n):
        1. The leftmost letter in our solution will be the smallest letter such that the
        suffix from that letter contains evert other. This is because we know that the
        solution must have one copy of every letter, and we know that the solution will
        have the lexicographically smallest leftmost character possible.

        If there are multiple smallest letters, then we pick the leftmost one simply
        because it gives us more options. We can always eliminate more letters later
        on, so the optimal solution will always remain in our search space.

        2. As we iterate over our string, if character i is greater than character
        i+1 and another occurrence of character i exists later in the string, deleting
        character i will always lead to the optimal solution. Characters that come
        later in the string i don't matter in this calculation because i is in a more
        significant spot. Even if character i+1 isn't the best yet, we can always
        replace it for a smaller character down the line if possible.

    Since we try to remove characters as early as possible, and picking the best letter
    at each step leads to the best solution, "greedy" should be going off like an alarm.
    """

    class Approach1:
        """
        == Approach 1: Greedy - Solving Letter by Letter ==
        == Algorithm ==
        We use idea number one from the intuition. In each iteration, we determine the
        leftmost letter in our solution. This will be the smallest character such that
        its suffix contains at least one copy of every character in the string. We
        determine the rest of our answer by recursively calling the function on the
        suffix we generate from the original string (leftmost letter is removed).

        == Complexity Analysis ==
        - Time Complexity: O(n).
            Each recursive call will take O(n).
            The number of recursive calls is bounded by 26 letters in the alphabet.
            So, we have O(n) * C = O(n).
        - Space Complexity: O(n).
            Each time we slice the string we're creating a new one (strings are
            immutable).
            The number of slices is bound by a constant, so we have O(n) * C = O(n).
        """

        def removeDuplicateLetters(self, s: str) -> str:
            counter = Counter(s)
            start_index = 0
            for index in range(len(s)):
                if s[index] < s[start_index]:
                    start_index = index
                counter[s[index]] -= 1
                if counter[s[index]] == 0:
                    break
            return (
                s[start_index]
                + self.removeDuplicateLetters(
                    s=s[start_index:].replace(s[start_index], "")
                )
                if s
                else ""
            )

    class Approach2:
        """
        == Approach 2: Greedy - Solving with Stack ==
        We use idea number 2 from the intuition. We will keep a stack to store the
        solution we have built as we iterate over the string, and we will delete the
        characters off the stack whenever it is possible and make our string smaller.
        Each iteration as we add the current character to the solution if it hasn't
        already been used. We try to remove as many characters as possible off the
        top of the stack, and then add the current character.
        The conditions for deletion are:
            1. The character is greater than the current characters.
            2. The character can be removed because it occurs later on.
        At each stage in our iteration through the string, we greedily keep what's on
        the stack as small as possible.

        Suppose we have "bcabca".
        We start with empty stack.
        Iteration 1:
            Push "b" into the stack.
        Iteration 2:
            Push "c" into the stack.
        Iteration 3:
            We check "a" < "c" and "c" appears later. We pop "c".
            We check "a" < "b" and "b" appears later. We pop "b".
            We push "a".
        Iteration 4:
            We push "b" into the stack.
        Iteration 5:
            We push "c" into the stack.
        Iteration 6:
            "a" is already in the stack, so we skip.

        In any iteration, we might have to pop at most 25 elements.
        So, the time complexity is O(n).
        Space complexity is O(1), since at most we keep 26 elements in the stack or
        counter hashtable.

        == Complexity Analysis ==
        - Time Complexity: O(n).
            Although there is a loop inside a loop, the time complexity is still O(n).
            This is because the inner while loop is bounded by the total number of
            elements added to the stack (each time it fires an element goes). This
            means that the total amount of time spent in the inner loop is bounded by
            O(26), giving us a total time complexity of O(n).

        - Space Complexity: O(1).
            At first glance it looks like this is O(n), but that is not true! Stack
            only consists of unique elements, bounded by the number of characters in the
            alphabet, giving us O(1) space complexity.
        """

        def removeDuplicateLetters(self, s: str) -> str:
            counter, stack = Counter(s), []
            for ch in s:
                counter[ch] -= 1
                if ch not in stack:
                    while stack and stack[-1] > ch and counter[stack[-1]] > 0:
                        stack.pop()
                    stack.append(ch)
            return "".join(stack)
