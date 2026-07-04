class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = nums[0]
        ans=currSum
        for i in range(1,len(nums)):
            if(currSum<0):
                currSum=0
            currSum+=nums[i]
            ans=max(ans,currSum)
        return ans
        
