class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0: return False
        i = 0
        while 3 ** i < abs(n):
            i += 1
        return 3 ** i == n