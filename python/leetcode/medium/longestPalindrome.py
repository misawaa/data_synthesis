class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Initialize variables for the start and length of the longest palindromic substring seen so far
        start = 0
        length = 0
        # Loop through each character in the string as the center of a potential palindrome
        for i in range(len(s)):
            # Check for odd-length palindromes with center at i
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > length:
                    start = left
                    length = right - left + 1
                left -= 1
                right += 1
            # Check for even-length palindromes with center at i and i+1
            left, right = i, i+1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > length:
                    start = left
                    length = right - left + 1
                left -= 1
                right += 1
        # Return the longest palindromic substring
        return s[start:start+length]
