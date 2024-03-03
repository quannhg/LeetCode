# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isEqual(root1, root2):
            if root1 == None or root2 == None: return root1 == root2
            return root1.val == root2.val and isEqual(root1.left, root2.left) and isEqual(root1.right, root2.right)
        def dfs(root, subRoot):
            if root == None: return False
            return isEqual(root, subRoot) or dfs(root.left, subRoot) or dfs(root.right, subRoot)
        return dfs(root, subRoot)
        