class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # initialize the DP table with zeros
        dp = [[0]*n for _ in range(m)]
        
        # set the values of the first row and column to 1
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
        
        # fill in the DP table using dynamic programming
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        # return the value in the bottom-right corner of the DP table
        return dp[m-1][n-1]
