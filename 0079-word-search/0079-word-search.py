class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row_len, col_len = len(board), len(board[0])
        def match(idx, row, col, visited_cell):
            if (row, col) in visited_cell: return False
            if not ( 0 <= row < row_len and 0 <= col < col_len) : return False
            if idx == 0: return board[row][col] == word[idx]
            return board[row][col] == word[idx] and any(match(idx - 1, *cell_idx, visited_cell | {(row, col)}) for cell_idx in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)])
        return any(match(len(word) - 1, row, col, set()) for col in range(col_len) for row in range(row_len))
