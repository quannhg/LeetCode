class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        col_0 = False;
        for row_idx, row in enumerate(matrix):
            for col_idx, num in enumerate(row):
                if num == 0:
                    matrix[row_idx][0] = 0
                    if col_idx == 0:
                        col_0 = True;
                    else:
                        matrix[0][col_idx] = 0 
        # hanle col 0 affer handler row
        for col_idx in range(1, len(matrix[0])):
            if matrix[0][col_idx] == 0:
                for row_idx in range(1, len(matrix)):
                    matrix[row_idx][col_idx] = 0
        for row_idx in range(len(matrix)):
            if matrix[row_idx][0] == 0:
                for col_idx in range(1, len(matrix[0])):
                    matrix[row_idx][col_idx] = 0
        
        # hanle col 0
        if col_0:
            for row_idx in range(len(matrix)):
                matrix[row_idx][0] = 0
            