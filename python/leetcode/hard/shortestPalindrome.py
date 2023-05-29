class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        rev_s = s[::-1]
        n = len(s)
        for i in range(n):
            if s[:n-i] == rev_s[i:]:
                break
        prefix = s[n-i:][::-1]
        return prefix + s