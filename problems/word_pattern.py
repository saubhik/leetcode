class Solution:
    # Time: O(N), where N is the number of words in str or characters in pattern.
    # Space: O(26 + N) = O(N) where N is the number of unique words in str.
    # Maintain two hash maps:
    # - hash map from character to word
    # - hash map from word to character
    def wordPattern(self, pattern: str, str: str) -> bool:
        char_to_word = {}
        word_to_char = {}

        words = str.split(sep=" ")

        if len(words) != len(pattern):
            return False

        for char, word in zip(pattern, words):
            if char not in char_to_word:
                if word not in word_to_char:
                    char_to_word[char] = word
                    word_to_char[word] = char
                elif word_to_char[word] != char:
                    return False
            else:
                if char_to_word[char] != word:
                    return False

        return True


class SolutionTwo:
    # Time: O(N) where N is the number of words in str or number of chars in pattern.
    # Space: O(26 + N) = O(N) where N is the number of unique words in str.
    # Single Index Hash Map
    # Maintain only one hash map.
    # Key is character of pattern or word of str.
    def wordPattern(self, pattern: str, str: str) -> bool:
        words = str.split(" ")

        if len(words) != len(pattern):
            return False

        map = {}

        for index in range(len(words)):
            char, word = f"char_{pattern[index]}", f"word_{words[index]}"
            if char in map and word in map:
                if map[char] != map[word]:
                    return False
            elif char in map and word not in map:
                # char is already mapped to some other word
                return False
            elif char not in map and word in map:
                # word is already mapped to some other char
                return False
            else:
                # char not in map and word not in map
                map[char] = index
                map[word] = index

        return True
