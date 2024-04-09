class Solution:
    def receiveFizzBuzz(self, number: int) -> str:
        if number % 3 == 0 and number % 5 == 0:
            return "FizzBuzz"
        elif number % 3 == 0:
            return "Fizz"
        elif number % 5 == 0:
            return "Buzz"
        else:
            return str(number)
            
    def fizzBuzz(self, n: int) -> List[str]:
        return map(self.receiveFizzBuzz, range(1, n + 1))