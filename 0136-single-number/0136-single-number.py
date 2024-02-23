class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums_set = set(nums)
        sum_set = sum(nums_set)
        return sum_set * 2 - sum(nums)
        