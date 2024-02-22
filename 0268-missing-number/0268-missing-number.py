class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        remain_nums = set(range(len(nums)+1))
        for num in nums:
            remain_nums = remain_nums.difference({num})
        return remain_nums.pop()
        
        