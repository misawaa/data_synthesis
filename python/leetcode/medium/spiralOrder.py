class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        
        m, n = len(matrix), len(matrix[0])
        result = []
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        # initial direction is to move right
        direction = directions[0]
        row, col = 0, 0
        
        # keep track of the visited positions
        visited = [[False] * n for _ in range(m)]
        
        # loop through all the elements in the matrix
        for _ in range(m * n):
            result.append(matrix[row][col])
            visited[row][col] = True
            next_row, next_col = row + direction[0], col + direction[1]
            if 0 <= next_row < m and 0 <= next_col < n and not visited[next_row][next_col]:
                # move to the next position in the same direction
                row, col = next_row, next_col
            else:
                # change direction
                direction = directions[(directions.index(direction) + 1) % 4]
                row, col = row + direction[0], col + direction[1]
        
        return result
