# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        temp=headA
        cntA=0
        while(temp is not None):
            temp=temp.next
            cntA+=1
        temp=headB
        cntB=0
        while(temp is not None):
            temp=temp.next
            cntB+=1
        diff = abs(cntA-cntB)
        if(cntA>cntB):
            while(diff!=0):
                headA=headA.next
                diff-=1
        else:
            while(diff!=0):
                headB=headB.next
                diff-=1
        # move and check
        while((headA is not None ) or (headB is not None)):
            if(headA==headB):
                return headA
            headA=headA.next
            headB=headB.next
        return None