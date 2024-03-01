# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root):
        if not root: return 0
        
        current_level = [root]
        depth = 0
        
        while current_level:
            depth += 1
            next_level = []
            for node in current_level:
                if not (node.left or node.right): return depth
                if node.left: next_level.append(node.left)
                if node.right: next_level.append(node.right)
            current_level = next_level
        return -1
