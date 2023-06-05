class Solution:
    def minLength(self, s: str) -> int:
        # Repeat until no more replacements can be made
        while True:
            new_s = s.replace("AB", "").replace("CD", "")
            if new_s == s:
                break
            s = new_s
        # Return the length of the final string
        return len(s)
