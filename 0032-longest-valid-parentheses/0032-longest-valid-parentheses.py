class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # create invalid parentheses stack
        invalid_bracket_stack = []
        for index in range(len(s)):
            if s[index] == "(":
                invalid_bracket_stack.append(index)
            elif s[index] == ")":
                if len(invalid_bracket_stack) and s[invalid_bracket_stack[-1]] == "(":
                    invalid_bracket_stack.pop()
                else:
                    invalid_bracket_stack.append(index)
        
        # find max valid
        longest_valid_parentheses = len(s) if len(invalid_bracket_stack) == 0 else 0
        backward_valid_bracket = len(s)
        while invalid_bracket_stack:
            front_bracket_index = invalid_bracket_stack.pop()
            valid_parentheses_len = backward_valid_bracket - front_bracket_index - 1
            longest_valid_parentheses = max(longest_valid_parentheses, valid_parentheses_len)
            backward_valid_bracket = front_bracket_index
        
        # compare with the first valid range
        return max(longest_valid_parentheses, backward_valid_bracket)
                    
            
        