class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        prev = self.countAndSay(n - 1)
        result = ""
        
        count = 0
        curr = None
        for digit in prev:
            if digit == curr:
                count += 1
            else:
                if count > 0:
                    result += str(count) + curr
                curr = digit
                count = 1
        
        # append the last count and digit
        result += str(count) + curr
        
        return result
