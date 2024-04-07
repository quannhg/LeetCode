class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal_triangle = []
        for row_level in range(numRows):
            new_level = [1] * (row_level + 1)
            for idx in range(1, len(new_level) - 1):
                new_level[idx] = pascal_triangle[-1][idx - 1] + pascal_triangle[-1][idx]
            pascal_triangle += [new_level]
        return pascal_triangle
            
        