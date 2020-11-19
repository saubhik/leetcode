class Solution:
    # Simulation.
    # Time Complexity: O(p).
    # Space Complexity: O(1).
    def mirrorReflection(self, p: int, q: int) -> int:
        from fractions import Fraction

        x = y = 0
        rx, ry = p, q
        targets = [(p, 0), (p, p), (0, p)]
        while (x, y) not in targets:
            # x + rx * t = 0 or p
            # y + ry * t = 0 or p
            t = float("inf")
            for v in [
                Fraction(numerator=-x, denominator=rx),
                Fraction(numerator=p - x, denominator=rx),
                Fraction(numerator=-y, denominator=ry),
                Fraction(numerator=p - y, denominator=ry),
            ]:
                if v > 0:
                    t = min(t, v)

            x += rx * t
            y += ry * t

            if x in (0, p):
                rx *= -1
            if y in (0, p):
                ry *= -1

        return 0 if (x, y) == (p, 0) else 1 if (x, y) == (p, p) else 2
