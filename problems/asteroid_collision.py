from typing import List


class Solution:
    """
    The idea is same as the Official Solution.
    Using Stack.

    == Intuition ==
    A row of asteroids is stable if no further collisions will occur. After adding a new
    asteroid to the right, some more collisions may happen before it becomes stable
    again, and all of those collisions (if they happen) must occur right to left. This
    is the perfect situation for using a stack.

    == Complexity Analysis ==
    - Time Complexity: O(n), where n is the number of asteroids. Our stack pushes and
        pops each asteroid at most once.
    - Space Complexity: O(n). We use a stack to keep track of the intermediate results.
        In the worst case, the states do not evolve at the end, i.e. we need O(n) space
        where n is the number of input asteroids.
    """

    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        result = []
        for asteroid in asteroids:
            if asteroid < 0:
                while result and abs(asteroid) > result[-1] > 0:
                    result.pop()

                # Asteroids in result, if any, are bigger or equal now.
                if result and result[-1] > 0:
                    if result[-1] == abs(asteroid):
                        result.pop()
                    continue

            result.append(asteroid)

        return result
