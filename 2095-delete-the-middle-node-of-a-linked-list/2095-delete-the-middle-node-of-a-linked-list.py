# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(head.next is None):
            return head.next
        l=head
        r=head
        pv=None
        while(r!=None and r.next!=None):
            pv=l
            l=l.next
            r=r.next.next
        # l at middle 
        pv.next=l.next
        return head