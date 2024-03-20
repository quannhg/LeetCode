class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        def casePermutationTraverse(cur_str):
            cur_str_len = len(cur_str)
            if cur_str_len == len(s):
                return [cur_str]
            
            if s[cur_str_len].upper() != s[cur_str_len].lower():
                return casePermutationTraverse(cur_str + s[cur_str_len].upper()) + casePermutationTraverse(cur_str + s[cur_str_len].lower())
            return casePermutationTraverse(cur_str + s[cur_str_len])
        return casePermutationTraverse("")
        