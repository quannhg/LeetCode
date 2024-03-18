class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_row = set()
        zero_col = set()
        for row_idx, row in enumerate(matrix):
            for col_idx, num in enumerate(row):
                if num == 0:
                    zero_row.add(row_idx)
                    zero_col.add(col_idx)
        for row_idx in zero_row:
            for col_idx in range(len(matrix[row_idx])):
                matrix[row_idx][col_idx] = 0
        for col_idx in zero_col:
            for row_idx in range(len(matrix)):
                matrix[row_idx][col_idx] = 0
        