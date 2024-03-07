class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        snowball_size = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                snowball_size +=1
            elif snowball_size > 0:
                nums[i], nums[i-snowball_size] = 0, nums[i]
                
            
                
        