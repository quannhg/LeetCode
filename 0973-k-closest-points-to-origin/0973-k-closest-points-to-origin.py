class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        left, right = 0, len(points) - 1
        while left <= right:
            mid = self.partition(points, left, right)
            if mid == k: break
            elif mid < k: left = mid + 1
            elif mid > k: right = mid - 1
        return points[:k]
    
    def partition(self, points, left, right):
        pivot = points[left]
        while left < right:
            while left < right and self.compareDistance(points[right], pivot) > 0: right -= 1
            points[left] = points[right]
            while left < right and self.compareDistance(points[left], pivot) <= 0: left += 1
            points[right] = points[left]
        points[left] = pivot
        return left
        
    def compareDistance(self, point1, point2):
        return point1[0]**2 + point1[1]**2 - point2[0]**2 - point2[1]**2
        