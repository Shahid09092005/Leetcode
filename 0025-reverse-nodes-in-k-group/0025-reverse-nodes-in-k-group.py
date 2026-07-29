# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverseLL(st,ed):
            curr=st
            n=None
            p=None
            while(curr is not ed):
                n = curr.next
                curr.next = p
                p=curr
                curr=n
            return p
        curr = head
        dummy=ListNode(-100)
        dummy.next=head
        prevGroupEnd=dummy
        while(curr is not None):
            groupStart = curr
            cnt=0
            while((curr is not None) and (cnt<k)):
                curr=curr.next
                cnt+=1
            # reverse from tp tp p and points to then curr
            if(cnt==k):
                NextgroupStart = curr
                rev = reverseLL(groupStart,curr)
                prevGroupEnd.next=rev # p points to groupend
                groupStart.next = NextgroupStart
                prevGroupEnd = groupStart     
        return dummy.next