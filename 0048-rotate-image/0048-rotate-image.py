class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix.reverse()
        for row_idx in range(len(matrix)):
            for col_idx in range(row_idx):
                matrix[row_idx][col_idx],  matrix[col_idx][row_idx] = matrix[col_idx][row_idx], matrix[row_idx][col_idx]
        