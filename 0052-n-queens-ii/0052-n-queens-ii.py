class Solution:
    def isValidPlace(self, row_i, col_i, location):
        for old_row_i, old_col_i in location:
            if old_col_i == col_i:
                return False
            if old_col_i > col_i and (old_col_i - col_i == row_i - old_row_i):
                return False
            if old_col_i < col_i and (col_i - old_col_i == row_i - old_row_i):
                return False
        return True
    
    def placeQueen(self, location, n):        
        newest_location, amount_place_way = location[-1], 0
        newest_row = newest_location[0]
        
        if newest_row + 1 == n:
            return 1
        
        for col_i in range(n):
            if self.isValidPlace(newest_row + 1, col_i, location):
                amount_place_way += self.placeQueen(location + [(newest_row + 1, col_i)], n)
        
        return amount_place_way
    
    def totalNQueens(self, n: int) -> int:
        total_way_place_queen = 0
        for col_i in range(n):
            total_way_place_queen += self.placeQueen([(0, col_i)], n)
        return total_way_place_queen