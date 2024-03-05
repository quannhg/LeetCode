class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        firstPointer, lastPointer, result = 0, len(nums) -1, []
        while firstPointer < lastPointer:
            if abs(nums[firstPointer]) >= (nums[lastPointer]):
                result.insert(0, nums[firstPointer] ** 2)
                firstPointer += 1
            else:
                result.insert(0, nums[lastPointer] ** 2)
                lastPointer -= 1
        result.insert(0, nums[firstPointer] ** 2)
        
        return result
        
        