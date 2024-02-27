# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visitedNodes = set()
        currentNode = head
        while currentNode:
            if currentNode in visitedNodes:
                return True
            visitedNodes.add(currentNode)
            currentNode = currentNode.next
        return False
        