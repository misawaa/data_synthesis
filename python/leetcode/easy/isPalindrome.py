class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Handle negative integers and those ending in 0
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        # Initialize variables for the reversed integer and the remaining digits
        rev = 0
        remaining = x
        # Reverse the integer by adding the last digit to rev and removing it from remaining
        while remaining != 0:
            rev = rev * 10 + remaining % 10
            remaining //= 10
        # Check if x is equal to rev
        return x == rev
