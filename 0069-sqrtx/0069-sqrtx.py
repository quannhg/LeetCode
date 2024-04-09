class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1: return x
        
        left, right= 1, x
        while left <= right:
            mid = (left + right) // 2
            square = mid * mid
            if square > x:
                right = mid - 1
            elif square < x:
                left = mid + 1
            else:
                return mid
            
        return right 