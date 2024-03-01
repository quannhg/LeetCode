# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        averages = []
        current_level = [root]
        while any(current_level):
            current_sum, current_node_amount, next_level = 0, 0, []
            for node in current_level:
                current_sum += node.val
                current_node_amount +=1
                if node.left: next_level.append(node.left)
                if node.right: next_level.append(node.right)
            averages.append(current_sum / float(current_node_amount))
            current_level = next_level
        return averages
            
        