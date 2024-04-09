class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_amount = {}
        
        for char in s:
            if char in char_amount:
                char_amount[char] += 1
            else:
                char_amount[char] = 1
        
        for index, char in enumerate(s):
            if char_amount[char] == 1:
                return index
        
        return -1
            
            
            
        