class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # initialize the matrix with zeros
        matrix = [[0]*n for _ in range(n)]
        
        # define the boundaries of the matrix
        top, bottom, left, right = 0, n-1, 0, n-1
        
        # initialize the counter and the direction variables
        num, direction = 1, 0
        
        while top <= bottom and left <= right:
            if direction == 0:  # move right
                for i in range(left, right+1):
                    matrix[top][i] = num
                    num += 1
                top += 1
            elif direction == 1:  # move down
                for i in range(top, bottom+1):
                    matrix[i][right] = num
                    num += 1
                right -= 1
            elif direction == 2:  # move left
                for i in range(right, left-1, -1):
                    matrix[bottom][i] = num
                    num += 1
                bottom -= 1
            else:  # move up
                for i in range(bottom, top-1, -1):
                    matrix[i][left] = num
                    num += 1
                left += 1
            
            # updatethe direction variable
            direction = (direction + 1) % 4
        
        return matrix
