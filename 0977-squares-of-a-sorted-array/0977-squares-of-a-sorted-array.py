class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        firstPointer, lastPointer, writePointer = 0, len(nums) -1, len(nums) - 1
        result = [0] * len(nums)
        while firstPointer < lastPointer:
            if abs(nums[firstPointer]) >= (nums[lastPointer]):
                result[writePointer] = nums[firstPointer] ** 2
                firstPointer += 1
                writePointer -= 1
            else:
                result[writePointer] = nums[lastPointer] ** 2
                lastPointer -= 1
                writePointer -= 1
        result[0] = nums[firstPointer] ** 2
        
        return result
        
        