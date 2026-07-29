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
        addTwoNum=0
        while((tempA is not None) or (tempB is not None)):
            addTwoNum=carry
            if(tempA is not None):
                addTwoNum += tempA.val
                tempA = tempA.next
            if(tempB is not None):
                addTwoNum += tempB.val
                tempB = tempB.next
            hereVal = addTwoNum%10
            carry = (int)(addTwoNum//10)
            anstemp.next = ListNode(hereVal)

            # move to next
            anstemp = anstemp.next

        if(carry==1):
            anstemp.next = ListNode(1)
            anstemp = anstemp.next
        anstemp.next=None
        return ansh.next
            


            
            