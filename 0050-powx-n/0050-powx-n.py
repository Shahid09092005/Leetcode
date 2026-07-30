class Solution:
    def myPow(self, x: float, n: int) -> float:
        def cal(x,n):
            if(n==1):
                return x
            if(n==0):
                return 1
            half = cal(x,n//2)
            if(n%2==0):
                return half*half
            return half*half*x        
        if(n<0):
            x=1/x
            n=-n
        ans = cal(x,n)
        return ans
        