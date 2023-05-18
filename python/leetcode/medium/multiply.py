class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1, n2 = len(num1), len(num2)
        result = [0] * (n1 + n2)
        
        # multiply each digit of num2 with num1 and add up the results
        for i in range(n2-1, -1, -1):
            for j in range(n1-1, -1, -1):
                product = int(num2[i]) * int(num1[j])
                pos1, pos2 = i+j, i+j+1
                carry, total = divmod(product + result[pos2], 10)
                result[pos1] += carry
                result[pos2] = total
        
        # remove leading zeros and convert to string
        start = 0
        while start < len(result) and result[start] == 0:
            start += 1
        if start == len(result):
            return "0"
        return ''.join(map(str, result[start:]))
