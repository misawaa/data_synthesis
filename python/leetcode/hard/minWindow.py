// minimun windows substring
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq = {}
        for c in t:
            freq[c] = freq.get(c, 0) + 1
        
        left = right = 0
        count = len(t)
        min_len = float('inf')
        start_index = 0
        
        for right in range(len(s)):
            if s[right] in freq:
                if freq[s[right]] > 0:
                    count -= 1
                freq[s[right]] -= 1
            
            while count == 0:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    start_index = left
                
                if s[left] in freq:
                    freq[s[left]] += 1
                    if freq[s[left]] > 0:
                        count += 1
                left += 1
        
        if min_len == float('inf'):
            return ""
        else:
            return s[start_index:start_index+min_len]
