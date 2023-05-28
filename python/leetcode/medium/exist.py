class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        
        def backtrack(i, j, k, visited):
            if k == len(word):
                return True
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[k] or (i, j) in visited:
                return False
            
            visited.add((i, j))
            found = backtrack(i+1, j, k+1, visited) \
                    or backtrack(i-1, j, k+1, visited) \
                    or backtrack(i, j+1, k+1, visited) \
                    or backtrack(i, j-1, k+1, visited)
            visited.remove((i, j))
            
            return found
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and backtrack(i, j, 0, set()):
                    return True
                
        return False
