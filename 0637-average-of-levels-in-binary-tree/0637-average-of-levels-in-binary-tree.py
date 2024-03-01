# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        info = [] #[[sum_of_level, num_node]]
        def dfs(node, depth=0):
            if node:
                if len(info) == depth:
                    info.append([0,0])
                info[depth][0] += node.val
                info[depth][1] += 1
                dfs(node.left, depth + 1)
                dfs(node.right, depth + 1)
        dfs(root)
        return [sum_of_level/float(num_node) for (sum_of_level, num_node) in info]
        