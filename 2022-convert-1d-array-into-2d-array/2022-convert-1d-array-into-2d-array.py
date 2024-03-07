class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m*n != len(original):
            return []
        result = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                result[i][j] = original[n*i+j]
        return result
                
            
        