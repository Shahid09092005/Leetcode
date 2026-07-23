# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if(head==None or head.next==None):
            return False
        l = head
        r=head
        while(r!=None and r.next!=None):
            l=l.next
            if(r.next.next==None) :
                return False
            r=r.next.next
            if(l==r):
                return True
        return False

        