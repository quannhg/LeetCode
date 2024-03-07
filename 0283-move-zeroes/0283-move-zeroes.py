class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left_pointer, right_pointer = 0, len(nums)-1
        
        def moveZeroToTail():
            nonlocal left_pointer, right_pointer
            for i in range(left_pointer, right_pointer):
                nums[i] = nums[i+1]
            nums[right_pointer] = 0
            right_pointer -= 1
            
        while(left_pointer<right_pointer):
            if(nums[left_pointer] == 0):
                moveZeroToTail()
            else:
                left_pointer += 1
                
        