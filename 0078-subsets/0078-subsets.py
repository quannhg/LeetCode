class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        power_sets = [[]]
        for num in nums:
            for idx in range(len(power_sets)):
                power_sets += [power_sets[idx] + [num]]
        return power_sets
        