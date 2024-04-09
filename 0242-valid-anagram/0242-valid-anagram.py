class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        
        alphabet = [0] * 26
        for char in s:
            alphabet[ord(char) - ord('a')] += 1
        for char in t:
            alphabet[ord(char) - ord('a')] -= 1
        
        return all(count == 0 for count in alphabet)
        