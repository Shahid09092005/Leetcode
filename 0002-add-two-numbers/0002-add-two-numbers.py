# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        tempA=l1
        tempB=l2
        ansh= ListNode(-100)
        anstemp=ansh
        carry=0
        while(tempA is not None and tempB is not None):
            addTwoNum = tempA.val+tempB.val+carry
            hereVal = addTwoNum%10
            carry = (int)(addTwoNum//10)
            anstemp.next = ListNode(hereVal)
            # move to next
            anstemp = anstemp.next
            # move A and B
            tempA = tempA.next
            tempB = tempB.next
        if((tempA is None )and (tempB is not None)):# temp A ends 
            while(tempB is not None):
                addTwoNum = tempB.val+carry
                hereVal = addTwoNum%10
                carry = (int)(addTwoNum//10)
                anstemp.next = ListNode(hereVal)
                # move to next
                anstemp = anstemp.next
                # move B
                tempB = tempB.next
        if((tempA is not None )and (tempB is None)):# temp B ends 
            while(tempA is not None):
                addTwoNum = tempA.val+carry
                hereVal = addTwoNum%10
                carry = (int)(addTwoNum//10)
                anstemp.next = ListNode(hereVal)
                # move to next
                anstemp = anstemp.next
                # move A
                tempA = tempA.next
        if(carry==1):
            anstemp.next = ListNode(1)
            anstemp = anstemp.next
        anstemp.next=None
        return ansh.next
            


            
            