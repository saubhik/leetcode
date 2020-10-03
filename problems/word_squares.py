from collections import defaultdict
from typing import List, Optional


class OfficialSolution:
    """
    Before diving into the solutions, it could be helpful to take a step back and
    clarify the requirements of the problem first.
    Given a list of non-duplicate words, we are asked to construct all possible
    combinations of word squares. And here is the definition of word square:
        A sequence of words forms a valid word square, if and only if each string Hk
        that is formed horizontally from the kth row equals to the string Vk that is
        formed vertically from the kth column, i.e. Hk == Vk for all k where
        0 <= k <= max(numRows, numColumns).
    Here numRows = numColumns since H0 == V0.
    As we can see from the definition, for a word square with equal sized row and
    column, the resulting letter matrix should be symmetrical across its diagonal.
    In other words, if we know the upper right part of the word square, we could infer
    its lower left part, and vice versa. This symmetric property of the word square
    could also be interpreted as the constraint of the problem (as in the constraint
    programming), which could help us narrow down the valid combinations.

    == Algorithm: Backtracking ==
    Given a list of words, we are asked to find a combination of words upon with we
    could construct a word square. The backbone of the algorithm to solve the above
    problem could be surprisingly simple.
    The idea is that we construct the word square row by row from top to down. At each
    row, we simply do trial and error, i.e. we try with one word, if it does not meet
    the constraint then we try another one.
    As one might notice, the above idea of the algorithm is actually known as
    backtracking, which is often associated with recusion and DFS (Depth-First Search)
    as well.
    Let us illustrate the idea with an example. Given a list of words [ball, able, area,
    lead, lady], we should pile up 4 words together in order to build a word square.
        1. Let us start with the word ball as the first word in the word square, i.e.
        the word that we would put in the first row.
        2. We then move on to the second row. Given the symmetric property of the word
        square, we now know the letters that we should fill on the first column of the
        second row. In other words, we know that the word in the second row should
        start with the prefix a.
        3. Among the list of words, there are two words with prefix a (i.e. able, area).
        Both of them could be candidates to fill the second row of the square. We then
        should try both of them in the next step.
        4. In the next step, let us fill the second row with the word able. Then we
        could move on to the third row. Again, due to the symmetric property, we know
        that the word in the third row should start with the prefix ll. Unfortunately,
        we do not find any word start with ll. As a result, we could no longer move
        forwards. We then abandon this path, and backtrack to the previous state (with
        the first row filled).
        5. As an alternative next step, we could try with the word area in the second
        row. Once we fill the second row, we would know that in the next row, the word
        to be filled should start with the prefix le. And this time, we find the
        candidate (i.e. lead).
        6. As a result, in the next step, we fill the third row with the word lead. So
        on and so forth.
        7. At the end, if one repeats the above steps with each word as the starting
        word, one would exhaust all the possibilities to construct a valid word square.
    """

    def wordSquares(self, words: List[str]) -> List[List[str]]:
        """Gets TLEd."""

        def backtrack(
            curr_row: int = 0,
            curr_square: Optional[List[str]] = None,
            squares: Optional[List[str]] = None,
        ):
            if squares is None:
                squares = []

            if curr_square is None:
                curr_square = []

            if len(curr_square) > 0 and curr_row == len(curr_square[0]):
                # curr_square is modified, so need to insert a copy of it.
                squares.append(curr_square.copy())
                return

            prefix = ""
            for i in range(curr_row):
                prefix += curr_square[i][curr_row]

            for i, word in enumerate(words):
                if word.startswith(prefix):
                    curr_square.append(word)
                    backtrack(
                        curr_row=curr_row + 1, curr_square=curr_square, squares=squares,
                    )
                    curr_square.pop()

            return squares

        return backtrack()

    def wordSquaresApproach1(self, words: List[str]) -> List[List[str]]:
        """
        == Intuition ==
        As one might notice in the above backtracking algorithm, the bottleneck lies in
        the finding all words with the given prefix. At each invocation of the function,
        we were iterating through the entire input list of words, which is of linear
        time complexity O(N).

            One of the ideas to optimize it would be to process the words beforehand
            and to build a data structure that could speed up the lookup procedure
            later.

        As one might recall, one of the data structures that provide a fast lookup
        operation is called hashtable or dictionary. We could simply build a hashtable
        with all possible prefixes as keys and the words that are associated with the
        prefix as the values in the table. Later, given the prefix, we should be able
        to list all the words with the given prefix in constant time O(1).

        == Algorithm ==
        - We build upon the backtracking algorithm that we listed above, and tweak two
        parts.
        - In the first part, we build a hashtable out of the input words.
        - In the second part, we simply query the hashtable to retrieve all the words
        that possess the given prefix.
        """

        prefix_to_words = defaultdict(list)
        for word in words:
            prefix = ""
            for ch in word:
                prefix += ch
                prefix_to_words[prefix].append(word)
        prefix_to_words[""] = words

        def backtrack(
            curr_row: int = 0,
            curr_square: Optional[List[str]] = None,
            squares: Optional[List[str]] = None,
        ):
            if squares is None:
                squares = []

            if curr_square is None:
                curr_square = []

            if len(curr_square) > 0 and curr_row == len(curr_square[0]):
                # curr_square is modified, so need to insert a copy of it.
                squares.append(curr_square.copy())
                return

            prefix = ""
            for i in range(curr_row):
                prefix += curr_square[i][curr_row]

            for word in prefix_to_words[prefix]:
                curr_square.append(word)
                backtrack(
                    curr_row=curr_row + 1, curr_square=curr_square, squares=squares,
                )
                curr_square.pop()

            return squares

        return backtrack()
