class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0: return []
        result = []
        upper_row, bottom_row, left_col, right_col = 0, len(matrix) - 1, 0, len(matrix[0]) -1
        while True:
            for col_idx in range(left_col, right_col + 1):
                result.append(matrix[upper_row][col_idx])
            upper_row += 1
            if upper_row > bottom_row:
                return result
            
            for row_idx in range(upper_row, bottom_row + 1):
                result.append(matrix[row_idx][right_col])
            right_col -= 1
            if left_col > right_col:
                return result
            
            for col_idx in range(right_col, left_col -1, -1):
                result.append(matrix[bottom_row][col_idx])
            bottom_row -= 1
            if upper_row > bottom_row:
                return result
            
            for row_idx in range(bottom_row, upper_row -1, -1):
                result.append(matrix[row_idx][left_col])
            left_col += 1
            if left_col > right_col:
                return result
            
        