from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        word_count = Counter(words)
        word_len = len(words[0])
        substr_len = word_len * len(words)
        result = []

        for i in range(len(s) - substr_len + 1):
            substring = s[i:i+substr_len]
            substring_count = Counter([substring[j:j+word_len] for j in range(0, substr_len, word_len)])
            if substring_count == word_count:
                result.append(i)

        return result
