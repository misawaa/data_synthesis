class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def is_valid(row, col, num):
            # check row
            for j in range(9):
                if board[row][j] == num:
                    return False
            
            # check column
            for i in range(9):
                if board[i][col] == num:
                    return False
            
            # check sub-box
            box_row = (row // 3) * 3
            box_col = (col // 3) * 3
            for i in range(box_row, box_row + 3):
                for j in range(box_col, box_col + 3):
                    if board[i][j] == num:
                        return False
            
            return True
        
        def backtrack():
            nonlocal solved
            # find the first empty cell
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        # try all possible digits
                        for num in '123456789':
                            if is_valid(i, j, num):
                                board[i][j] = num
                                if backtrack():
                                    return True
                                board[i][j] = '.'
                        return False
            solved = True
            return True
        
        solved = False
        backtrack()
