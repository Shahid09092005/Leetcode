class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ele1=float("-inf")
        cnt1=0
        ele2=float("-inf")
        cnt2=0
        for x in nums:
            if(cnt1==0 and x!=ele2):
                ele1=x
                cnt1+=1
            elif(cnt2==0 and x!=ele1):
                ele2=x
                cnt2+=1
            elif(ele1==x):
                cnt1+=1
            elif(ele2==x):
                cnt2+=1
            else:
                cnt1-=1
                cnt2-=1
                # Note: if anyone goes to 0 so no need to assign here they already assign above because 'x' defeat both the number as per 'Boyer-Moore operation'
                # You should not immediately select x as a candidate inside the same else block.
        # now check ele1 and ele2 are valid
        n=len(nums)
        maj = (int)(n/3)
        cnt1=0
        cnt2=0
        for x in nums:
            if(x==ele1):
                cnt1+=1
            elif (x==ele2):
                cnt2+=1
        # adding the in the list of both element
        lst=[]
        if(cnt1>maj):
            lst.append(ele1)
        if(cnt2>maj):
            lst.append(ele2)

        # print(ele1)
        # print(ele2)
        # print(lst)
        # sort both the element
        if(len(lst)<2):
            return lst
        if(lst[0]>lst[1]):
            t=lst[0]
            lst[0] =lst[1]
            lst[1]=t
        return lst
            