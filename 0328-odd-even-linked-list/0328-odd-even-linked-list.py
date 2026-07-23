# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(head==None or head.next==None):
            return head
        oddh=head
        odd=head
        evenh=odd.next
        even=evenh
        while(even!=None and even.next!=None):
            odd.next=odd.next.next
            odd = odd.next
            even.next=even.next.next # points to next'even
            even = even.next # reach to that node
        odd.next=evenh
        return oddh
