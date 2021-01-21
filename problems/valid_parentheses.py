from unittest import TestCase


class Solution:
    # Time Complexity: O(n).
    # Space Complexity: O(n).
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in ("(", "{", "["):
                stack.append(char)
            else:
                if stack and (
                    (char == ")" and stack[-1] == "(")
                    or (char == "}" and stack[-1] == "{")
                    or (char == "]" and stack[-1] == "[")
                ):
                    stack.pop()
                else:
                    return False
        return not stack


class TestSolution(TestCase):
    def test_is_valid(self):
        assert Solution().isValid(s="()") is True
        assert Solution().isValid(s="()[]{}") is True
        assert Solution().isValid(s="(]") is False
        assert Solution().isValid(s="([)]") is False
        assert Solution().isValid(s="{[]}") is True
