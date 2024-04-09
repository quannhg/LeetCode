class Solution:
    def mySqrt(self, x: int) -> int:
        for num in range(0, x+2):
            if num * num > x:
                return num - 1
        return -1