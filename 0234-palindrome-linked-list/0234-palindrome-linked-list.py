# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if(head==None or head.next==None):
            return True
        l=head
        r=head
        # get middle if LL is Odd
        # get left middle of LL is Even
        while(r.next!=None and r.next.next!=None):
            l=l.next
            r=r.next.next
        # Reverse linkedlist
        def reverseLL(head):
            curr=head
            p=None
            n=None
            while(curr!=None):
                n=curr.next
                curr.next = p
                p=curr
                curr=n
            return p
        middleNode = reverseLL(l.next)
        r=middleNode
        l=head
        while(r!=None):
            if(l.val!=r.val):
                return False
            r=r.next
            l=l.next
        return True
            
        
        