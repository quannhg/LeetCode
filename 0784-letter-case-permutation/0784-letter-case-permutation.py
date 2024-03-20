class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        permutation = [""]
        for char in s:
            if char.isalpha():
                permutation = [perm + case for perm in permutation for case in [char.upper(), char.lower()]]
            else:
                permutation = [perm + char for perm in permutation]
        return permutation