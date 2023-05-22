class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        carry = 0
        i, j = len(a) - 1, len(b) - 1
        
        while i >= 0 or j >= 0 or carry > 0:
            # Get the current digits of a and b (or 0 if we've reached the end of a or b)
            digit_a = int(a[i]) if i >= 0 else 0
            digit_b = int(b[j]) if j >= 0 else 0
            
            # Compute the sum of the current digits and the carry
            digit_sum = digit_a + digit_b + carry
            
            # Compute the new carry (if any)
            carry = digit_sum // 2
            
            # Compute the new digit (the remainder of digit_sum divided by 2)
            digit = digit_sum % 2
            
            # Insert the new digit at the beginning of the result list
            res.insert(0, str(digit))
            
            # Move to the next digits of a and b (or to the end if we've reached the beginning)
            i -= 1
            j -= 1
        
        # Convert the result list to a string and return it
        return ''.join(res)
