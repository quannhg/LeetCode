class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = reduce(lambda array, new_num: array + [new_num] if array[-1] != new_num else array, nums[1:], [nums[0]])
        return len(nums)