class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        back = lambda res, c: res[:-1] if c == '#' else res + c
        return reduce(back, s, "") == reduce(back, t, "")
