class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swape(nums,f,e):
            t=nums[f]
            nums[f] = nums[e]
            nums[e]=t
        def reverseArr(nums,s,e):
            while(s<e):
                swape(nums,s,e)
                s+=1
                e-=1
        le= len(nums)-1
        i=le
        smalleridx=-1
        smallerfound=False
        while(i>=1):
            if(nums[i-1]<nums[i]):
                smalleridx=i-1
                smallerfound=True
                break
            i-=1
        
        if(smallerfound):
            maxidx=-1
            i=le
            while(i>=0):
                if(nums[smalleridx]<nums[i]):
                    maxidx=i
                    break
                i-=1
            # swap smallerIdx with it just max element idx
            swape(nums,smalleridx,maxidx)
            reverseArr(nums,smalleridx+1,le)
        else:
            # reverse whole array
            reverseArr(nums,0,le)
        return
