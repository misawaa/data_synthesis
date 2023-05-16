class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Handle special cases where numRows is 1 or s is shorter than numRows
        if numRows == 1 or numRows >= len(s):
            return s
        # Initialize variables for the zigzag pattern
        rows = [''] * numRows
        index = 0
        step = 1
        # Loop through each character in s and add it to the corresponding row in the zigzag pattern
        for c in s:
            rows[index] += c
            if index == 0:
                step = 1
            elif index == numRows-1:
                step = -1
            index += step
        # Join the rows together to form the final string
        return ''.join(rows)
