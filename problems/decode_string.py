class Solution:
    # Time Complexity: O(maxK * n)?
    # Space Complexity: O(n).
    def decodeString(self, s: str) -> str:
        def _get_substring_within_brackets(index: int, string: str, length: int):
            # index is guaranteed to be a left bracket.
            _tmp_stack = []
            pos = index
            while pos < length:
                if string[pos] == "[":
                    _tmp_stack.append("[")
                elif string[pos] == "]":
                    if _tmp_stack[-1] == "[":
                        _tmp_stack.pop()
                if not _tmp_stack:
                    break
                pos += 1
            return string[index + 1 : pos], pos + 1

        def _get_number(index: int, string: str):
            pos = index
            while string[pos].isnumeric():
                pos += 1
            return int(string[index:pos]), pos

        i, result, length = 0, [], len(s)
        while i < length:
            if s[i].isnumeric():
                number, next_i = _get_number(index=i, string=s)
                substring, next_i = _get_substring_within_brackets(
                    index=next_i, string=s, length=length
                )
                decoded_substring = self.decodeString(s=substring)
                result.append(decoded_substring * number)
                i = next_i
            else:
                # s[i] is a character
                result.append(s[i])
                i += 1

        return "".join(result)
