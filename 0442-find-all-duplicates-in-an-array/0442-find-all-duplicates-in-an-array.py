class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        unique_num = set()
        duplicate = set()
        for num in nums:
            if num in unique_num:
                duplicate.add(num)
            else:
                unique_num.add(num)
        return list(duplicate)
        
        