# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMostLeft(self, root: Optional[TreeNode]):
        node = root
        while node.left != None:
            node = node.left
        return node
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root == None:
            return root
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.left == None:
                return root.right
            elif root.right == None:
                return root.left
            
            most_left_node = self.findMostLeft(root.right)
            root.val = most_left_node.val
            root.right = self.deleteNode(root.right, root.val)
        return root
            
            