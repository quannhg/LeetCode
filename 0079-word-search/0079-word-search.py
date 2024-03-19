class Solution:
    def travel(self, board: List[List[str]], word: str, row_idx: int, col_idx: int) -> bool:
        if board[row_idx][col_idx] != word[0]:
            return False
        if len(word) == 1:
            return True
        
        board[row_idx][col_idx] = ""
        
        if (row_idx - 1 >= 0) and len(board[row_idx - 1][col_idx]) == 1:
            if self.travel(board, word[1:], row_idx - 1, col_idx):
                return True
            
        if (row_idx + 1 < len(board)) and len(board[row_idx + 1][col_idx]) == 1:
            if self.travel(board, word[1:], row_idx + 1, col_idx):
                return True
            
        if (col_idx - 1 >= 0) and len(board[row_idx][col_idx - 1]) == 1:
            if self.travel(board, word[1:], row_idx, col_idx - 1):
                return True
            
        if (col_idx + 1 < len(board[0])) and len(board[row_idx][col_idx + 1]) == 1:
            if self.travel(board, word[1:], row_idx, col_idx + 1):
                return True
        
        board[row_idx][col_idx] = word[0]
        return False
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        for row_idx in range(len(board)):
            for col_idx in range(len(board[row_idx])):
                if self.travel(board, word, row_idx, col_idx):
                    return True
        return False
