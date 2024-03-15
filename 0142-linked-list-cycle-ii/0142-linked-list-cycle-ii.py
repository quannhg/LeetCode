# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head
        # find the intersection
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if fast == slow:
                break # fast and slow is in intersection
        else:
            return None
        while head != slow:
            head, slow = head.next, slow.next    
        return head
        
        # x: distance from head to begining of the cicle -> slow move = x + y
        # fast move = 2(x+y)
        # 2(x+y) - (x+y) = N*C
        # x = NC - y
        # x + y + NC -y = x + NC
        # head = slow 