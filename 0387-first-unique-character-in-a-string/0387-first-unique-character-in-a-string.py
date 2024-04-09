class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_amount = Counter(s)
        
        for index, char in enumerate(s):
            if char_amount[char] == 1:
                return index
        
        return -1
            
            
            
        