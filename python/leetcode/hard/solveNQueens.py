class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtrack(row, queens, diagonals, anti_diagonals):
            if row == n:
                result.append(queens)
                return
            for col in range(n):
                if col not in queens and row - col not in diagonals and row + col not in anti_diagonals:
                    backtrack(row + 1, queens + [col], diagonals + [row - col], anti_diagonals + [row + col])
        
        result = []
        backtrack(0, [], [], [])
        return [['.' * col + 'Q' + '.' * (n - col - 1) for col in row] for row in result]
