class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        def backtrack(index, combination):
            if index == len(digits):
                result.append(combination)
                return
                
            for letter in mapping[digits[index]]:
                backtrack(index+1, combination+letter)
                
        result = []
        backtrack(0, "")
        return result
