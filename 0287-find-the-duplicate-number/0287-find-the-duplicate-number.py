class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        appear_nums = set()
        for num in nums:
            if num in appear_nums:
                return num
            else:
                appear_nums.add(num)
        return -1
        