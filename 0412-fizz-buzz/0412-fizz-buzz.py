class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        return map(lambda number: "Fizz" * (not number % 3) + "Buzz" * (not number % 5) or str(number), range(1, n + 1))