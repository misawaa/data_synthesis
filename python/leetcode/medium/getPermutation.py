class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # create a list of numbers from 1 to n
        nums = [i for i in range(1, n+1)]
        
        # create a list of factorials from 0! to (n-1)!
        factorials = [1] * n
        for i in range(1, n):
            factorials[i] = factorials[i-1] * i
        
        # decrement k to convert it to 0-based indexing
        k -= 1
        
        # initialize the result string
        res = ""
        
        # loop through the digits in the result string
        for i in range(n-1, -1, -1):
            # compute the index of the current digit
            idx = k // factorials[i]
            
            # add the current digit to the result string
            res += str(nums[idx])
            
            # remove the current digit from the list of numbers
            nums.pop(idx)
            
            # update k to the remaining index
            k %= factorials[i]
        
        return res
      
