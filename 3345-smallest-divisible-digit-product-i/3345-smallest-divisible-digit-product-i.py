class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def productOfDigit(n):
            prod = 1
            while(n!=0):
                lstDigit = n%10
                n=n//10
                prod = prod*lstDigit
            return prod
        for i in range(n,101):
            prod = productOfDigit(i)
            if(prod%t==0):
                return i
        return 0
