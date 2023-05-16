class Solution:
    def myAtoi(self, s: str) -> int:
        # Initialize variables for the sign and the integer
        sign = 1
        num = 0
        # Remove leading whitespace
        s = s.lstrip()
        # Handle leading sign
        if s and (s[0] == '-' or s[0] == '+'):
            sign = -1 if s[0] == '-' else 1
            s = s[1:]
        # Loop through each digit in s and add it to num
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            else:
                break
        # Apply sign and clamp to 32-bit integer range
        num *= sign
        num = max(-2**31, min(num, 2**31 - 1))
        return num
