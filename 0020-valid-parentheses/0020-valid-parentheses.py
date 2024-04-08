class Solution:
    def isValid(self, s: str) -> bool:
        brackets_stack = []
        matching_brackets = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }
        for bracket in s:
            if bracket in "([{":
                brackets_stack.append(bracket)
            else:
                if not brackets_stack or brackets_stack.pop() != matching_brackets[bracket]:
                    return False
        return len(brackets_stack) == 0
        