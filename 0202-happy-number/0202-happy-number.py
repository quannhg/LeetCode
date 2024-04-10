class Solution:
    def isHappy(self, n: int) -> bool:
        square_digits_set = set()
        while True:
            square_sum = 0
            while n != 0:
                remain = n % 10
                square_sum += remain ** 2
                n //= 10 
            if square_sum == 1:
                return True
            if square_sum in square_digits_set:
                return False
            else:
                square_digits_set.add(square_sum)
                n = square_sum
                