class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        carry = 1
        
        while i >= 0 and carry > 0:
            digits[i] += carry
            carry = digits[i] // 10
            digits[i] %= 10
            i -= 1
        
        if carry > 0:
            digits.insert(0, carry)
        
        return digits
