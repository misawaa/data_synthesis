class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Create a 2D table of size (len(s) + 1) x (len(p) + 1) to store the results of subproblems
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        
        # The empty string matches the empty pattern
        dp[0][0] = True
        
        # Handle patterns that start with '*'
        for j in range(1, len(p) + 1):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-2]
        
        # Fill the table in a bottom-up manner
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                # Case 1: s[i-1] and p[j-1] match or p[j-1] is '.'
                if s[i-1] == p[j-1] or p[j-1] == '.':
                    dp[i][j] = dp[i-1][j-1]
                # Case 2: p[j-1] is '*'
                elif p[j-1] == '*':
                    # Subcase 1: '*' matches zero occurrences of the preceding character
                    dp[i][j] = dp[i][j-2]
                    # Subcase 2: '*' matches one or more occurrences of the preceding character
                    if s[i-1] == p[j-2] or p[j-2] == '.':
                        dp[i][j] |= dp[i-1][j]
                # Case 3: s[i-1] and p[j-1] do not match
                else:
                    dp[i][j] = False
        
        # Return the result for the entire string
        return dp[len(s)][len(p)]
