class Solution:
    # Time: O(n), One Pass!
    # Space: O(1)
    #
    # After working out some examples, I found that the net direction should not be
    # North. Or if it is North, then the robot should be in the same initial point after
    # one full cycle.
    #
    # Extensive mathematical proof required.
    # Two proofs required:
    # 1. Bounded <=> Cycle. (Cycle => Bounded is trivial)
    # 2. Cycle <=>  (final directions is not North OR final coordinate is not Origin)
    def isRobotBounded(self, instructions: str) -> bool:
        coordinate = (0, 0)
        direction = (0, 1)
        for instruction in instructions:
            if instruction == "G":
                coordinate = (
                    coordinate[0] + direction[0],
                    coordinate[1] + direction[1],
                )
            elif instruction == "L":
                # 0,1 -> -1,0
                # -1,0 -> 0,-1
                # 0,-1 -> 1,0
                # 1,0 -> 0,1
                direction = (-1 * direction[1], direction[0])
            elif instruction == "R":
                # 0,1 -> 1,0
                # 1,0 -> 0,-1
                # 0,-1 -> -1,0
                # -1,0 -> 0,1
                direction = (direction[1], -1 * direction[0])

        return direction != (0, 1) or coordinate == (0, 0)
