class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams = {}
        
        # Iterate over each string in the input list
        for s in strs:
            # Sort the string to get a key
            key = ''.join(sorted(s))
            # Add the string to the corresponding list of anagrams
            if key in anagrams:
                anagrams[key].append(s)
            else:
                anagrams[key] = [s]
        
        # Return the values of the dictionary as a list of lists
        return list(anagrams.values())
