class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq = {}
        # store frequency of each character
        # for x in nums:
        #     freq[x] = freq.get(x,0)
        # start code
        ans=0
        currSum=0
        freq[0]=1
        for x in nums:
            currSum+=x
            if((currSum-k)in freq):
                ans+=freq.get(currSum-k)
            freq[currSum]= freq.get(currSum,0)+1
        return ans
        