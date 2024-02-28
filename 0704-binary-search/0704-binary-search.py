class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) -1
        while lo < hi:
            mid = lo + (hi - lo + 1) // 2
            if nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid
        return lo if nums[lo] == target else -1
        