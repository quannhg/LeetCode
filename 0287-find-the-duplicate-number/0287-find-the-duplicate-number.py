class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # see value index as f(value) = index => linked list with circle
        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        fast = 0
        while fast != slow:
            fast = nums[fast]
            slow = nums[slow]
        return slow
        