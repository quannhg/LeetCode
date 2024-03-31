class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        matrix_edge_len = len(matrix)
        min_heap = [] # [(val, row_idx, col_idx)]
        for row_idx in range(min(matrix_edge_len, k)):
            heappush(min_heap, (matrix[row_idx][0], row_idx, 0))
        min_num = -1
        for kthSmall in range(k):
            min_num, row_idx, col_idx = heappop(min_heap)
            if col_idx + 1 < matrix_edge_len: heappush(min_heap, (matrix[row_idx][col_idx + 1], row_idx, col_idx + 1))
        return min_num