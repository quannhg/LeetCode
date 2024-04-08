class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        lps = self.buildLPS(needle)
        needle_index = 0
        
        for index in range(len(haystack)):
            while haystack[index] != needle[needle_index] and needle_index > 0:
                needle_index = lps[needle_index - 1]
            if haystack[index] == needle[needle_index]:
                needle_index += 1
                if needle_index == len(needle):
                    return index - needle_index + 1
        return -1
        
    def buildLPS(self, string) -> List[int]:
        lps = [0] * len(string)
        previous_repeat_index = 0
        for current_index in range(1, len(string)):
            while string[previous_repeat_index] != string[current_index] and previous_repeat_index > 0:
                previous_repeat_index = lps[previous_repeat_index - 1]
            if string[previous_repeat_index] == string[current_index]:
                previous_repeat_index += 1
                lps[current_index] = previous_repeat_index
        return lps