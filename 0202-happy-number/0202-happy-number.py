class Solution:
    def sumSquareDigits(self, n: int) -> int:
        square_sum = 0
        while n != 0:
            digit = n % 10
            square_sum += digit * digit
            n //= 10
        return square_sum

    def isHappy(self, n: int) -> bool:
        slow = fast = n

        while True:
            slow = self.sumSquareDigits(slow)
            fast = self.sumSquareDigits(fast)
            fast = self.sumSquareDigits(fast)
            if fast == 1 or slow == 1: 
                return True
            if fast == slow:
                return False