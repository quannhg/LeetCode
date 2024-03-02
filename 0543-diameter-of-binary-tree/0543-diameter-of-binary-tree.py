# Idea 1 Implementation!
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        max_diameter = 0
        def diameterOfNode(node):
            nonlocal max_diameter
            if node is None: return 0
            left_diameter = diameterOfNode(node.left)
            right_diameter = diameterOfNode(node.right)
            max_diameter = max(max_diameter, left_diameter + right_diameter)
            return 1 + max(right_diameter, left_diameter)
        diameterOfNode(root)
        return max_diameter