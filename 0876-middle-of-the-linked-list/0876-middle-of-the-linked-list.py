# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        mid_idx = self.length(head) // 2
        mid_node = head
        while mid_idx > 0:
            mid_node = mid_node.next
            mid_idx -= 1
        return mid_node
    
    def length(self, head: Optional[ListNode]) -> int:
        if not head:
            return 0;
        return 1 + self.length(head.next)
            
            
        