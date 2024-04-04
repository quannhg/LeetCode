class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0: return 0
        
        number_islands = 0
        for row_idx in range(len(grid)):
            for col_idx in range(len(grid[0])):
                if grid[row_idx][col_idx] == "1":
                    number_islands += 1
                    self.markVisitedIslands(row_idx, col_idx, grid)
        return number_islands
    
    def markVisitedIslands(self, row_idx: int, col_idx: int, grid: List[List[str]]):
        if grid[row_idx][col_idx] == "1":
            grid[row_idx][col_idx] = "0"
            if row_idx > 0: self.markVisitedIslands(row_idx - 1, col_idx, grid)
            if row_idx < len(grid) - 1: self.markVisitedIslands(row_idx + 1, col_idx, grid)
            if col_idx > 0: self.markVisitedIslands(row_idx, col_idx - 1, grid)
            if col_idx < len(grid[0]) - 1: self.markVisitedIslands(row_idx, col_idx + 1, grid)
        
                
        