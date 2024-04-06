class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        kth_largest_element = []
        for num in nums:
            if len(kth_largest_element) < k:
                heappush(kth_largest_element, num)
            else:
                heappushpop(kth_largest_element, num)
        return heappop(kth_largest_element)