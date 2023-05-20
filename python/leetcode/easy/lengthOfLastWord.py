class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Split the input string into a list of words
        words = s.split()
        
        # If there are no words, return 0
        if not words:
            return 0
        
        # Otherwise, return the length of the last word
        last_word = words[-1]
        return len(last_word)
