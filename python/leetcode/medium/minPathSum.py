class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [0 for j in range(n)]
        
        # Base case
        dp[0] = grid[0][0]
        
        # Fill in first row
        for j in range(1, n):
            dp[j] = dp[j-1] + grid[0][j]
        
        # Fill in rest of the cells
        for i in range(1, m):
            # Fill in first column
            dp[0] += grid[i][0]
            for j in range(1, n):
                dp[j] = min(dp[j], dp[j-1]) + grid[i][j]
        
        return dp[n-1]
