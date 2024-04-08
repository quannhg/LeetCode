class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0: return ""
        
        sort_strings = sorted(strs)
        prefix, first_string, last_string = "", sort_strings[0], sort_strings[-1]
        
        for index in range(min(len(first_string), len(last_string))):
            if first_string[index] == last_string[index]:
                prefix += first_string[index]
            else: break
        return prefix