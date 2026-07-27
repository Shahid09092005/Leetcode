class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans=0
        fmax=float('-inf')
        smax=float('-inf')
        for x in nums:
            if(x>=fmax):
                smax=fmax
                fmax=x
            else:
                smax=max(smax,x)
        ans = (fmax-1)*(smax-1)
        return ans