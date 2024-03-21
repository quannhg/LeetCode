class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def addParenthesis(amount_left, amount_right, cur_str):
            nonlocal result
            if len(cur_str) == 2*n:
                result.append(cur_str)
            if amount_left < n:
                addParenthesis(amount_left + 1, amount_right , cur_str + '(')
            if amount_left > amount_right:
                addParenthesis(amount_left, amount_right+1, cur_str + ')')
        addParenthesis(0, 0, "")
        return result
        