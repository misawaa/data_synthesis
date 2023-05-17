class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1] # base index
        max_len = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack: # empty stack, push current index as new base
                    stack.append(i)
                else:
                    max_len = max(max_len, i - stack[-1])
        return max_len
