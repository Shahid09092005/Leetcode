class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n=len(nums)
        if(n==1 or n==2):
            return n
        for i in range(1,n):
            expo = 2**i
            if(expo>n):
                return expo
        return 0
        