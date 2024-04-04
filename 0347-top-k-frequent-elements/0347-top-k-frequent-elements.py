class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_count = Counter(nums)
        
        top_k = []
        for num, frequent in nums_count.items():
            if len(top_k) == k:
                heappushpop(top_k, (frequent, num))
            else:
                heappush(top_k, (frequent, num))
        
        return [num for _, num in top_k]