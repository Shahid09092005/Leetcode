class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxi=0
        ans=0
        for x in nums:
            if(x==1):
                ans+=1
            else:
                maxi = max(maxi,ans)
                ans=0
        return max(ans,maxi)