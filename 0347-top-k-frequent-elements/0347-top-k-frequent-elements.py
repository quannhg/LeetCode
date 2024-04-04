class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_count = Counter(nums)
        
        frequent_buckets = [[] for _ in range(len(nums) + 1)]
        
        for num, frequent in nums_count.items():
            frequent_buckets[frequent].append(num)
        
        return [num for bucket in frequent_buckets[::-1] for num in bucket][:k]
        