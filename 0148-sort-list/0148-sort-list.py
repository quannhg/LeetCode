# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge(self, head1, head2) -> Optional[ListNode]:
        tail = head = ListNode()
        while head1 and head2:
            if head1.val < head2.val:
                tail.next, tail, head1 = head1, head1, head1.next
            else:
                tail.next, tail, head2 = head2, head2, head2.next
        tail.next = head1 or head2
        return head.next
    
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head  or not head.next: return head
        prev, slow, fast = None, head, head
        while fast and fast.next:
            prev, slow, fast = slow, slow.next, fast.next.next
        prev.next = None
        return self.merge(*map(self.sortList, (head, slow)))
    
            