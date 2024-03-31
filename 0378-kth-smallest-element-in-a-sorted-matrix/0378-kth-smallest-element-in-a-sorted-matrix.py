class Solution:
    def countLessOrEqual(self, matrix, value):
        num_element = 0
        col_idx = len(matrix[0]) - 1 # start with the rightmost element
        for row_idx in range(len(matrix)):
            while col_idx >= 0 and matrix[row_idx][col_idx] > value: col_idx -= 1
            num_element += col_idx + 1
        return num_element
    
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        left, right = matrix[0][0], matrix[len(matrix) - 1][len(matrix) - 1]
        kthSmallestNum = -1
        while(left <= right):
            mid = (left + right) // 2
            if self.countLessOrEqual(matrix, mid) >= k:
                kthSmallestNum = mid
                right = mid - 1
            else:
                left = mid + 1
        return kthSmallestNum