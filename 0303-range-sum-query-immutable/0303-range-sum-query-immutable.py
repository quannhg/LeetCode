class NumArray:

    def __init__(self, nums: List[int]):
        self.pre_sums = nums
        for i in range(len(nums)-1):
            self.pre_sums[i+1] = self.pre_sums[i] + self.pre_sums[i+1] 

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.pre_sums[right]
        return self.pre_sums[right] - self.pre_sums[left - 1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)