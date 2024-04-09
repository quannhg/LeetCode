class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        fizz = buzz = 0
        string_array = []
        for number in range(1, n + 1):
            fizz += 1
            buzz += 1
            new_string = ""
            if fizz == 3:
                new_string += "Fizz"
                fizz = 0
            if buzz == 5:
                new_string += "Buzz"
                buzz = 0
            if len(new_string) == 0:
                new_string = str(number)
            string_array += [new_string]
        return string_array