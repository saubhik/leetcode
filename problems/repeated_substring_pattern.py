import re
from math import sqrt


class SolutionRegex:
    # to use regex during the interviews is like to use built-in functions, the
    # community has no single opinion about it yet, and it's a sort of risk.
    # Time: O(n^2)
    # Space: O(1)
    def repeatedSubstringPattern(self, s: str) -> bool:
        pattern = re.compile(pattern=r"^(.+)\1+$")
        return pattern.match(string=s) is not None


class SolutionConcatenation:
    # Time: O(n^2)
    # Space: O(n)
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s + s)[1:-1]


class SolutionRabinKarp:
    # Time: O(sum-of-divisors-of-len(s)) < O(N*sqrt(N))
    # Space: O(sqrt(N)), during each hash calculation
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)

        if n < 2:
            return False

        if n == 2:
            return s[0] == s[1]

        for d in range(int(sqrt(n)), 0, -1):
            if n % d == 0:
                divs = [d]
                if d != 1:
                    divs.append(n // d)

                for div in divs:
                    h = hash(s[0:div])
                    j = div
                    while j < n:
                        if hash(s[j : div + j]) != h:
                            break
                        j += div

                    if j == n:
                        return True

        return False
