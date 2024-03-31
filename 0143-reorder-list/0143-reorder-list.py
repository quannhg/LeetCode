# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getMiddleNode(self, head):
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        return slow
    
    def reverseList(self, head):
        prev = None
        while head:
            next_node = head.next
            head.next = prev
            prev = head
            head = next_node
        return prev
    
    def reorderList(self, head: Optional[ListNode]) -> None:
        mid_node = self.getMiddleNode(head)
        reverse_node = self.reverseList(mid_node.next)
        
        mid_node.next = None #avoid cyclic
        
        while head and reverse_node:
            next_node = head.next
            next_reverse_node = reverse_node.next
            head.next = reverse_node
            head.next.next = next_node
            head = next_node
            reverse_node = next_reverse_node
            
        