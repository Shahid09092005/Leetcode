class Solution:
    def maxProduct(self, n: int) -> int:
        firstMax=float("-inf")
        secondMax = float("-inf")
        while(n!=0):
            rem = n%10
            if(rem>=firstMax):
                secondMax = max(secondMax,firstMax)
                firstMax = rem
            else:
                secondMax = max(secondMax,rem)
            n=n//10
        return firstMax*secondMax
        
        