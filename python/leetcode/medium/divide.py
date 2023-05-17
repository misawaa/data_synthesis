class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if divisor == 0:
            return 2**31 - 1
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1

        # get signs and convert to positive
        sign = 1
        if dividend < 0:
            sign *= -1
            dividend *= -1
        if divisor < 0:
            sign *= -1
            divisor *= -1

        # binary search for quotient
        left, right = 0, dividend
        while left <= right:
            mid = (left + right) // 2
            if divisor * mid <= dividend < divisor * (mid + 1):
                return sign * mid
            elif divisor * mid > dividend:
                right = mid - 1
            else:
                left = mid + 1
                
