class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Create a dictionary to store the last index of each character seen so far
        last_seen = {}
        # Initialize variables to keep track of the start of the current substring and the length of the longest substring seen so far
        start = 0
        longest = 0
        # Loop through each character in the string
        for i, char in enumerate(s):
            # If the current character has been seen before and its last index is after the start of the current substring, update the start of the current substring
            if char in last_seen and last_seen[char] >= start:
                start = last_seen[char] + 1
            # Update the last index of the current character
            last_seen[char] = i
            # Update the length of the longest substring seen so far
            longest = max(longest, i - start + 1)
        return longest
      
