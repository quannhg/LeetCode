# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root):
            """
            :type root: TreeNode
            :rtype: int
            """
            if not root:
                return 0

            depth = 0
            current_level = [root]

            while current_level:
                depth += 1
                next_level = []
                for node in current_level:
                    left = node.left
                    right = node.right
                    if not left and not right:
                        return depth
                    if left:
                        next_level.append(left)
                    if right:
                        next_level.append(right)
                current_level = next_level
            return depth
