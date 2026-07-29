# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def totalEle(head):
            temp=head
            cnt=0
            while(temp!=None):
                cnt+=1
                temp=temp.next
            return cnt
        # base condition
        if(head==None or head.next==None or k==0):
            return head
        tail=head
        while(tail.next!=None) : # at last node
            tail=tail.next
        # total element in the LL
        total = totalEle(head)
        # now make it circular
        tail.next=head
        k = k%total
        # moves steps to get rotate head
        steps=total-k
        curr=head
        while(steps-1>0):
            curr=curr.next
            steps-=1
        cnext = curr.next
        # make curr.next is None
        curr.next=None
        return cnext

            
