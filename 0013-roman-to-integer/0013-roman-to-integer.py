class Solution:
    def romanToInt(self, s: str) -> int:
        romanToInt = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        int_value = 0
        for index in range(len(s)):
            symbol_value, next_symbol_value = romanToInt[s[index]], romanToInt[s[index + 1]] if index < len(s) -1 else 0
            if symbol_value >= next_symbol_value:
                int_value += symbol_value
            else:
                int_value -= symbol_value
        return int_value
        