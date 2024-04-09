class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left_pointer, right_pointer = 0, len(s) - 1
        while left_pointer < right_pointer:
            s[left_pointer], s[right_pointer] = s[right_pointer], s[left_pointer]
            left_pointer += 1
            right_pointer -= 1
        