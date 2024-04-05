class Solution:
    def lettersOfNum(self, num: str) -> List[str]:
        mapping_of_digits = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }
        return mapping_of_digits[num]
    
    def addNewLetter(self, digits:str, result: str):
        if len(digits) == 0:
            return [result]
        else:
            letter_combinations = map(lambda new_letter: result + new_letter, self.lettersOfNum(digits[0]))
        return reduce(lambda acc, new_combination: acc + self.addNewLetter(digits[1:], new_combination), letter_combinations, [])
        
    
    def letterCombinations(self, digits: str) -> List[str]:
        return self.addNewLetter(digits, "") if len(digits) != 0 else []
        