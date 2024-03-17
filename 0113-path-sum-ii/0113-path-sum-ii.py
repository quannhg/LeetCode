# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root: Optional[TreeNode], curr_list: List[int], targetSum: int) ->List[List[int]]:
        if root is None:
            return []
        
        curr_list.append(root.val)
        if root.left == None and root.right == None:
            if sum(curr_list) == targetSum:
                return [curr_list]
            else: return []
        else:
            left_paths = self.helper(root.left, curr_list.copy(), targetSum)
            right_paths = self.helper(root.right, curr_list.copy(), targetSum)
            return left_paths + right_paths

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root is None: return []
        return self.helper(root, [], targetSum)
        