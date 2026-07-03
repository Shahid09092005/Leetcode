class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        if(len(nums)==1 and nums[0]==1):
            return 1
        maxi=0
        tempmax=1
        iscontainOne=False
        for i in range(1,len(nums)):
            if(nums[i]==1 or nums[i-1]==1):
                iscontainOne=True
            if((nums[i]==1) and (nums[i]==nums[i-1])):
                tempmax+=1
                maxi = max(maxi,tempmax)
            else:
                tempmax=1
        if(iscontainOne):
            return max(1,maxi)        
        return maxi