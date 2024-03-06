class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums_appear = defaultdict(int)
        for num in nums:
            nums_appear[num] += 1
            
        half_len = len(nums) // 2
        
        for key, value in nums_appear.items():
            if value > half_len:
                return key
        return -1
        
        