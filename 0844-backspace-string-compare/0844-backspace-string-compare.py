class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def backspacePointer(pointer, string):
            skip = 0
            while pointer >= 0 and (string[pointer] == '#' or skip > 0):
                skip += 1 if string[pointer] == '#' else -1
                pointer -= 1
            return pointer

        s_pointer, t_pointer = len(s) - 1, len(t) - 1

        while s_pointer >= 0 or t_pointer >= 0:
            s_pointer = backspacePointer(s_pointer, s)
            t_pointer = backspacePointer(t_pointer, t)

            if s_pointer == -1 or t_pointer == -1:
                return s_pointer == t_pointer

            if s[s_pointer] != t[t_pointer]:
                return False

            s_pointer -= 1
            t_pointer -= 1

        return s_pointer == t_pointer
