class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(row, queens, diagonals, anti_diagonals):
            nonlocal count
            if row == n:
                count += 1
                return
            for col in range(n):
                if col not in queens and row - col not in diagonals and row + col not in anti_diagonals:
                    backtrack(row + 1, queens + [col], diagonals + [row - col], anti_diagonals + [row + col])
        
        count = 0
        backtrack(0, [], [], [])
        return count
