class Solution:
    def reverse(self, x: int) -> int:
        # Initialize variables for the sign and the absolute value of x
        sign = -1 if x < 0 else 1
        x = abs(x)
        # Initialize variable for the reversed integer
        rev = 0
        # Loop through each digit in x and add it to the reversed integer
        while x != 0:
            rev = rev * 10 + x % 10
            x //= 10
        # Check if the reversed integer is within the signed 32-bit integer range
        if rev > 2**31 - 1:
            return 0
        # Return the reversed integer with the original sign
        return sign * rev
