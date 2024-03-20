class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return reduce(lambda acc, ele: acc + [power_set + [ele] for power_set in acc],nums, [[]])
        