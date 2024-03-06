class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def backspacePointer(pointer, s):
            amount_character_remove = 0
            while (s[pointer] == '#' or amount_character_remove > 0) and pointer >= 0:
                if s[pointer] == '#':
                    amount_character_remove += 1
                else:
                    amount_character_remove -=1
                pointer -=1
            return pointer
                
            
        s_pointer, t_pointer = len(s) - 1, len(t) - 1
        while s_pointer >= 0 or t_pointer >= 0:
            
            s_pointer, t_pointer = backspacePointer(s_pointer, s), backspacePointer(t_pointer, t)
            if s_pointer == -1 or t_pointer == -1:
                return s_pointer == t_pointer
            if s[s_pointer] != t[t_pointer]:
                return False
            s_pointer -=1
            t_pointer -=1
        return s_pointer == t_pointer
            
            
        