class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        for point in points:
            heappush(min_heap, (point[0]**2 + point[1]**2, point[0], point[1]))
        k_closest_points = []
        for i in range(k):
            closest_point = heappop(min_heap)
            k_closest_points.append([closest_point[1], closest_point[2]])
        return k_closest_points
        