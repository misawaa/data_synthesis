class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Initialize the result list
        res = []
        
        # Define the recursive function to generate the combinations
        def backtrack(s='', left=0, right=0):
            # Base case: if the length of the string is 2n, add it to the result list
            if len(s) == 2 * n:
                res.append(s)
                return
            
            # Recursive case: add a left parenthesis if there are less than n left parentheses
            if left < n:
                backtrack(s + '(', left + 1, right)
            
            # Recursive case: add a right parenthesis if there are less right parentheses than left parentheses
            if right < left:
                backtrack(s + ')', left, right + 1)
        
        # Call the recursive function to generate the combinations
        backtrack()
        
        # Return the result list
        return res
