class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def addParenthesis(amount_left, amount_right, cur_str):
            if amount_left >= n:
                if amount_right >= n:
                    return [cur_str]
                else:
                    return addParenthesis(amount_left, amount_right + 1, cur_str + ')')
            if amount_left > amount_right:
                return addParenthesis(amount_left + 1, amount_right, cur_str +'(') + addParenthesis(amount_left, amount_right+1, cur_str + ')')
            else:
                return addParenthesis(amount_left + 1, amount_right, cur_str + '(')
        return addParenthesis(0, 0, "")
        