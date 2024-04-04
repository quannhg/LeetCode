class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_count = Counter(nums)
        
        frequent_buckets = [[] for _ in range(len(nums) + 1)]
        
        for num, frequent in nums_count.items():
            frequent_buckets[frequent].append(num)
        
        top_k_frequent = []
        for bucket in frequent_buckets[::-1]:
            top_k_frequent += bucket
            if len(top_k_frequent) >= k:
                break
                
        return top_k_frequent
        