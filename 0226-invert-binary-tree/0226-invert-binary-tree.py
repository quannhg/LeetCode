# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None: 
            return None
        
        left_node = root.left
        right_node = root.right
        root.left = self.invertTree(right_node)
        root.right = self.invertTree(left_node)
        
        return root