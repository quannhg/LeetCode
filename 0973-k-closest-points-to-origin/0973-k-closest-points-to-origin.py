class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        k_closest_points = []
        for point in points:
            distance = - (point[0]**2 + point[1]**2) # use negative to build max heap
            if len(k_closest_points) == k:
                heappushpop(k_closest_points, (distance, point[0], point[1]))
            else:
                heappush(k_closest_points, (distance, point[0], point[1]))
        return [(x, y) for _, x, y in k_closest_points]
        