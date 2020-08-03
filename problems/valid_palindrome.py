class Solution:
    def isPalindrome(self, s: str) -> bool:
        # O(n) time, O(1) additional space.
        n = len(s)
        i, j = 0, n - 1
        while i < j:
            if not s[i].isalnum():
                i += 1
            elif not s[j].isalnum():
                j -= 1
            elif s[i].lower() != s[j].lower():
                return False
            else:
                i, j = i + 1, j - 1
        return True


class SolutionTwo:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True

        check = '!@#$%^&*-;,.<>"?/:\|~()[]{}`~_'
        others = ["'", '"', " "]
        for x in check:
            if x in s:
                s = s.replace(x, "")
        for x in others:
            if x in s:
                s = s.replace(x, "")
        if s.lower() == s[::-1].lower():
            return True
        return False
